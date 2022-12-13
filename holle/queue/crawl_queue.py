# -*- coding:utf-8 -*-
from kombu import Queue, Exchange, binding

zh_exchange = Exchange('nosetime', type='topic')

nosetime_queues = [
    Queue(
        'nosetime.web.search.list',
        [binding(exchange=zh_exchange, routing_key='nosetime.web.search.list')],
        queue_arguments={'x-queue-mode': 'lazy', 'x-max-priority': 10},
        max_priority=10
    ),
    Queue(
        'nosetime.web.product.info',
        [binding(exchange=zh_exchange, routing_key='nosetime.web.product.info')],
        queue_arguments={'x-queue-mode': 'lazy', 'x-max-priority': 10},
        max_priority=10
    ),
    Queue(
        'nosetime.web.comment.short',
        [binding(exchange=zh_exchange, routing_key='nosetime.web.comment.short')],
        queue_arguments={'x-queue-mode': 'lazy', 'x-max-priority': 10},
        max_priority=10
    ),
    Queue(
        'nosetime.web.comment.long',
        [binding(exchange=zh_exchange, routing_key='nosetime.web.comment.long')],
        queue_arguments={'x-queue-mode': 'lazy', 'x-max-priority': 10},
        max_priority=10
    ),
]
