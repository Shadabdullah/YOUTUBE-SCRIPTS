from pytube import YouTube

def download_youtube_video(url, output_path):
    try:
        # Create a YouTube object
        youtube = YouTube(url)

        # Get the first available video format
        video = youtube.streams.first()

        # Download the video
        video.download(output_path)

        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
video_url = "https://youtu.be/PjYWpd7xkaM?si=o6STRIVdZTExert0"
output_path = "D:\VIDEOS\REACT"

download_youtube_video(video_url, output_path)






