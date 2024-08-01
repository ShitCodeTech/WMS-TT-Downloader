import requests
# import json

# response = requests.get('https://www.tiktok.com/api/related/item_list/?WebIdLastTime=1722449892&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%29&channel=tiktok_web&clientABVersions=70508271%2C72135780%2C72213608%2C72406134%2C72422697%2C72430803%2C72444799%2C72479967%2C72508181%2C72508984%2C72514055%2C72527747%2C70405643%2C71057832%2C71200802&cookie_enabled=true&count=16&coverFormat=2&cursor=0&data_collection_enabled=true&device_id=7397865885422175777&device_platform=web_pc&focus_state=false&from_page=video&history_len=9&isNonPersonalized=false&is_fullscreen=false&is_page_visible=true&itemID=7374169946097503521&language=en&odinId=7397873809720722465&os=linux&priority_region=&referer=&region=FI&screen_height=1080&screen_width=1920&tz_name=Asia%2FYekaterinburg&user_is_login=false&webcast_language=en')


# data = response.json()


# print(data['itemList'])
# print(data['itemList']['0'])
# print(data['itemList']['0']['video'])
# print(data['itemList']['0']['video']['playAddr'])

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


download_video('https://www.tiktok.com/@amazingnellytv/video/7376932683466706208')