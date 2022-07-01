import pandas as pd
import asyncio
import aiohttp
import os
import time
import warnings
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup as bs
import lxml.html as lh
from lxml.html import builder as E
from bs4 import BeautifulSoup
import numpy as np

with open ("usdot_10+_14.txt", "r") as myfile:
    data = myfile.read()
data=data.replace("[","").replace("]","").replace("'","").replace('"',"")
_all_usdots = data.split(',')
all_usdots=[]
for element in _all_usdots:
    all_usdots.append(element.strip())

url="https://usdot411.com/"
results=[]

def get_tasks(session,usdot_list):
    tasks = []
    for number in usdot_list:
        tasks.append(asyncio.create_task(session.get(
    url=url+number, 
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'X-KEY=eyJpdiI6InVVc01BR3dvYm8xNmEyYko1NnYwTGc9PSIsInZhbHVlIjoiVXBpZDlCbThzdkNDWkcyVityU2UzMXUwaEpOV1o3MG13T0o3Q3o3U0xkdWFnVkdnSll0eHRaZGltV1QwRk1vdUhKVVBTbkkvcEZuV3IzN2VjSXA5OFBENVNCNUlIcHBFQThVbHd5TityRkM3ZURmUWpMWWF5RzU2R0cvTXdFd2M5bUtacVpWUVJBMTNISEM0OGN5bkhvczJDNnlucUJvYWpDaHV2ZS9FWnRZZExXdExHVkFWajFCZDRGU0JMeXl5SG56RmE2bVdtYlpMMFVrWnUydExXa2xRNVVpT1ZpUHhLT3VneXFtbFE4bFl2em1IOVpONlZySExnL0xJaThSVyIsIm1hYyI6IjI1NDI1YWEzZmUwMzRhNDdjODQ3MDhhNDA1YjZiMDBhYzJhMzRiYjU5OTk4YmUxN2NhMzg1OWU0ZDg0NTQ2ZDQifQ%3D%3D; _ga=GA1.1.1581905416.1655785741; __gads=ID=99f07c8c1a291d4d-2257f1a267d40030:T=1655785920:RT=1655785920:S=ALNI_MYlSRLddQtXSEyb4lHHQsOjsdUeUg; __gpi=UID=000006d14ebceca5:T=1655785920:RT=1655807753:S=ALNI_MZh0MOvwE_5nwCwuuuhUqb7KFLpkQ; _ga_2CX7JCZ1RS=GS1.1.1655807743.7.1.1655807957.0',
        'Pragma': 'no-cache',
        'Referer': 'https://usdot411.com/user/search/advanced',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    },
    cookies={
        'X-KEY': 'eyJpdiI6InVVc01BR3dvYm8xNmEyYko1NnYwTGc9PSIsInZhbHVlIjoiVXBpZDlCbThzdkNDWkcyVityU2UzMXUwaEpOV1o3MG13T0o3Q3o3U0xkdWFnVkdnSll0eHRaZGltV1QwRk1vdUhKVVBTbkkvcEZuV3IzN2VjSXA5OFBENVNCNUlIcHBFQThVbHd5TityRkM3ZURmUWpMWWF5RzU2R0cvTXdFd2M5bUtacVpWUVJBMTNISEM0OGN5bkhvczJDNnlucUJvYWpDaHV2ZS9FWnRZZExXdExHVkFWajFCZDRGU0JMeXl5SG56RmE2bVdtYlpMMFVrWnUydExXa2xRNVVpT1ZpUHhLT3VneXFtbFE4bFl2em1IOVpONlZySExnL0xJaThSVyIsIm1hYyI6IjI1NDI1YWEzZmUwMzRhNDdjODQ3MDhhNDA1YjZiMDBhYzJhMzRiYjU5OTk4YmUxN2NhMzg1OWU0ZDg0NTQ2ZDQifQ%3D%3D',
        '_ga': 'GA1.1.1581905416.1655785741',
        '__gads': 'ID=99f07c8c1a291d4d-2257f1a267d40030:T=1655785920:RT=1655785920:S=ALNI_MYlSRLddQtXSEyb4lHHQsOjsdUeUg',
        '__gpi': 'UID=000006d14ebceca5:T=1655785920:RT=1656587976:S=ALNI_MZh0MOvwE_5nwCwuuuhUqb7KFLpkQ',
        '_ga_2CX7JCZ1RS': 'GS1.1.1656587961.38.1.1656587999.0',
    },ssl=False)))
    return tasks


async def get_symbols(usdot_list):
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session,usdot_list)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.text())




print(f"usdot number count in file : {len(all_usdots)}")
all_usdots_splited=np.array_split(all_usdots, 5)

start = time.time()
range=[]

count=1
for _list in all_usdots_splited:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_symbols(_list))
    range.extend(list(_list))
    print(f"{count}. {len(_list)} api calls sent")  
    count+=1
    loop.close()
     
    

#clean
print("Cleaning......")
cleaned_content=[]
for html_string in results:
    soup = bs(html_string)               
    prettyHTML = soup.prettify()
    cleantext = BeautifulSoup(prettyHTML, "lxml").text.strip('\n')
    cleantext=' '.join(cleantext.split())
    cleaned_content.append(cleantext)


end = time.time()
total_time = end - start

# print(cleaned_content)
print("\nResult")
print(f"all USDOTs in file : {len(all_usdots)}")
print(f"responses : {len(results)}")
print(f"cleaned content len : {len(cleaned_content)}")
print("It took {} seconds to make {} API calls".format(total_time, len(range)))


df = pd.DataFrame(list(zip((range), cleaned_content)), columns =['USDOT', 'content'])
df.to_csv (r'../raw_data/raw_14.csv', index = False, header=True)