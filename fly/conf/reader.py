#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from redis import Redis

CACHE_TIME = 60

class ConfReader(object):
    """a redis config reader"""
    def __init__(self, url, prefix=None):
        self.client = Redis.from_url(url)
        self.prefix = prefix

    def get_key(self, key):
        if self.prefix:
            return "{0}:{1}".format(self.prefix, key)
        else:
            return key

    def get(self, key):
        key = self.get_key(key)
        return self.client.zrange(key, 0, -1)

    def get_full(self, key):
        key = self.get_key(key)
        return dict(self.client.zrange(key, 0, -1, withscores=True))

    def add(self, key, value):
        key = self.get_key(key)
        self.client.zadd(key, value, time.time())

    def remove(self, key, value):
        key = self.get_key(key)
        self.client.zrem(key, value)
