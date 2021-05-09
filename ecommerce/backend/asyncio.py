import asyncio
import aiohttp
import aiofiles

async def do(data:dict, session:aiohttp.ClientSession,tasks:list):
    response = await get_new_request(method="HEAD", url=data['url'], session=session)
    print(response.status)
    size = response.header.get('content-length')
    #print(size)
    #sections = [[0,0] for _ in range(data['TotalSec'])]
    #each_size = int(size) // data['TotalSections']
    #print(sections)

async def get_new_request(method : str, url : str,session : aiohttp.ClientSession, headers : dict = None) ->aiohttp.ClientSession:
    if headers:
        headers['User-Agent'] = User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
    return await session.request(method=method, url=url,headers=headers)

