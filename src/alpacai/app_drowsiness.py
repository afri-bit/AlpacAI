import argparse
import logging
import pathlib
import sys
import time

import cv2
from kuksa_client.grpc import Datapoint
from kuksa_client.grpc import VSSClient

from alpacai.core.perception.distraction.drowsiness import Drawsiness

# Speed variable
DELAY_TIME = 0.01

BORKER_IP = '10.51.249.160'
BROKER_PORT = 55555

API_DISTRACTION_LEVEL = "Vehicle.Driver.DistractionLevel"
API_FATIGUE_LEVEL = "Vehicle.Driver.FatigueLevel"
API_VEHICLE_SPEED = "Vehicle.Speed"

client = VSSClient(BORKER_IP, BROKER_PORT)
client.connect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Driver Drowsiness Score',
        description='Calculate driver drowsiness level based on camera sensor')
    parser.add_argument('drowsiness_model')
    args = parser.parse_args()

    # Check the path, if exist
    model_path = pathlib.Path(args.drowsiness_model).absolute()

    if not model_path.is_file():
        logging.error("Unable to find the model. Exiting program")
        sys.exit(1)

    drawsiness = Drawsiness(model_path.resolve())

    cap = cv2.VideoCapture(0)
    frame_width = cap.get(3)
    frame_height = cap.get(4)

    try:
        while (cap.isOpened()):
            start_time = time.time()
            ret, frame = cap.read()
            if ret:
                drowsiness_score = drawsiness.calculate(frame, frame_width, frame_height, device)
                cv2.putText(frame, "Drowsiness score: " + str(drowsiness_score)[:4], (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2, cv2.LINE_AA)
                client.set_current_values({
                    API_FATIGUE_LEVEL: Datapoint(drowsiness_score),
                    API_DISTRACTION_LEVEL: Datapoint(0),
                })
                time.sleep(DELAY_TIME)
                print(f'Drowsiness Score: {drowsiness_score}')
                print(f"Total time to process 1 frame: {time.time() - start_time}")
                print()

                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows()
        sys.exit()

    cap.release()
    cv2.destroyAllWindows()
