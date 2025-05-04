# 🎬 Video Downloader Backend (FastAPI)

This is a simple backend API built with **FastAPI** that allows downloading videos from platforms like TikTok, Instagram, and YouTube using `yt-dlp`. It is designed to be connected with a modern frontend (e.g., built in Next.js).

---

## 🧠 How It Works

- Accepts a video URL via a POST request.
- Uses `yt-dlp` to download the video in the best quality.
- Sends the video back as a downloadable response.
- Deletes the file afterward to save disk space.

---

## 🛠 Requirements

- Python 3.11+
- Docker (optional but recommended)
- Python packages:
  - `yt-dlp`
  - `fastapi`
  - `uvicorn`
  - `python-multipart`

### 🔧 Install Manually

```bash
pip install -r requirements.txt
```

---

## 🚀 Running with Docker

1. **Build the image**

```bash
docker build -t fastapi-backend .
```

2. **Run the container**

```bash
docker run -d --name backend-api -p 8000:8000 fastapi-backend
```

✅ The API is now live at:

```
http://<your-vm-ip>:8000
```

---

## 📦 API Endpoint

### `POST /download`

Downloads a video and returns it.

**Request:**

- Content-Type: `multipart/form-data`
- Body:
  - `url`: The video URL to download

**Example using curl:**

```bash
curl -X POST http://localhost:8000/download \
  -F "url=https://www.tiktok.com/@example/video/1234567890" \
  --output video.mp4
```

---

## 🧹 Auto Cleanup

After sending the video, the file is deleted from disk so the server doesn't fill up with junk.

---

## 📝 Project Structure

```
.
├── main.py             # FastAPI application
├── downloader.py       # Video downloading logic
├── Dockerfile          # For building container
├── requirements.txt    # Dependencies
└── downloads/          # (Optional) Temp storage (auto-deleted)
```

---

## 🧪 Local Testing

Start the development server:

```bash
uvicorn main:app --reload
```

Test using Postman or `curl` as shown above.

---

## 📡 Use with Frontend

Ensure your frontend sends a POST request with the video URL inside a `FormData` object to:

```
http://<backend-ip>:8000/download
```

You can deploy this backend to:

- An Ubuntu VM
- Render
- Railway
- Azure (via container apps)

---

## 🛑 Disclaimer

This project is for **educational purposes only**. Use responsibly and respect copyright laws and platform terms of service.

---

## 🙌 Made with ❤️ by Ibrahim
