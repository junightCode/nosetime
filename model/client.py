# -*- coding:utf-8 -*-
import requests
from retrying import retry
from urllib.parse import quote

from nosetime.model.constant import SEARCH_LIST, HEADERS,PRODUCT_INFO,LONG_COMMENT,SHORT_COMMENT


class Client():

    @classmethod
    def get_ip(cls):
        proxies = {}
        return proxies

    @classmethod
    def get_data(cls, type, word, **kwargs):
        word_ = quote(word)
        page = kwargs.get('page',1)
        data = {
            'search_list': {
                'url': SEARCH_LIST.format(page,word_)
            },
            'product_info':{
                'url': PRODUCT_INFO.format(word_)
            },
            'comment_short':{
                'url': SHORT_COMMENT.format(word_,page)
            },
            'comment_long':{
                'url':LONG_COMMENT.format(word_,page)
            }
        }
        rdata = data[type]
        return cls.factory_func(rdata['url'])

    @classmethod
    @retry(stop_max_attempt_number=3)
    def factory_func(cls, url, **kwargs):
        try:
            res = requests.get(url=url,
                               headers=HEADERS,
                               timeout=5,
                               proxies=cls.get_ip(),
                               )
            return res.json()
        except ConnectionError:
            raise ConnectionError('HTTP连接失败')
        except Exception as e:
            print(e)
