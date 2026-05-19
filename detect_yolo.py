import cv2
import time
import argparse

from ultralytics import YOLO
from imutils.video import FPS
from imutils.video import VideoStream

# Argument parser
ap = argparse.ArgumentParser()

ap.add_argument(
    "-v",
    "--video",
    type=str,
    help="Path to input video file"
)

ap.add_argument(
    "-c",
    "--confidence",
    type=float,
    default=0.5,
    help="Confidence threshold"
)

args = vars(ap.parse_args())

# Load YOLOv8 Nano model
print("[INFO] Loading YOLOv8 model...")
model = YOLO("yolov8n.pt")

# Start video stream
if not args.get("video", False):
    print("[INFO] Starting webcam...")
    vs = VideoStream(src=0).start()
    time.sleep(2.0)
else:
    vs = cv2.VideoCapture(args["video"])

fps = FPS().start()
prev_time = time.time()

# Main loop
while True:

    # Read frame
    frame = vs.read()
    frame = frame[1] if args.get("video", False) else frame

    if frame is None:
        break

    # Resize frame
    frame = cv2.resize(frame, (800, 600))

    # Run YOLO inference
    results = model(frame, conf=args["confidence"])

    # Plot detections
    annotated_frame = results[0].plot()

    # Show FPS
    fps.update()

    current_time = time.time()

    fps_value = 1 / (current_time - prev_time)

    prev_time = current_time

    cv2.putText(
        annotated_frame,
        f"FPS: {fps_value:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Display output
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

fps.stop()

print("[INFO] Elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] Approximate FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()

if args.get("video", False):
    vs.release()
else:
    vs.stop()