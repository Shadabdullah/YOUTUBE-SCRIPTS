import pytube
import json

def get_video_links(playlist_url):
    playlist = pytube.Playlist(playlist_url)
    video_links = list(playlist.video_urls)  # Convert to a list
    return video_links

# Example usage
playlist_url = 'https://youtube.com/playlist?list=PLbGui_ZYuhijTKyrlu-0g5GcP9nUp_HlN'
video_links = get_video_links(playlist_url)

# Load existing JSON data, if any
existing_data = {}
try:
    with open('Links.json', 'r') as file:
        existing_data = json.load(file)
except FileNotFoundError:
    pass

# Update the existing data with the video links
existing_data['vidList'] = video_links

# Write the updated data to the JSON file
with open('Links.json', 'w') as file:
    json.dump(existing_data, file)




