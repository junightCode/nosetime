# -*- coding:utf-8 -*-
import httpx
import asyncio
import redis
from lxml import etree
from nosetime.handler.handler_connect.nosetime_rds import redis_cluster

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

def get_brand_urls():
    brand_urls = []
    y = [chr(y) for y in range(97, 123)]
    y.insert(0,'hot-trade')
    y.insert(1,'hot-salon')
    for index,value in enumerate(y):
        r = str(index) + "-" + value+'.html'
        url = 'https://www.nosetime.com/pinpai/'+r
        brand_urls.append(url)
    return brand_urls

async def get_brand_name(urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(parse_brand(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


async def parse_brand(url):
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.get(url)
        res = response.text
        tree = etree.HTML(res)
        li_list = tree.xpath('//div[@class="odorlist"]/ul/li')
        for li in li_list:
            text = li.xpath('./a[2]/text()')
            brand_name = '+'.join(text)
            redis_cluster.sadd('nosetime:brand_list', brand_name)





if __name__ == '__main__':
    urls = get_brand_urls()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_brand_name(urls))


