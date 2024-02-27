from kuksa_client.grpc import Datapoint
from kuksa_client.grpc import VSSClient
from kuksa_client.grpc import DataEntry
from kuksa_client.grpc import DataType
from kuksa_client.grpc import EntryUpdate
from kuksa_client.grpc import Field
from kuksa_client.grpc import Metadata

from ultralytics import YOLO
import cv2
import torch
import torch.nn.functional as F
import time

## Init
drowsiness_model = YOLO('./drowsiness_weights/last.pt')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

phoneUse_model = YOLO('./phone_use_weights/last.pt')

# Speed variable
DELAY_TIME = 0.01

# BORKER_IP = '127.0.0.1'
BORKER_IP = '10.51.249.160'
BROKER_PORT = 55555

API_DISTRACTION_LEVEL = "Vehicle.Driver.DistractionLevel"
API_FATIGUE_LEVEL= "Vehicle.Driver.FatigueLevel"
API_VEHICLE_SPEED= "Vehicle.Speed"

client = VSSClient(BORKER_IP, BROKER_PORT)
client.connect()

# with VSSClient(BORKER_IP, BROKER_PORT) as client:
# values = client.get_target_values(['Vehicle.Driver.DrowsinessScore'])
#################################################################


def calculateDrowsinessScore(prediction, frame_width, frame_height, device):
    """
    Function to calculate drowsiness score
    Input: Prediction from Yolov8, frame_width, frame_height, device
    Output: Drowsiness score
    """
    
    preds = prediction[0].boxes.data
    drowsiness_score = torch.tensor(0, device=device)
    if len(preds) == 1:
        drowsiness_score = 1 - preds[0][-2] if preds[0][-1]==0 else preds[0][-2]
    if len(preds) > 1:
        pred_coords = torch.cat(tuple(pred[:2].unsqueeze(0) for pred in  preds))
        center = torch.tensor([frame_width/2, frame_height/2], device=device)
        center_idx = ((pred_coords - center)).square().sum(dim=1).sqrt().argmin().item()
        
        drowsiness_score = 1 - preds[center_idx][-2] if preds[center_idx][-1]==0 else preds[center_idx][-2]
    
    return int(drowsiness_score.item()*100)



distractionScorePrev = 0
keepPrev = False
startTime = 0
setTime = 0

def calculateDistractionScore(preds, distractionScorePrev, keepPrev, startTime, setTime):
    pred = preds[0].boxes.data
    distractionScore = 0
    if len(pred) >= 1:
        distractionScore = 10 if pred[0][-1] == 0 else 100
    
    if distractionScore > 0:
        startTime = time.time()
        keepPrev = True
        distractionScorePrev = distractionScore


    if keepPrev == False:
        distractionScorePrev = distractionScore


    if keepPrev == True and time.time() - startTime >= setTime:
        distractionScorePrev = distractionScore
        keepPrev = False
    return distractionScore, distractionScorePrev, keepPrev, startTime


cap = cv2.VideoCapture(0)
frame_width = cap.get(3)
frame_height = cap.get(4)
while(cap.isOpened()):
    start_time = time.time()
    ret, frame = cap.read()
    if ret:
        drowsiness_prediction = drowsiness_model(frame, verbose=False)
        phoneUse_prediction = phoneUse_model(frame, verbose=False)

        drowsiness_score = calculateDrowsinessScore(drowsiness_prediction, frame_width, frame_height, device)
        distractionScore, distractionScorePrev, keepPrev, startTime = calculateDistractionScore(phoneUse_prediction, 
                                                                                            distractionScorePrev, keepPrev, startTime, 
                                                                                            setTime)

        cv2.putText(frame, str(drowsiness_score)[:4], (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0, 255, 0), 2, cv2.LINE_AA)
        client.set_current_values({
            API_FATIGUE_LEVEL: Datapoint(drowsiness_score),
            API_DISTRACTION_LEVEL: Datapoint(distractionScore),
        })
        #updates = (EntryUpdate(DataEntry(
        #        API_DISTRACTION_LEVEL,
        #        value=Datapoint(value=distractionScore),
        #        metadata=Metadata(data_type=DataType.FLOAT),
        #    ), (Field.VALUE,)),)
        #client.set(updates=updates)

        time.sleep(DELAY_TIME)
        print(f'Drowsiness Score: {drowsiness_score}   Distraction Score: {distractionScore}   Distraction Score Prev: {distractionScorePrev}    keepPrev: {keepPrev}')
        print(f"Total time to process 1 frame: {time.time() - start_time}")
        print()


    else:
        break
        
cap.release()
cv2.destroyAllWindows()
