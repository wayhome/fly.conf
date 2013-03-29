#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time


class TestConf(unittest.TestCase):

    def setUp(self):
        from fly.conf import ConfReader, ConfWriter
        self.reader = ConfReader('redis://127.0.0.1:6379/0', 'main')
        self.writer = ConfWriter('redis://127.0.0.1:6379/0', 'main')

    def test_conf(self):
        self.writer.delete('cache_servers')
        self.writer.add('cache_servers', 'redis://127.0.0.1/6389/0')
        self.writer.add('cache_servers', 'redis://127.0.0.1/6389/2')
        assert len(self.reader.get('cache_servers')) == 2
        assert 'redis://127.0.0.1/6389/0' in self.reader.get('cache_servers')
        server_time = self.reader.get_full('cache_servers')[0][1]
        assert int(server_time) + 100 > time.time()

    def test_json_conf(self):
        self.writer.delete('rpc_servers')
        self.writer.add('rpc_servers', {'name': 'live', 'host': 'localhost', 'port': 3399})
        assert self.reader.get('rpc_servers')[0]['port'] == 3399
