import requests

async def addToCDN(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'HX-Request': 'true',
        'HX-Trigger': '_gcaptcha_pt',
        'HX-Target': 'target',
        'HX-Current-URL': 'https://ssstik.io/ru',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://ssstik.io',
        'Connection': 'keep-alive',
        'Referer': 'https://ssstik.io/ru',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'ru',
        'tt': 'YWU0QUcy',
    }

    response = requests.post(
        'https://ssstik.io/abc',
        params=params, 
        headers=headers, 
        data=data
        )
    
def downloadVideo(link):
    link = link.split('/')[5::]
    uid = str(link[0])
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
    }

    response = requests.get(
        f'https://tikcdn.io/ssstik/{uid}',
        headers=headers
        )
    
    with open(f'{uid}.mp4','wb') as file:
        file.write(response.content)
    
links = [
    "https://www.tiktok.com/@brai_sa/video/7059710159974681858",
    "https://www.tiktok.com/@arinadubkova/video/7041117309183757569",
    "https://www.tiktok.com/@brai_sa/video/7044882065698884866",
    "https://www.tiktok.com/@brai_sa/video/7015940304620539138",
    "https://www.tiktok.com/@oblomoffrecipe/video/7013687886809713922"
]


for link in links:        
    addToCDN(link)
    downloadVideo(link)


