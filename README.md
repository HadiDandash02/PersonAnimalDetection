YOLOv8 Real-Time Person and Animal Detection
This project demonstrates a real-time object detection system using the YOLOv8 model with OpenCV to detect persons and animals from webcam input. The detections are displayed live and saved into a video file.

📸 Features
Real-time detection using YOLOv8 (Nano version by default)

Highlights persons (green) and animals (blue)

Saves the annotated video to output_detected.mp4

Supports easy model switching and customization

🛠 Requirements
Python 3.8+

OpenCV

Ultralytics YOLOv8

Install dependencies via pip:
pip install opencv-python ultralytics
⚠️ Make sure to activate your virtual environment and adjust site.addsitedir() if using custom paths as in the code.

🚀 Usage
Clone this repository:
git clone https://github.com/HadiDandash02/PersonAnimalDetection.git
cd yolov8-animal-person-detector
Run the detection script:
python detect.py
Press Q to quit the live stream.

The output video will be saved as output_detected.mp4.

🎯 Supported Classes
This implementation detects:

👤 Person (COCO class ID 0)

🐕 Animals (COCO class IDs 15–23):

cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe

You can customize this list by modifying the animal_classes array.

🧠 Model
The script uses the YOLOv8n (nano) model by default:
python
model = YOLO('yolov8n.pt')
To use a custom-trained model or another YOLOv8 variant (e.g., yolov8s.pt), update the model path accordingly.

📂 Project Structure

├── detect.py               # Main detection script
├── output_detected.mp4     # Output video (created after running)
├── README.md               # Project documentation
📃 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgements
Ultralytics for the YOLOv8 models

OpenCV for real-time video processing
