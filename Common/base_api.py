# coding=utf-8
import requests
import json
from Log import log


class MyRequest:
    def __init__(self):
        self.log = log.MyLog()

    def get(self, url, cookies, data):
        try:
            self.log.info('请求地址：%s' % url)
            self.log.info('GET请求')
            self.log.info('请求参数：%s' % data)
            res_tem = requests.get(
                url=url,
                cookies=cookies,
                params=data,
                verify=False
            )
            self.log.info('返回的状态码：%s' % res_tem.status_code)
            response = res_tem.json()
            self.log.info('返回结果：%s' % response)
            return res_tem.status_code, response
        except Exception as e:
            self.log.error('访问GET接口(%s)异常：%s' % (url, e))
            return ()

    def post(self, url, cookies, data):
        try:
            self.log.info('请求地址：%s' % url)
            self.log.info('POST请求')
            self.log.info('请求参数：%s' % data)
            res_tem = requests.post(
                url=url,
                cookies=cookies,
                data=data,
                verify=False
            )
            self.log.info('返回的状态码：%s' % res_tem.status_code)
            response = res_tem.json()
            self.log.info('返回结果：%s' % response)
            return res_tem.status_code, response
        except Exception as e:
            self.log.error('访问POST接口(%s)异常：%s' % (url, e))
            return ()

    def json_post(self, url, cookies, data):
        try:
            self.log.info('请求地址：%s' % url)
            self.log.info('POST请求')
            self.log.info('请求参数：%s' % data)
            data = json.dumps(data)
            res_tem = requests.post(
                url=url,
                cookies=cookies,
                data=data,
                verify=False
            )
            self.log.info('返回的状态码：%s' % res_tem.status_code)
            response = res_tem.json()
            self.log.info('返回结果：%s' % response)
            return res_tem.status_code, response
        except Exception as e:
            self.log.error('访问接口(%s)异常：%s' % (url, e))
            return ()
