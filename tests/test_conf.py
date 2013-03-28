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
        server_time = self.reader.get_full('cache_servers')['redis://127.0.0.1/6389/0']
        assert int(server_time) + 100 > time.time()
