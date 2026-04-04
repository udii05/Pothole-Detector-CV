import gradio as gr
from ultralytics import YOLO

model = YOLO("../runs/detect/pothole_detector/weights/best.pt")

def detect(image):
    results = model(image)
    return results[0].plot()

iface = gr.Interface(
    fn=detect,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Image(type="numpy"),
    title="Pothole Detection System",
    description="Upload a road image to detect potholes"
)

iface.launch()