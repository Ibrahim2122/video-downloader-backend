from fastapi import FastAPI, Form, BackgroundTasks
from fastapi.responses import FileResponse
import os
from downloader import download_video
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ibrahimdev.cloud", "https://vid-download.ibrahimdev.cloud"],  # You can restrict this to ["http://localhost:3000", "https://yourdomain.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Video Downloader API!"}

@app.post("/download")
async def download_route(background_tasks: BackgroundTasks, url: str = Form(...)):
    file_path = download_video(url)
    background_tasks.add_task(os.remove, file_path)

    return FileResponse(
        file_path, 
        media_type="video/mp4", 
        filename=os.path.basename(file_path)
        )

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", port=8000, reload=True)


