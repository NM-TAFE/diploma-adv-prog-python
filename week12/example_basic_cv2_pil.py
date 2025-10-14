# cv2 VideoCapture of oop.mp4
# Get:
# FPS, Resolution, Duration
# Function to save frame at a specific Point in Time and save as image (jpeg/png/etc)

# %%
import cv2
from PIL import Image
import numpy as np
from pathlib import Path

VID_PATH = Path("resources")


def get_image_from(seconds: int,
                   cap: cv2.VideoCapture,
                   file_path: str | Path = 'output.png') -> None:
    """For a given frame, save an image to the capture file"""

    def frame_position() -> int:
        """Given a time in (s),
        Returns the frame number"""
        return int(seconds * cap.get(cv2.CAP_PROP_FPS))

    def get_frame_in_rgb(frame_number: int) -> np.ndarray:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()
        if not ret:
            raise ValueError(f"Invalid read {frame_number}")
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_array = get_frame_in_rgb(frame_position())
    image = Image.fromarray(frame_array)
    image.save(file_path)


# def save_image_from
# %%
def main():
    cap = cv2.VideoCapture(VID_PATH / "oop.mp4") # type: ignore

    # %%
    if not cap.isOpened():
        raise ValueError(f"Cannot open video in Path")
    # %%
    print("FPS:", fps := cap.get(cv2.CAP_PROP_FPS))
    print("TOTAL FRAMES:", frames := cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Duration (m):", round(frames/fps/60, 2))
    seconds = int(input("Time in (s): "))
    get_image_from(seconds, cap, Path("output/output.png"))


if __name__ == '__main__':
    main()
