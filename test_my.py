#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:taoke
# import random
# for i in range(100):
#     res = random.randint(1,3)
#     print(res)
# r = u"\u5f53\u524d\u6d4f\u89c8\u5668\u4e0d\u652f\u6301Promise\uff0c\u8bf7\u5728windows\u5bf9\u8c61\u4e0a\u6302\u8f7dPromise\u5bf9\u8c61\u53ef\u53c2\u8003\uff08http://gitlab.alibaba-inc.com/mtb/lib-es6polyfill/tree/master\uff09\u4e2d\u7684\u89e3\u51b3\u65b9\u6848"
#
#
#
# print(r)
import datetime
# d = datetime.datetime.now()
# '%d年%d月%d日 %2d:%2d'%(d.date().year,d.date().month,comm.pub.date().day,comm.pub.time().hour,comm.pub.time().hour)
import redis
rcon = redis.StrictRedis(host='118.31.173.223', port=6379, db=10)
rcon.set('xes_api_status', 1)
rcon.set('hkes_api_status', 1)

        # if not rcon.set('hkes_api_status', 'False'):
        #     logger.error('redis writing error!!!')