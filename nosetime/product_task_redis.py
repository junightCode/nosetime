# -*- coding:utf-8 -*-
import time
import json
from nosetime.model.app import celery
from nosetime.handler.handler_connect.nosetime_rds import redis_cluster

def run():
    for k,v in redis_cluster.hscan_iter('nosetime:product_info'):
        value = json.loads(v)
        pid = value['pid']
        ifullname = value['ifullname']
        celery.send_task('nosetime.web.comment.short',args=(pid,),kwargs={'ifullname':ifullname})
        celery.send_task('nosetime.web.comment.long',args=(pid,),kwargs={'ifullname':ifullname})


if __name__ == '__main__':
    run()