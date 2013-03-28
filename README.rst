flyconf
================
``flyconf`` 是一套用redis来做集中化配置管理的方案.

.. image:: https://travis-ci.org/youngking/fly.conf.png?branch=master
   :alt: Build Status


读取配置
----------------
提供给客户调用方使用, 配置项会在client缓存两分钟以减少网络请求，两分钟后自动更新

>>> from fly.conf import ConfReader
>>> reader = ConfReader('redis://127.0.0.1:6379/0', 'main')
>>> reader.get('cache_servers')
... ['redis://127.0.0.1/6389/0', 'redis://127.0.0.1/6389/2']

>>> reader.get_full('cache_servers')
... {'redis://127.0.0.1/6389/0': 1364456822, # 时间戳
     'redis://127.0.0.1/6389/2': 1364456822, #
    }


更新配置
----------------
提供给管理方使用

>>> from fly.conf import ConfWriter
>>> writer = ConfWriter('redis://127.0.0.1:6379/0', 'main')
>>> writer.delete('cache_servers')
>>> writer.add('cache_servers', 'redis://127.0.0.1/6389/0')
>>> writer.add('cache_servers', 'redis://127.0.0.1/6389/2')
>>> writer.remote('cache_servers', 'redis://127.0.0.1/6389/2')



dashboard
--------------
管理和更新配置
