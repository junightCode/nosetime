# -*- coding:utf-8 -*-
import datetime
import re
import time

class Kit:
    @classmethod    # 秒前移
    def preseconds(cls, seconds):
        time = (datetime.datetime.now() - datetime.timedelta(seconds=seconds)).strftime("%Y-%m-%d %H:%M:%S")
        return time

    @classmethod  # 分钟前移
    def preminute(cls, minute):
        time = (datetime.datetime.now() - datetime.timedelta(minutes=minute)).strftime("%Y-%m-%d %H:%M:%S")
        return time

    @classmethod  # 小时前移
    def prehour(cls, hour):
        time = (datetime.datetime.now() - datetime.timedelta(hours=hour)).strftime("%Y-%m-%d %H:%M:%S")
        return time

    @classmethod    # 天前移
    def preday(cls, day):
        time = (datetime.datetime.now() - datetime.timedelta(days=day)).strftime("%Y-%m-%d %H:%M:%S")
        return time

    @classmethod  # 标准格式转时间戳
    def ex_stamp(cls, t_standard):
        tmp = time.strptime(t_standard, "%Y-%m-%d %H:%M:%S")
        t_stamp = int(time.mktime(tmp))
        return t_stamp

    @classmethod  # 时间戳转标准格式
    def ex_standard(cls, t_stamp):
        t_stamp = int(t_stamp)
        tmp = time.localtime(t_stamp)
        t_standard = time.strftime('%Y-%m-%d %H:%M:%S', tmp)
        return t_standard

    @classmethod  # 当前时间戳
    def timestamp_now(cls):
        return int(time.time())

    @classmethod  # 当前标准格式
    def timestandard_now(cls):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
