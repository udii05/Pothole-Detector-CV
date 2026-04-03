# 🎨 ColorFlux – DevOps Deployment Demo Project

[![Python](https://img.shields.io/badge/Python-grey?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-black?style=for-the-badge)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Gradio](https://img.shields.io/badge/Gradio-FF7C00?style=for-the-badge)](https://www.gradio.app/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)](https://matplotlib.org/)

---

## 📌 Overview

**Pothole Detector** is a computer vision project that uses deep learning to automatically detect potholes in road images. The system is built using the YOLOv8 object detection model and aims to assist in road condition monitoring by identifying and localizing potholes efficiently.

The model is trained on annotated datasets in YOLO format and can detect potholes in real-time images. A simple web interface is also provided for easy testing and demonstration.

---

## ⭐ Features
- Detects potholes using YOLOv8
- Uses transfer learning for efficient training
- Supports image-based inference
- Real-time testing using Gradio UI
- Provides bounding box predictions

---

# 🚀 Getting Started

## 1️⃣ Prerequisites

Make sure the following are installed:

- **Python (3.8 or above)**
- **Git**
- **pip**

---

# 2️⃣ Clone the Repository

```bash
git clone https://github.com/udii05/Pothole-Detector-CV.git
cd Pothole-Detector-CV
```

---

# 3️⃣ Setup Virtual Environment

```bash
python -m venv venv
```
Activate it:
Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```
---

# 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---
## 📁 Project Structure
```tree
Pothole-Detector-CV/
├── data/
│   ├── train/
│   ├── valid/
│   ├── test/
│   └── data.yaml
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_training.ipynb
│   └── 03_evaluation.ipynb
│
├── src/
│   ├── train.py
│   ├── inference.py
│   ├── demo.py
│   └── augment.py
│
├── results/
├── requirements.txt
├── README.md
└── .gitignore
```

### **⭐ Support**
If you liked this project, please star the repo — it really motivates me.
- and follow for more updates!
---

Udita Chakraborty
<p align="left"> <a href="https://github.com/udii05"> <img src="https://img.shields.io/badge/GitHub-udii05-black?style=flat-square&logo=github"> </a> <a href="https://www.linkedin.com/in/udita-chakraborty-b890982a2/"> <img src="https://img.shields.io/badge/LinkedIn-Udita%20Chakraborty-blue?style=flat-square&logo=linkedin"> </a> <a href="https://www.instagram.com/u_dii05"> <img src="https://img.shields.io/badge/Instagram-@u_dii05-e84393?style=flat-square&logo=instagram"> </a> </p>