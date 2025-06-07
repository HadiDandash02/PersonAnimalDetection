import cv2
import sys
import site

# Add your virtual environment packages path
site.addsitedir(r"C:\Users\11\finale_project\Lib\site-packages")

from ultralytics import YOLO

# Load YOLOv8 model (change to yolov8n.pt or your trained model)
model = YOLO('yolov8n.pt')

# Open webcam (0)
cap = cv2.VideoCapture(0)

# Get width and height of the video frames
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
if fps == 0:
    fps = 30  # fallback fps if webcam doesn't return it properly

# Define the codec and create VideoWriter to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'XVID', 'MJPG'
out = cv2.VideoWriter('output_detected.mp4', fourcc, fps, (width, height))

# COCO animal classes IDs (15-23)
animal_classes = [15, 16, 17, 18, 19, 20, 21, 22, 23]

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Failed to read from webcam.")
        break

    results = model(frame, verbose=False)[0]

    for box in results.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]

        if cls_id == 0:  # person
            color = (0, 255, 0)  # green
            label_text = f"Person ({conf:.2f})"
        elif cls_id in animal_classes:
            color = (255, 0, 0)  # blue
            label_text = f"Animal: {label} ({conf:.2f})"
        else:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label_text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Write the frame with bounding boxes to the output video
    out.write(frame)

    cv2.imshow("Person and Animal Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
out.release()
cv2.destroyAllWindows()
