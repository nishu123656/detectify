# 🛰️ Detectify — Rooftop AI Object Detection

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-FF6B35?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-REST%20API-000000?style=for-the-badge&logo=flask)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Real-time rooftop object detection powered by YOLOv8 deep learning**

[🔴 Live Demo](https://detectify.onrender.com) · [📂 GitHub](https://github.com/nishu123656/detectify) · [🐛 Report Bug](https://github.com/nishu123656/detectify/issues)

</div>

---

## 📸 Preview

> Upload any rooftop image or stream live camera feed — Detectify identifies objects with bounding boxes and confidence scores in real time.

---

## ✨ Features

- 🔍 **Image Upload Detection** — Upload JPG/PNG/WEBP and get instant results
- 📹 **Live Camera Detection** — Real-time YOLOv8 inference via webcam stream
- 📦 **Bounding Boxes** — Annotated output image with labeled detections
- 📊 **Confidence Scores** — Each detection shown with accuracy percentage
- 🌐 **REST API** — Flask-powered backend with `/predict` endpoint
- 🎨 **Modern UI** — Dark futuristic interface with drag & drop support

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| AI Model | YOLOv8 (Ultralytics) |
| Backend | Python · Flask · REST API |
| Computer Vision | OpenCV · NumPy |
| Frontend | HTML · CSS · JavaScript |
| Deployment | Render · Gunicorn |

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/nishu123656/detectify.git
cd detectify
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

### 5. Open in browser
```
http://localhost:5000
```

---

## 📡 API Reference

### `POST /predict`

Upload an image and get detection results.

**Request**
```
Content-Type: multipart/form-data
Body: image (file)
```

**Response**
```json
{
  "total": 3,
  "detections": [
    { "label": "solar_panel", "confidence": "91.2%" },
    { "label": "water_tank",  "confidence": "87.5%" },
    { "label": "ac_unit",     "confidence": "76.3%" }
  ],
  "result_image": "/static/uploads/result_abc123.jpg"
}
```

### `GET /video_feed`
Returns a multipart MJPEG stream for live camera detection.

---

## 📁 Project Structure

```
detectify/
├── templates/
│   └── index.html              # Frontend UI
├── static/
│   └── uploads/                # Uploaded & result images
├── runs/
│   └── detect/
│       └── rooftop_detector/
│           └── weights/
│               └── best.pt     # Trained YOLOv8 model
├── app.py                      # Flask application
├── train.py                    # Model training script
├── requirements.txt
└── Procfile                    # Render deployment
```

---

## 🧠 Model Training

```bash
python train.py
```

Trained on rooftop object dataset with:
- **Architecture:** YOLOv8n (Nano)
- **Image Size:** 640×640
- **Epochs:** 50
- **Dataset:** Custom rooftop imagery (Roboflow)

---

## 🌐 Deployment

Deployed on **Render** with Gunicorn WSGI server.

```
Start Command: gunicorn app:app
```

---

## 👨‍💻 Author

**Nishu Kumar**
MCA Student

[![GitHub](https://img.shields.io/badge/GitHub-nishu123656-181717?style=flat&logo=github)](https://github.com/nishu123656)

---

## 📄 License

```
© 2025 Nishu Kumar. All rights reserved.
```

---

<div align="center">
Made with ❤️ by <b>Nishu Kumar</b>
</div>
