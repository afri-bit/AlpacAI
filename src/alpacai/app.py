import argparse
import time

import cv2
import torch
from kuksa_client.grpc import Datapoint
from kuksa_client.grpc import VSSClient

from alpacai.core.perception.distraction.drowsiness import Drawsiness


def dance(args):
    DRIVE_DROWSINESS_SCORE = 100  # No attention 0-100 Full attention

    # Speed variable
    DELAY_TIME = 0.01

    API_DISTRACTION_LEVEL = "Vehicle.Driver.DistractionLevel"
    API_FATIGUE_LEVEL = "Vehicle.Driver.FatigueLevel"

    client = None
    cap = None  # Video capture variable
    drowsiness = None

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    client = VSSClient(args.vehicle_ip, args.vehicle_port)
    client.connect()

    cap = cv2.VideoCapture(0)
    frame_width = cap.get(3)
    frame_height = cap.get(4)

    try:
        while True:
            drowsiness = Drawsiness(args.model_path)
            ret, frame = cap.read()

            assert cap.isOpened()

            start_time = time.time()
            ret, frame = cap.read()

            if ret:
                DRIVE_DROWSINESS_SCORE = drowsiness.calculate(frame, frame_width, frame_height, device)

                cv2.putText(frame, "Drowsiness score: " + str(DRIVE_DROWSINESS_SCORE)[:4], (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2, cv2.LINE_AA)

                client.set_current_values({
                    API_FATIGUE_LEVEL: Datapoint(DRIVE_DROWSINESS_SCORE),
                    API_DISTRACTION_LEVEL: Datapoint(0),
                })

                time.sleep(DELAY_TIME)
                print(f'Drowsiness Score: {DRIVE_DROWSINESS_SCORE}')
                print(f"Total time to process 1 frame: {time.time() - start_time}")

                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print("Skipping frame")
                break
    except KeyboardInterrupt:
        print("AttentionAI -- End of Application")
        return


def run():
    parser = argparse.ArgumentParser(
        prog="AttentiveAI",
        description="Intelligent driver drowsiness avoidance with GenAI")
    parser.add_argument("model_path", help="Path to the driver drowsiness path")
    parser.add_argument("-vip", "--vehicle_ip", default="127.0.0.1",
                        help="IP address to the vehicle interface communication")
    parser.add_argument("-vp", "--vehicle_port", default="55555", help="Port communication to the vehicle")
    args = parser.parse_args()

    dance(args)

    print("AlpacAI -- End of Application")


if __name__ == "__main__":
    run()
