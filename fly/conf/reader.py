#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import json
from redis import Redis

CACHE_TIME = 120  # 2分钟后自动重新读取配置


class ConfReader(object):
    """a redis config reader"""
    _results = {}

    def __init__(self, url, prefix=None, timeout=CACHE_TIME):
        self.client = Redis.from_url(url)
        self.prefix = prefix
        self.timeout = timeout

    def get_key(self, key):
        if self.prefix:
            return "{0}:{1}".format(self.prefix, key)
        else:
            return key

    def get(self, key):
        key = self.get_key(key)
        if key in ConfReader._results:
            result = ConfReader._results[key]
            if time.time() - result['updated'] < self.timeout:
                return result['value']
        value = []
        for v in self.client.zrange(key, 0, -1):
            try:
                v = json.loads(v)
            except Exception:
                pass
            value.append(v)
        ConfReader._results[key] = {'value': value, 'updated': time.time()}
        return value

    def get_full(self, key):
        key = self.get_key(key)
        results = []
        for k, v in self.client.zrange(key, 0, -1, withscores=True):
            try:
                k = json.loads(k)
            except:
                pass
            results.append((k, v))
        return results

    def get_all_keys(self):
        if self.prefix:
            key = "{0}:*".format(self.prefix)
        else:
            key = "*"
        return self.client.keys(key)
