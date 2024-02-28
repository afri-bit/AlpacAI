import torch
from ultralytics import YOLO


class Drawsiness:
    drawsiness_model = None
    device = None

    def __init__(self, drawsiness_model_path: str):
        self.drawsiness_model_path = drawsiness_model_path
        try:
            self.drawsiness_model = YOLO(self.drawsiness_model_path)
        except:
            raise ValueError("Unable to load the model")

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def calculate(self, frame, frame_width, frame_height, device) -> int:
        """
        Function to calculate drowsiness score
        Args:
            frame: Picture frame
            frame_width:
            frame_height:
            device:

        Returns: Drawsiness score in percentage level

        """
        """

        Input: Prediction from Yolov8, frame_width, frame_height, device
        Output: Drowsiness score
        """

        drowsiness_prediction = self.drowsiness_model(frame, verbose=False)

        preds = drowsiness_prediction[0].boxes.data
        drowsiness_score = torch.tensor(0, device=device)

        if len(preds) == 1:
            drowsiness_score = 1 - preds[0][-2] if preds[0][-1] == 0 else preds[0][-2]

        if len(preds) > 1:
            pred_coords = torch.cat(tuple(pred[:2].unsqueeze(0) for pred in preds))
            center = torch.tensor([frame_width / 2, frame_height / 2], device=device)
            center_idx = ((pred_coords - center)).square().sum(dim=1).sqrt().argmin().item()

            drowsiness_score = 1 - preds[center_idx][-2] if preds[center_idx][-1] == 0 else preds[center_idx][-2]

        return int(drowsiness_score.item() * 100)
