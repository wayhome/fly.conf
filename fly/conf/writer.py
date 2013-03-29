#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
from redis import Redis


class ConfWriter(object):
    """a redis config reader"""
    def __init__(self, url, prefix=None):
        self.client = Redis.from_url(url)
        self.prefix = prefix

    def get_key(self, key):
        if self.prefix:
            return "{0}:{1}".format(self.prefix, key)
        else:
            return key

    def add(self, key, value):
        key = self.get_key(key)
        if not isinstance(value, basestring):
            value = json.dumps(value)
        self.client.zadd(key, value, time.time())

    def remove(self, key, value):
        key = self.get_key(key)
        self.client.zrem(key, value)

    def delete(self, key):
        key = self.get_key(key)
        self.client.delete(key)
