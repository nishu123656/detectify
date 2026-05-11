from flask import Flask, request, jsonify, render_template, Response
from ultralytics import YOLO
import cv2, os, uuid

# ── Auto download model from Google Drive ──
MODEL_PATH = 'best.pt'

if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    import urllib.request
    FILE_ID = "1hSCtOnQ0Q-q7C6R6OwtKtGG9ZXNpwqXl"   # ← Step 5 wali ID
    url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"
    urllib.request.urlretrieve(url, MODEL_PATH)
    print("Model downloaded!")

app = Flask(__name__)
os.makedirs('static/uploads', exist_ok=True)
model = YOLO(MODEL_PATH)

model = YOLO('runs/detect/rooftop_detector-3/weights/best.pt')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image"}), 400

    file = request.files['image']
    filename = f"{uuid.uuid4().hex}.jpg"
    filepath = os.path.join('static/uploads', filename)
    file.save(filepath)

    results = model(filepath)[0]

    detections = []
    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])
        detections.append({
            "label": label,
            "confidence": f"{conf*100:.1f}%"
        })

    annotated = results.plot()
    result_filename = f"result_{filename}"
    result_path = os.path.join('static/uploads', result_filename)
    cv2.imwrite(result_path, annotated)

    return jsonify({
        "detections": detections,
        "total": len(detections),
        "result_image": f"/static/uploads/{result_filename}"
    })

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, verbose=False)[0]
        annotated = results.plot()
        _, buffer = cv2.imencode('.jpg', annotated)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, port=5000)