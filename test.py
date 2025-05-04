from downloader import download_video

# Example TikTok or YouTube short URL
url = "https://www.instagram.com/reel/DJM8Xglsr3D/?utm_source=ig_web_copy_link"

# You can try with "best", "worst", or "bestaudio"
file_path = download_video(url, quality="best")

print("✅ Downloaded file saved at:", file_path)
