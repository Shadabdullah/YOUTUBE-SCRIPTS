

from pytube import YouTube

# URL of the YouTube video you want to download
video_url = "https://youtu.be/WiCj2r0Z7TY?si=iq0xskyelcWvMfke"

# Initialize a YouTube object
yt = YouTube(video_url)

# Select the stream with the highest resolution (usually it's progressive=True)
video_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

# Define the download location (you can change this)
download_path = "D:/VIDEOS/TEMP/video.mp4"

# Download the video
video_stream.download(output_path=download_path)

print("Video downloaded successfully!")
