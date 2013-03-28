#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from redis import Redis

CACHE_TIME = 120  # 2分钟后自动重新读取配置


class ConfReader(object):
    """a redis config reader"""
    _results = {}

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
        if key in ConfReader._results:
            result = ConfReader._results[key]
            if time.time() - result['updated'] < CACHE_TIME:
                return result['value']
        value = self.client.zrange(key, 0, -1)
        ConfReader._results[key] = {'value': value, 'updated': time.time()}
        return value

    def get_full(self, key):
        key = self.get_key(key)
        return dict(self.client.zrange(key, 0, -1, withscores=True))

    def get_all_keys(self):
        if self.prefix:
            key = "{0}:*".format(self.prefix)
        else:
            key = "*"
        return self.client.keys(key)
