from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(
    data='objects-1/data.yaml',
    epochs=50,
    imgsz=640,
    batch=8,
    patience=15,
    name='rooftop_detector'
)

print("✅ Training complete!")