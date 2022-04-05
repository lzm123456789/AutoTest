# coding=utf-8
import json
import requests
from Log import log


def json_formatted_output(dic):
    """json字符串格式化输出"""

    j = json.dumps(dic, indent=4, ensure_ascii=False)
    return j


class MyRequest:
    """封装接口测试类"""

    def __init__(self):
        self.log = log.MyLog

    def get(self, url, cookies, data):
        """
        get请求
        :param url: 请求地址
        :param cookies: 请求需携带的cookies
        :param data: 请求参数
        :return: 响应的状态码和响应的数据
        """

        try:
            self.log.info('请求地址：%s' % url)
            self.log.info('GET请求')
            self.log.info('请求参数：\n%s' % json_formatted_output(data))
            res_tem = requests.get(url=url,
                                   cookies=cookies,
                                   params=data,
                                   verify=False)
            self.log.info('响应的状态码：%s' % res_tem.status_code)
            response = res_tem.json()
            self.log.info('响应结果：\n%s' % json_formatted_output(response))
            return res_tem.status_code, response
        except Exception as e:
            self.log.error('访问GET接口(%s)异常：%s' % (url, e))
            return ()

    def form_post(self, url, cookies, data):
        """
        表单提交的post请求
        :param url: 请求地址
        :param cookies: 请求需携带的cookies
        :param data: 请求参数
        :return: 响应的状态码和响应的数据
        """

        try:
            self.log.info('请求地址：%s' % url)
            self.log.info('POST请求')
            self.log.info('请求参数：\n%s' % json_formatted_output(data))
            res_tem = requests.post(url=url,
                                    cookies=cookies,
                                    data=data,
                                    verify=False)
            self.log.info('响应的状态码：%s' % res_tem.status_code)
            response = res_tem.json()
            self.log.info('响应结果：\n%s' % json_formatted_output(response))
            return res_tem.status_code, response
        except Exception as e:
            self.log.error('访问POST接口(%s)异常：%s' % (url, e))
            return ()

    def json_post(self, url, headers, data):
        """
        json提交的post请求
        :param url: 请求地址
        :param cookies: 请求需携带的cookies
        :param data: 请求参数
        :return: 响应的状态码和响应的数据
        """

        try:
            self.log.info('请求地址：%s' % url)
            self.log.info('POST请求')
            self.log.info('请求参数：\n%s' % json_formatted_output(data))
            res_tem = requests.post(url=url,
                                    headers=headers,
                                    json=data,
                                    verify=False)
            self.log.info('响应的状态码：%s' % res_tem.status_code)
            response = res_tem.json()
            self.log.info('响应结果：%s' % json_formatted_output(response))
            return res_tem.status_code, response
        except Exception as e:
            self.log.error('访问POST接口(%s)异常：%s' % (url, e))
            return ()
