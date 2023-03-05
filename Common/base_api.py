# coding=utf-8
import json
import requests
from Log import log

log = log.MyLog


def json_formatted_output(dic):
    """json字符串格式化输出"""

    j = json.dumps(dic, indent=4, ensure_ascii=False)
    return j


class MyRequest:
    """封装接口测试类"""

    def get(self, url, cookies, data):
        """
        get请求
        :param url: 请求地址
        :param cookies: 请求需携带的cookies
        :param data: 字典，请求参数
        :return: 元组，(响应的状态码,响应的数据)
        """

        res = ()
        try:
            log.info(f'请求地址：{url}')
            log.info('GET请求')
            log.info(f'请求参数：\n{json_formatted_output(data)}')
            restem = requests.get(url=url, cookies=cookies, params=data, verify=False)
            rescode = restem.status_code
            resdict = restem.json()
            reslog = json_formatted_output(resdict)
            log.info(f'响应的状态码：{rescode}')
            log.info(f'响应结果：\n{reslog}')
            res = rescode, resdict
        except Exception as e:
            log.error(f'访问GET接口({url})异常：{e}')
        return res

    def form_post(self, url, cookies, data):
        """
        表单提交的post请求
        :param url: 请求地址
        :param cookies: 请求需携带的cookies
        :param data: 字典，请求参数
        :return: 元组，(响应的状态码,响应的数据)
        """

        res = ()
        try:
            log.info(f'请求地址：{url}')
            log.info('POST请求')
            log.info(f'请求参数：\n{json_formatted_output(data)}')
            restem = requests.post(url=url, cookies=cookies, data=data, verify=False)
            rescode = restem.status_code
            resdict = restem.json()
            reslog = json_formatted_output(resdict)
            log.info(f'响应的状态码：{rescode}')
            log.info(f'响应结果：\n{reslog}')
            res = rescode, resdict
        except Exception as e:
            log.error(f'访问POST接口({url})异常：{e}')
        return res

    def json_post(self, url, headers, data):
        """
        json提交的post请求
        :param url: 请求地址
        :param cookies: 请求需携带的cookies
        :param data: 字典，请求参数
        :return: 元组，(响应的状态码,响应的数据)
        """

        res = ()
        try:
            log.info(f'请求地址：{url}')
            log.info('POST请求')
            log.info(f'请求参数：\n{json_formatted_output(data)}')
            restem = requests.post(url=url, headers=headers, json=data, verify=False)
            rescode = restem.status_code
            resdict = restem.json()
            reslog = json_formatted_output(resdict)
            log.info(f'响应的状态码：{rescode}')
            log.info(f'响应结果：{reslog}')
            res = rescode, resdict
        except Exception as e:
            log.error(f'访问POST接口({url})异常：{e}')
        return res
