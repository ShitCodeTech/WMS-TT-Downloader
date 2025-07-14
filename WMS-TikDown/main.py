from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
import httpx
import aiofiles

app = FastAPI()
# Shared async HTTP client
client = httpx.AsyncClient(timeout=30.0)

# Pydantic models for request and response
class DownRequest(BaseModel):
    link: str

class DownResponse(BaseModel):
    link: str
    bytearr: str
    status: str
    detail: str | None = None

# Async helper functions
async def add_to_cdn(link: str) -> None:
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
    params = {'url': 'dl'}
    data = {
        'id': link,
        'locale': 'ru',
        'tt': 'YWU0QUcy',
    }

    resp = await client.post(
        'https://ssstik.io/abc',
        headers=headers,
        params=params,
        data=data
    )
    resp.raise_for_status()

async def download_video(link: str):
    uid = link.rstrip('/').split('/')[-1]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Accept': 'application/octet-stream',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'none',
    }

    # resp = await client.get(f'https://tikcdn.io/ssstik/{uid}', headers=headers)
    # resp.raise_for_status()

    # return resp.content

    # async with aiofiles.open(f'{uid}.mp4', 'wb') as f:
    #     await f.write(resp.content)

    return (f'https://tikcdn.io/ssstik/{uid}')

async def process_link(link: str) -> DownResponse:
    try:
        await add_to_cdn(link)
        bytearr = await download_video(link)
        return DownResponse(link=link,bytearr=bytearr, status="success")
    except Exception as e:
        return DownResponse(link=link, status="error", detail=str(e))

# FastAPI endpoint: single link per request
@app.post("/down", response_model=DownResponse)
async def download_endpoint(request: DownRequest):
    """
    Trigger download for a single TikTok URL.
    Returns status and optional error detail.
    """
    result = await process_link(request.link)
    return result

# Cleanup HTTP client on shutdown
def on_shutdown():
    asyncio.create_task(client.aclose())

app.add_event_handler("shutdown", on_shutdown)

# To run: uvicorn fastapi_downloader:app --reload