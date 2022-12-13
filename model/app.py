# -*- coding:utf-8 -*-
import copy
import logging


from celery import Task, Celery
from kombu import Queue, Exchange, binding
from nosetime.holle.queue.crawl_queue import nosetime_queues
from nosetime.handler.setting import config

logger = logging.getLogger("task.redoffice")
class BaseTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error('[%s]: error: %s-%s, args:[%s], kwargs:[%s]' % (exc, self.name, task_id, args, kwargs))

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        logger.warning('[%s]:retry: %s-%s,  args:[%s], kwargs:[%s]' % (exc, self.name, task_id, args, kwargs))

    def on_success(self, retval, task_id, args, kwargs):
        logger.info('%s-[%s]:success, args:[%s], kwargs:[%s]' % (self.name, task_id, args, kwargs))


def route_task_nt(name, args, kwargs, options, task=None, **kw):
    exchange = options.get('exchange', 'nosetime')
    exchange_type = options.get('exchange_type', 'topic')
    routing_key = options.get('routing_key', name)
    return {
        'exchange': exchange,
        'exchange_type': exchange_type,
        'routing_key': routing_key
    }


celery = Celery(task_cls=BaseTask)
vv = copy.deepcopy(config['CELERY'])
vv['broker_url'] = 'amqp://root:root@127.0.0.1:5672/nosetime'
vv['task_queues'] = nosetime_queues
vv['task_routes'] = route_task_nt
vv['result_backend'] = None
vv['worker_enable_remote_control'] = False
# vv['include']=['nosetime.task.nosetime_task']
celery.config_from_object(vv)

# celery -A  nosetime.model.app worker --loglevel=info -P eventlet