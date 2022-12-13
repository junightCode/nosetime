# -*- coding:utf-8 -*-
from nosetime.model.app import celery


class NosetimeSendData():

    @classmethod
    def send_search_list(cls,data,page,**kwargs):
        celery.send_task('nosetime.web.search.list', args=(data,), priority=0,kwargs={'page':page})

    @classmethod
    def send_product_info(cls,data,**kwargs):
        celery.send_task('nosetime.web.product.info',args=(data,), priority=0)

    @classmethod
    def send_comment_short(cls,data,**kwargs):
        page = kwargs.get('page',1)
        ifullname = kwargs.get('ifullname','')

        celery.send_task('nosetime.web.comment.short',args=(data,), priority=0,kwargs={'page':page,'ifullname':ifullname})

    @classmethod
    def send_comment_long(cls, data, **kwargs):
        page = kwargs.get('page', 1)
        ifullname = kwargs.get('ifullname','')
        celery.send_task('nosetime.web.comment.long', args=(data,), priority=0, kwargs={'page': page,'ifullname':ifullname})
