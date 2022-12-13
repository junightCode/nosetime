# -*- coding:utf-8 -*-
import time
from nosetime.model.app import celery
from nosetime.handler.handler_connect.nosetime_rds import redis_cluster


def run():
    search_words = redis_cluster.sscan_iter('nosetime:brand_list',count=10)
    for word in search_words:
        print(word)
        celery.send_task('nosetime.web.search.list',args=(word,),priority=0)

def unlink():
    redis_cluster.unlink('nosetime:comment_long')
    redis_cluster.unlink('nosetime:comment_short')
    # redis_cluster.unlink('nosetime:product_info')


if __name__ == '__main__':
    # run()
    # unlink()
    # celery.send_task('nosetime.web.comment.short', args=('449262',), priority=0,kwargs={'ifullname':"爱马仕 大地 Hermes Terre d'Hermes, 2006"})
    # celery.send_task('nosetime.web.comment.long', args=('449262',), priority=0,kwargs={'ifullname':"爱马仕 大地 Hermes Terre d'Hermes, 2006"})
    # celery.send_task('nosetime.web.search.list', args=('塞巴斯汀标记+Sebastian Signs',), priority=0)
    pass

