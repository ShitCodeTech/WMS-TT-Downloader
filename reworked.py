import requests
from bs4 import BeautifulSoup


def getSourceLink(link):
    
    cookies = {
        'ttwid': '1%7Cjj_YWMUAJrHn7HUzDCjPR7CVqt02ugsCM-RNjYn-PBg%7C1719356903%7C971285f7d4ea421ae1d59002d616b4f107712538338210e959ffe917dfca4aec',
        'tt_chain_token': '+TMf7erS//xc/8JhDgimcw==',
        'passport_csrf_token': '0da9434b4eca2dfbd93b2d68524bc963',
        'passport_csrf_token_default': '0da9434b4eca2dfbd93b2d68524bc963',
        'tt_csrf_token': 'DXzCxLJt-eK_82t2dbYHhhDiIaQ76Zl6Io0g',
        'msToken': 'kgGMZGxYTcPyD1CdZSbWUK5y_Cp0grxTfSYMrFaQG74lHZepZne1N6X82OV-JLgiOF1OHFCbBJTA28rY8GbeZLxkrHuUx741Rv94P5KeUQ9NOY5fTT8M4hqidN_jG3ndCd9j9DuMsuF54WK_qwI=',
        'ak_bmsc': '70C88231755891E60216D3E27CE7C01D~000000000000000000000000000000~YAAQygNJF0rBTQWRAQAAEEdlCRjH2oS4J2zXpbqs0Wj9Y7lnSPw8CXuz3xgdHDZcBMiZPiXbzlFPCQ2FmyoVbg/4nBA0nUaAdUdjFU1jJD6tBBNbFx6k8aJsO26Ls9cZ/wmz3IB9gdHEOnpuHE+lafe+mdmhekogN+9sIDG1jou8axRsqejIzHrJ4syEidi/UgpAtSD5WD2cWMlyBwRYfJwi5BBoxTsOt58jnVi2Ee95Bs3a+2puHpIe9W73V874vvc534ox1o31LddH6BByqWhLf6pNjRsJrMB+5gMEfeoTCxLH7B5MCMy3XwHXpjAa84aLZMH+xKn5R+DKdCWYzpARUvC4OjNNj6HOESHnwnZAJWzM9NF/n1YQXMKJm3fkTQPZnjntl+3AL04=',
        'cookie-consent': '{%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}',
        'bm_sv': 'A9F79CB83A764750175CB483F6219980~YAAQygNJFzhlTgWRAQAAro2LCRi6RqQ7ek05KqzX3PmCoo3/6fH8F8FtIw0gSjYoVHv6INzxf0L42CqC11poR3OePxDPUOUpIW3oGQluf8lXuAC3hq97zdIcWaPJYHdZjXCTP8BONGdTmIVJoUU0OHu6n0pM+ShOwZxO9lcOFSdl8dwG75z+QLkd5HqiiqWIyjjLKpsuDjucu4IBlpju3rhfcUuW8BYOkUyfhJVGoiOq7ShNVjso2TMGekmPVJE0~1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Accept': 'video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.tiktok.com/',
        'Range': 'bytes=0-',
        'Connection': 'keep-alive',
        # 'Cookie': 'ttwid=1%7Cjj_YWMUAJrHn7HUzDCjPR7CVqt02ugsCM-RNjYn-PBg%7C1719356903%7C971285f7d4ea421ae1d59002d616b4f107712538338210e959ffe917dfca4aec; tt_chain_token=+TMf7erS//xc/8JhDgimcw==; passport_csrf_token=0da9434b4eca2dfbd93b2d68524bc963; passport_csrf_token_default=0da9434b4eca2dfbd93b2d68524bc963; tt_csrf_token=DXzCxLJt-eK_82t2dbYHhhDiIaQ76Zl6Io0g; msToken=kgGMZGxYTcPyD1CdZSbWUK5y_Cp0grxTfSYMrFaQG74lHZepZne1N6X82OV-JLgiOF1OHFCbBJTA28rY8GbeZLxkrHuUx741Rv94P5KeUQ9NOY5fTT8M4hqidN_jG3ndCd9j9DuMsuF54WK_qwI=; ak_bmsc=70C88231755891E60216D3E27CE7C01D~000000000000000000000000000000~YAAQygNJF0rBTQWRAQAAEEdlCRjH2oS4J2zXpbqs0Wj9Y7lnSPw8CXuz3xgdHDZcBMiZPiXbzlFPCQ2FmyoVbg/4nBA0nUaAdUdjFU1jJD6tBBNbFx6k8aJsO26Ls9cZ/wmz3IB9gdHEOnpuHE+lafe+mdmhekogN+9sIDG1jou8axRsqejIzHrJ4syEidi/UgpAtSD5WD2cWMlyBwRYfJwi5BBoxTsOt58jnVi2Ee95Bs3a+2puHpIe9W73V874vvc534ox1o31LddH6BByqWhLf6pNjRsJrMB+5gMEfeoTCxLH7B5MCMy3XwHXpjAa84aLZMH+xKn5R+DKdCWYzpARUvC4OjNNj6HOESHnwnZAJWzM9NF/n1YQXMKJm3fkTQPZnjntl+3AL04=; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}; bm_sv=A9F79CB83A764750175CB483F6219980~YAAQygNJFzhlTgWRAQAAro2LCRi6RqQ7ek05KqzX3PmCoo3/6fH8F8FtIw0gSjYoVHv6INzxf0L42CqC11poR3OePxDPUOUpIW3oGQluf8lXuAC3hq97zdIcWaPJYHdZjXCTP8BONGdTmIVJoUU0OHu6n0pM+ShOwZxO9lcOFSdl8dwG75z+QLkd5HqiiqWIyjjLKpsuDjucu4IBlpju3rhfcUuW8BYOkUyfhJVGoiOq7ShNVjso2TMGekmPVJE0~1',
        'Sec-Fetch-Dest': 'video',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        # 'Accept-Encoding': 'identity',
        'Priority': 'u=4',
    }
    response = requests.get(link, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
    print(soup.find('video'))
    asdasd = soup.prettify().encode()
    with open('123.html','wb') as file:
        file.write(asdasd)


getSourceLink('https://www.tiktok.com/@heresmystory0_0/video/7397399688783170849')