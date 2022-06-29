import asyncio
import aiohttp
import os
import time
import warnings
from async_timeout import timeout
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup as bs
import lxml.html as lh
from lxml.html import builder as E
from bs4 import BeautifulSoup
import numpy as np

url = 'https://usdot411.com/user/search/advanced/list'
range=[x for x in range(220000,500000,50)]
results = []


def get_tasks(session,request_gaps):
    tasks = []
    for number in request_gaps:
        tasks.append(asyncio.create_task(session.post(
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
                '__gpi': 'UID=000006d14ebceca5:T=1655785920:RT=1656408940:S=ALNI_MZh0MOvwE_5nwCwuuuhUqb7KFLpkQ',
                '_ga_2CX7JCZ1RS': 'GS1.1.1656412719.26.0.1656412719.0',
            },
            data={
                'state': '',
                'zip': '',
                'distance': '0',
                'hazmat': '',
                'units': '1',
                'start':str(number)
            }, ssl=False)))
    return tasks

async def get_symbols(request_gaps):
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session,request_gaps)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())
    



def get_usdot(html_string):
    usdot=[]
    root = html_string 
    soup = bs(root)               
    prettyHTML = soup.prettify()
    cleantext = BeautifulSoup(prettyHTML, "lxml").text.replace(" ", "").split("USDOT") 
    cleantext.pop(0)
    for line in cleantext:
        try:
            if int(line[:8].replace("\n","")): 
                usdot.append(line[:8].replace("\n","")) 
        except:
            pass
    return usdot








print(f"request gap count in file : {len(range)}")
range_splited=np.array_split(range, 100)

start = time.time()
api_calls=[]
for _list in range_splited:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_symbols(_list))
    api_calls.extend(list(_list))
    print(f"{len(_list)} api calls sent")  
    loop.close()

end = time.time()
total_time = end - start

html_string=""
for data in results:
    try:
        html_string=html_string+(data["data"]["content"])
    except:
        pass



usdots=get_usdot(html_string)

file = open("usdot_10+_11.txt","w") 
file.write(str(usdots))
file.close() 

#time
print("It took {} seconds to make {} API calls".format(total_time, len(api_calls)))
end_2 = time.time()
total_time = end_2 - start
print("It took {} seconds to make {} API calls and extract {} data".format(total_time,len(api_calls),len(usdots)))