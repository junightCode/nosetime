# -*- coding:utf-8 -*-

from nosetime.model.app import celery
from nosetime.model.client import Client
from nosetime.holle.clear_data import NosetimeClearData
from nosetime.holle.send_data import NosetimeSendData
from nosetime.holle.save_data import NosetimeSaveData
from nosetime.handler.handler_exception import HttpError
from nosetime.task import MAX_RETRIES, DEFAULT_RETRY_DELAY


@celery.task(name='nosetime.web.search.list', acks_late=True, bind=True, autoretry_for=(HttpError,),
    retry_kwargs={'max_retries': MAX_RETRIES}, default_retry_delay=DEFAULT_RETRY_DELAY, )
def get_search_list(self,brand,**kwargs):
    page = kwargs.get('page',1)
    res = Client.get_data('search_list',brand,page=page)
    if res:
        NosetimeClearData.clear_search_list(res,page=page,brand=brand)



@celery.task(name='nosetime.web.product.info', acks_late=True, bind=True, autoretry_for=(HttpError,),
    retry_kwargs={'max_retries': MAX_RETRIES}, default_retry_delay=DEFAULT_RETRY_DELAY, )
def get_product_info(self,pid):
    res = Client.get_data('product_info',pid)
    if res:
        data = NosetimeClearData.clear_product_info(res)
        NosetimeSaveData.save_product_info(data)



@celery.task(name='nosetime.web.comment.short', acks_late=True, bind=True, autoretry_for=(HttpError,),
    retry_kwargs={'max_retries': MAX_RETRIES}, default_retry_delay=DEFAULT_RETRY_DELAY, )
def get_comment_short(self,pid,**kwargs):
    ifullname = kwargs.get('ifullname','')
    page = kwargs.get('page',1)
    res = Client.get_data('comment_short',pid,page=page)
    if res :
        NosetimeClearData.clear_comment_short(res,pid=pid,page=page,ifullname=ifullname)



@celery.task(name='nosetime.web.comment.long', acks_late=True, bind=True, autoretry_for=(HttpError,),
    retry_kwargs={'max_retries': MAX_RETRIES}, default_retry_delay=DEFAULT_RETRY_DELAY, )
def get_comment_long(self,pid,**kwargs):
    ifullname = kwargs.get('ifullname', '')
    page = kwargs.get('page', 1)
    res = Client.get_data('comment_long', pid, page=page)
    if res :
        NosetimeClearData.clear_comment_long(res,pid=pid,page=page,ifullname=ifullname)


if __name__ == '__main__':
    pass