# -*- coding:utf-8 -*-
import json
from nosetime.holle.Kits import Kit
from nosetime.holle.send_data import NosetimeSendData
from nosetime.handler.handler_connect.nosetime_rds import redis_cluster


class NosetimeClearData():

    @classmethod
    def clear_search_list(cls,response,**kwargs):
        page = kwargs.get('page',1)
        brand = kwargs.get('brand',None)
        datas = response['item'].get('data', None)
        if datas and datas != []:
            for data in datas:
                pid = data['id']
                NosetimeSendData.send_product_info(pid)
            page += 1
            NosetimeSendData.send_search_list(brand,page=page)


    @classmethod
    def clear_product_info(cls,response):
        pid = response['id']  # 商品id
        ifullname = response['ifullname']  # 商品标题
        brand = response['brand']  # 品牌
        fragrance = response['fragrance']  # 香调
        top = ' '.join(response.get('top', ''))  # 前调
        middle = ' '.join(response.get('middle', ''))  # 中调
        base = ' '.join(response.get('base', ''))  # 后调
        isscore = response.get('isscore', 0)  # 评分
        istotal = response.get('istotal', 0)  # 评分人数
        data = {
            'pid': pid,
            'ifullname': ifullname,
            'brand': brand,
            'fragrance': fragrance,
            'top': top,
            'middle': middle,
            'base': base,
            'isscore': isscore,
            'istotal': istotal,
        }
        return data

    @classmethod
    def clear_comment_short(cls,response,**kwargs):
        ifullname = kwargs.get('ifullname','')
        page = kwargs.get('page',1)
        pid = kwargs.get('pid','')
        reply = response.get('reply',None)
        if reply:
            comments = []
            for ele in reply:
                uname = ele['uname']
                content = ele['content']
                up = ele['up']
                comments.append({
                    'name': uname,
                    'content': content,
                    'up': up,
                })
                sub = ele.get('sub', None)
                if sub:
                    for s in sub:
                        sname = s['uname']
                        scontent = s['urcontent']
                        sup = s['up']
                        comments.append({
                            'name': sname,
                            'content': scontent,
                            'up': sup,
                        })
            for comment in comments:
                data = {
                    'ifullname': ifullname,
                    'type': '一句话香评',
                    'name': comment['name'],
                    'content': comment['content'],
                    'up': comment['up'],
                    'timestamp': Kit.timestandard_now(),
                    'pid':pid,
                }
                #入库
                # print(data)
                data_ = json.dumps(data, ensure_ascii=False)
                if r'\x' not in data_:
                    redis_cluster.lpush('nosetime:comment_short',data_ )
            # 翻页
            page += 1
            NosetimeSendData.send_comment_short(pid,page=page,ifullname=ifullname)


    @classmethod
    def clear_comment_long(cls,response,**kwargs):
        ifullname = kwargs.get('ifullname', '')
        page = kwargs.get('page', 1)
        pid = kwargs.get('pid')
        if response :
            for res in response:
                uname = res['uname']
                udtime = res['udtime']
                ucontent = res['content']
                ucontent = ucontent.replace('\n','').replace('\t','')
                udup = res['udup']
                data = {
                    'ifullname': ifullname,
                    'type': '香水评论',
                    'name': uname,
                    'time': udtime,
                    'content': ucontent,
                    'up': udup,
                    'pid': pid,
                    'timestamp': Kit.timestandard_now(),
                }
                # 入库
                # print(data)
                data_ = json.dumps(data, ensure_ascii=False)
                if r'\x' not in data_:
                    redis_cluster.lpush('nosetime:comment_long',data_)
            page += 1
            NosetimeSendData.send_comment_long(pid,page=page,ifullname=ifullname)
