# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from .utils.api import get_ip_port

class ProxyMiddleware(object):

    def process_request(self, request, spider):
        # 获取一个优质代理
        proxy = get_ip_port('http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=a31f8cd494e343d69b51b303859ac446&orderno=YZ2018112517118ojIuo&returnType=2&count=1')
        # 设置代理
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass