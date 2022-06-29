import asyncio
from http import cookies
import aiohttp
from pprint import pprint
import json
import time

url = 'https://usdot411.com/user/search/advanced/list'
range=[x for x in range(0,1000,50)]
results = []



start = time.time()

def get_tasks(session):
    tasks = []
    for numbers in range:
        tasks.append(asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False)))
    return tasks


async def fetch(url, session):
    async with session.post(
    url=url, 
    headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'X-KEY=eyJpdiI6InVVc01BR3dvYm8xNmEyYko1NnYwTGc9PSIsInZhbHVlIjoiVXBpZDlCbThzdkNDWkcyVityU2UzMXUwaEpOV1o3MG13T0o3Q3o3U0xkdWFnVkdnSll0eHRaZGltV1QwRk1vdUhKVVBTbkkvcEZuV3IzN2VjSXA5OFBENVNCNUlIcHBFQThVbHd5TityRkM3ZURmUWpMWWF5RzU2R0cvTXdFd2M5bUtacVpWUVJBMTNISEM0OGN5bkhvczJDNnlucUJvYWpDaHV2ZS9FWnRZZExXdExHVkFWajFCZDRGU0JMeXl5SG56RmE2bVdtYlpMMFVrWnUydExXa2xRNVVpT1ZpUHhLT3VneXFtbFE4bFl2em1IOVpONlZySExnL0xJaThSVyIsIm1hYyI6IjI1NDI1YWEzZmUwMzRhNDdjODQ3MDhhNDA1YjZiMDBhYzJhMzRiYjU5OTk4YmUxN2NhMzg1OWU0ZDg0NTQ2ZDQifQ%3D%3D; _ga=GA1.1.1581905416.1655785741; __gads=ID=99f07c8c1a291d4d-2257f1a267d40030:T=1655785920:RT=1655785920:S=ALNI_MYlSRLddQtXSEyb4lHHQsOjsdUeUg; __gpi=UID=000006d14ebceca5:T=1655785920:RT=1655807753:S=ALNI_MZh0MOvwE_5nwCwuuuhUqb7KFLpkQ; _ga_2CX7JCZ1RS=GS1.1.1655807743.7.1.1655807957.0',
        'Origin': 'https://usdot411.com',
        'Pragma': 'no-cache',
        'Referer': 'https://usdot411.com/user/search/advanced',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    },
    cookies={
        'X-KEY': 'eyJpdiI6InVVc01BR3dvYm8xNmEyYko1NnYwTGc9PSIsInZhbHVlIjoiVXBpZDlCbThzdkNDWkcyVityU2UzMXUwaEpOV1o3MG13T0o3Q3o3U0xkdWFnVkdnSll0eHRaZGltV1QwRk1vdUhKVVBTbkkvcEZuV3IzN2VjSXA5OFBENVNCNUlIcHBFQThVbHd5TityRkM3ZURmUWpMWWF5RzU2R0cvTXdFd2M5bUtacVpWUVJBMTNISEM0OGN5bkhvczJDNnlucUJvYWpDaHV2ZS9FWnRZZExXdExHVkFWajFCZDRGU0JMeXl5SG56RmE2bVdtYlpMMFVrWnUydExXa2xRNVVpT1ZpUHhLT3VneXFtbFE4bFl2em1IOVpONlZySExnL0xJaThSVyIsIm1hYyI6IjI1NDI1YWEzZmUwMzRhNDdjODQ3MDhhNDA1YjZiMDBhYzJhMzRiYjU5OTk4YmUxN2NhMzg1OWU0ZDg0NTQ2ZDQifQ%3D%3D',
        '_ga': 'GA1.1.1581905416.1655785741',
        '__gads': 'ID=99f07c8c1a291d4d-2257f1a267d40030:T=1655785920:RT=1655785920:S=ALNI_MYlSRLddQtXSEyb4lHHQsOjsdUeUg',
        '__gpi': 'UID=000006d14ebceca5:T=1655785920:RT=1655807753:S=ALNI_MZh0MOvwE_5nwCwuuuhUqb7KFLpkQ',
        '_ga_2CX7JCZ1RS': 'GS1.1.1655807743.7.1.1655807957.0',
    },
    data={
        'state': '',
        'zip': '',
        'distance': '0',
        'hazmat': '',
        'units': '2',
        'start':str(0)
    }) as response:
        res = await response.json()
        pprint(res["data"]["content"])


async def main():
    async with aiohttp.ClientSession() as session:
        await fetch(url, session)


asyncio.run(main())

# import asyncio
# import aiohttp

# async def make_numbers(numbers, _numbers):
#     for i in range(numbers, _numbers):
#         yield i

# async def make_account():
#     url = "https://example.com/sign_up.php"
#     async with aiohttp.ClientSession() as session:
#         post_tasks = []
#         # prepare the coroutines that post
#         async for x in make_numbers(35691, 5000000):
#             post_tasks.append(do_post(session, url, x))
#         # now execute them all at once
#         await asyncio.gather(*post_tasks)

# async def do_post(session, url, x):
#     async with session.post(url, data ={
#                 "terms": 1,
#                 "captcha": 1,
#                 "email": "user%s@hotmail.com" % str(x),
#                 "full_name": "user%s" % str(x),
#                 "password": "123456",
#                 "username": "auser%s" % str(x)
#           }) as response:
#           data = await response.text()
#           print("-> Created account number %d" % x)
#           print (data)

# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(make_account())
# finally:
#     loop.close()