# -*- coding:utf-8 -*-
import json
from nosetime.holle.send_data import NosetimeSendData
from nosetime.handler.handler_connect.nosetime_rds import redis_cluster

class NosetimeSaveData():

    @classmethod
    def save_product_info(cls,data):
        data_ = json.dumps(data,ensure_ascii=False)
        redis_cluster.hset('nosetime:product_info',data['pid'],data_)

        NosetimeSendData.send_comment_short(data['pid'],ifullname=data['ifullname'])
        NosetimeSendData.send_comment_long(data['pid'], ifullname=data['ifullname'])
