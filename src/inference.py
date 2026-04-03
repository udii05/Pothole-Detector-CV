from ultralytics import YOLO
import cv2

def run_inference(image_path):
    model = YOLO("runs/detect/pothole_detector/weights/best.pt")

    results = model(image_path)

    # Show result
    for r in results:
        img = r.plot()
        cv2.imshow("Prediction", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    run_inference("test.jpg")  # replace with your image