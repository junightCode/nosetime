# -*- coding:utf-8 -*-

HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

SEARCH_LIST = 'https://www.nosetime.com/search.php?op=ajax&type=3&start=10&page={}&perpage=10&word={}'

PRODUCT_INFO = 'https://www.nosetime.com/app/item.php?id={}'

SHORT_COMMENT = 'https://app.nosetime.com/app/reply.php?type=itemv2&id={}&o=s&page={}'

LONG_COMMENT = 'https://app.nosetime.com/app/item.php?method=discuss&id={}&o=s&page={}'
