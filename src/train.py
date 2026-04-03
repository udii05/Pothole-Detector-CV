from ultralytics import YOLO

def main():
    # Load pretrained YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
        data="data/data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        name="pothole_detector"
    )

if __name__ == "__main__":
    main()