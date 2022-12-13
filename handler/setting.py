import os
import sys
import logging.config

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

queues = []


def route_task(name, args, kwargs, options, task=None, **kw):
    exchange = options.get('exchange', 'default')
    exchange_type = options.get('exchange_type', 'default')
    routing_key = options.get('routing_key', name)
    return {
        'exchange': exchange,
        'exchange_type': exchange_type,
        'routing_key': routing_key
    }


class ProductConfig(object):
    PRO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
    CACHE_REDIS_URL = 'file:///var/duck/result_backend'
    REDIS_MONITOR_PROJECTS = 'monitor:projects:'
    PROXIES = {}

    RABBITMQ_URL = 'amqp://root:root@127.0.0.1:5672/'

    CELERY = {
        'broker_url': RABBITMQ_URL,

        # 'broker_transport_options': {},
        # 'result_backend': CACHE_REDIS_URL,
        # 'task_ignore_result': True,
        # 'broker_pool_limit': None,
        # 默认任务配置
        'task_default_queue': 'nosetime:default',
        'task_default_exchange': 'nosetime',
        'task_default_exchange_type': 'topic',
        # 'task_default_delivery_mode': 'transient',  # 不设置消息持久化
        'task_queue_max_priority': 10,  # 设置所有队列优先级默认值
        'task_default_priority': 1,  # 指定所有任务默认的优先级
        'task_default_routing_key': 'default',
        'task_default_delivery_mode': 'persistent',  # 消息持久化
        # 'task_track_started': True,
        'timezone': "Asia/Shanghai",
        # 'result_compression': 'gzip',
        # 'task_compression': 'gzip',
        'result_expires': 3600,
        'task_ignore_result': True,
        'task_store_errors_even_if_ignored': True,
        "broker_connection_max_retries": None,
        "worker_max_tasks_per_child": 40,
        # 发送端路由
        'task_queues': queues,
        'task_routes': (route_task,),
        # 日志
        'worker_task_log_format': "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s",
        'worker_log_format': "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s",
    }

    LOGGING_CONFIG = {
        "version": 1,
        "formatters": {
            'f': {
                'format':
                    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
        "handlers": {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'f',
            },
            'error_file': {
                'class': 'logging.FileHandler',
                'formatter': 'f',
                'filename': os.path.join(PRO_DIR, 'logs/http_err.log'),
            },
            'file_http_api': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(PRO_DIR, 'logs/http_api_access.log'),
                'encoding': 'utf-8',
                'formatter': 'f',
            },
            'file_task': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(PRO_DIR, 'logs/task.log'),
                'encoding': 'utf-8',
                'formatter': 'f',
            }
        },
        "root": {
            'handlers': ['console'],
            'level': logging.DEBUG,
        },
        "loggers": {
            'gunicorn.error': {
                'level': 'INFO',
                'handlers': ['error_file'],
                'propagate': True,
            },
            'gunicorn.access': {
                'level': 'INFO',
                'handlers': ['file_http_api'],
                'propagate': False,
            },
            'http_err': {
                'propagate': False,
                'level': 'DEBUG',
                'handlers': ['console', 'error_file']
            },
            'task': {
                'propagate': False,
                'level': 'WARNING',
                'handlers': ['console', 'file_task']
            }
        }
    }


def obj2dict(obj):
    return {key: getattr(obj, key) for key in dir(obj) if key.isupper()}


config = obj2dict(ProductConfig)
logging.config.dictConfig(config['LOGGING_CONFIG'])
