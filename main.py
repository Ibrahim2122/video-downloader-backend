from fastapi import FastAPI, Form, BackgroundTasks
from fastapi.responses import FileResponse
import os
from downloader import download_video

app = FastAPI()

@app.post("/download")
async def download_route(background_tasks: BackgroundTasks, url: str = Form(...)):
    file_path = download_video(url)
    background_tasks.add_task(os.remove, file_path)

    return FileResponse(
        file_path, 
        media_type="video/mp4", 
        filename=os.path.basename(file_path)
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)


