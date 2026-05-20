# Sentinel - Real-Time Object Detection System

## From SSD MobileNet (Caffe) to YOLOv8

## Overview

This project is a real-time object detection system built using Python and computer vision frameworks. The project initially began as a lightweight edge-compatible detection pipeline using OpenCV DNN with SSD MobileNet in Caffe format and was later modernized by migrating to YOLOv8 for improved performance, scalability, and extensibility.

The system is capable of detecting multiple real-world objects such as:

* People
* Cars
* Buses
* Bikes
* Animals
* Bottles
* Chairs
* TV monitors
* And other COCO/Common object classes

The project was designed with a strong focus on:

* Real-time inference
* Lightweight deployment
* Mobile and edge compatibility
* Scalable AI architecture
* Future intelligent analytics integration

---

# Features

## Current Features

* Real-time webcam object detection
* Video file detection support
* YOLOv8-based inference pipeline
* Bounding box visualization
* Confidence score display
* FPS monitoring
* Multi-object detection
* Lightweight edge-compatible architecture

## Previous Architecture

The original version used:

* OpenCV DNN module
* Caffe framework
* SSD MobileNet detector

This provided:

* CPU-friendly inference
* Low computational requirements
* Efficient deployment on lightweight devices

---

# Tech Stack

## Languages

* Python

## Libraries and Frameworks

* OpenCV
* Ultralytics YOLOv8
* NumPy
* Imutils

## Previous Stack

* OpenCV DNN
* Caffe SSD MobileNet

---

# Project Evolution

## Phase 1 — SSD MobileNet + Caffe

Initial architecture:

Frame → Blob Conversion → SSD MobileNet → Bounding Boxes

### Why SSD MobileNet?

The project was initially designed for:

* Mobile phones
* CPU-only systems
* Embedded devices
* Lightweight edge AI deployment

SSD MobileNet provided:

* Low memory usage
* Faster CPU inference
* Lightweight CNN architecture

### Limitations

* Older framework ecosystem
* Lower detection accuracy
* Limited scalability
* Weak small-object detection
* Manual preprocessing pipeline

---

## Phase 2 — YOLOv8 Migration

The project was later migrated to YOLOv8.

Updated architecture:

Frame → YOLOv8 → Results Object → Rendering

### Why YOLOv8?

YOLOv8 provided:

* Better accuracy
* Cleaner architecture
* Faster inference
* Easier deployment
* Built-in tracking support
* Modern PyTorch ecosystem

### Chosen Variant

YOLOv8n (Nano)

Reason:

* Lightweight inference
* Edge-device optimized
* Better speed-accuracy balance

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd <project-folder>
```

---

## Install Dependencies

```bash
pip install ultralytics opencv-python imutils numpy
```

---

# Running the Project

## Webcam Detection

```bash
python detect_yolo.py
```

---

## Video File Detection

```bash
python detect_yolo.py -v test.mp4
```

---

# YOLOv8 Model Download

On first execution:

* YOLOv8 automatically downloads the model weights
* Example:

```text
Downloading yolov8n.pt
```

---

# Project Structure

```text
project/
│
├── detect_yolo.py
├── detectDNN.py
├── yolov8n.pt
├── README.md
├── outputs/
├── videos/
└── models/
```

---

# How the System Works

## Step 1 — Frame Capture

Frames are captured from:

* Webcam
* Video stream
* Video files

---

## Step 2 — Inference

YOLOv8 processes the frame and performs:

* Feature extraction
* Object localization
* Classification
* Confidence scoring
* Non-Maximum Suppression (NMS)

---

## Step 3 — Visualization

The system renders:

* Bounding boxes
* Object labels
* Confidence scores
* FPS metrics

---

# Example Output

Detected objects may include:

```text
person 0.93
car 0.88
bottle 0.81
```

---

# Edge AI Perspective

The project was intentionally designed around lightweight AI deployment.

## Edge Responsibilities

* Image capture
* Lightweight inference
* GPS tagging (future)
* Batch uploads (future)

## Cloud Responsibilities

* Heavy analytics
* Large-scale inference
* Historical analysis
* Risk scoring

This creates a scalable edge-cloud hybrid AI architecture.

---

# Use Cases

## Surveillance Systems

* Human detection
* Restricted zone monitoring
* Crowd analytics

## Traffic Analytics

* Vehicle detection
* Vehicle counting
* Congestion monitoring

## Smart City Applications

* Public safety monitoring
* Infrastructure analytics
* Smart surveillance systems

## Retail Analytics

* Footfall estimation
* Customer movement analytics

---

# Future Scope

## Planned Improvements

* Object tracking
* Segmentation
* Pose estimation
* GPS integration
* Firebase/cloud integration
* Detection logging
* Analytics dashboard
* Custom-trained YOLO models

---

## Road Safety Direction

Potential future expansion:

* Pothole detection
* Waterlogging detection
* Road crack analysis
* Obstruction detection
* Traffic anomaly detection

---

# Performance Notes

## SSD MobileNet

Pros:

* Lightweight
* CPU efficient
* Mobile-friendly

Cons:

* Lower accuracy
* Older ecosystem

---

## YOLOv8n

Pros:

* Higher accuracy
* Modern architecture
* Better extensibility
* Faster inference pipeline

Cons:

* Slightly heavier computationally
* Better performance with GPU acceleration

---

# Learning Outcomes

This project helped build understanding of:

* Deep learning inference pipelines
* CNN-based object detection
* Edge AI concepts
* Real-time computer vision
* Framework migration
* YOLO ecosystem
* Performance tradeoffs
* AI deployment strategies

---

# Conclusion

This project evolved from a lightweight classical object detection pipeline into a modern YOLO-based real-time computer vision system.

The migration from SSD MobileNet + Caffe to YOLOv8 improved:

* Accuracy
* Scalability
* Deployment flexibility
* System extensibility
* Real-world applicability

The project now serves as a strong foundation for future intelligent analytics systems and edge-cloud AI architectures.

---

# Author

Subhranshu Pattnayak
B.Tech CSE
AI/ML Enthusiast

Life Motto:
"Seek wisdom and fear none."
