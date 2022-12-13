# -*- coding:utf-8 -*-
import redis

pool_redis_cluster = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
redis_cluster = redis.StrictRedis(connection_pool=pool_redis_cluster)

