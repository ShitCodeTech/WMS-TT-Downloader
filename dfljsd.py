import requests
# import fastapi
import time

def download_video(url):
    response = requests.get(url) 
    spl = response.url.split('/') 
    if spl[4] == 'video': 
        video_id = spl[5].split('?')[0] 
        request_url = f'https://www.tikwm.com/video/media/play/${video_id}.mp4' 
        response = requests.get(request_url) 
        video_link = response.url 
        return video_link 
    else: 
        return False

start = time.time()
print(download_video('https://www.tiktok.com/@amazingnellytv/video/7376932683466706208'))

print(time.time() - start)