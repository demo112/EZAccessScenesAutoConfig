#!/usr/bin/env python
# --encoding=utf-8
# Copyright (c) 2018-2022,Zhejiang Uniview Technology Co.,Ltd. All rights reserved.
# ===============================================================#
#           Function:   UCS http_method                          #
#           Author:     huxiaohua h03965                         #
#           Version:    2020-04-01 13:33                         #
# ===============================================================#


import json
import time
import hashlib
import http.client

# 解决python中无法处理null问题，将返回值中的null强制转化为空字符，''
global null
null = ''


class HttpMethod(object):
    def __init__(self, username="Heney", password='Admin123', port=80):
        self.server_ip = 'ucs.uniview.com'
        self.username = username
        self.password = password
        # 建立长链接，节约时间及网络带宽
        self.httpClient = http.client.HTTPConnection(self.server_ip, port, timeout=60)
        # 获取鉴权token值
        self.token = self.getAccessToken()

    def getAccessToken(self):
        """
        获取鉴权Token值
        """
        url = "http://%s/openapi/user/account/token/get" % self.server_ip
        accessToken = ""
        # 密码MD5加密
        password = self.password.encode('utf-8')
        m = hashlib.md5()
        m.update(password)
        password_md5 = m.hexdigest()
        param = {"loginName": self.username, "password": password_md5}
        param = json.JSONEncoder().encode(param)
        headers = {"Connection": "keep-alive",
                   "Content-Length": len(param),
                   "Cache-Control": "no-cache",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
                   "Content-Type": "application/json",
                   "charset": "UTF-8",
                   "Origin": "http://ucs.uniview.com",
                   "Referer": "http://ucs.uniview.com",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.9"
                   }
        try:
            self.httpClient.request('POST', url, body=param, headers=headers)
            time.sleep(1)
            response = self.httpClient.getresponse().read()
            res = self.getStatusCode(response)
            if res == 200:
                resdata = self.getResData(response)
                accessToken = resdata["accessToken"]
        except Exception as e:
            self.httpClient.close()
            self.httpClient = http.client.HTTPConnection(self.server_ip, 80, timeout=60)  # 重新建立链接
            # raise http.client.HTTPConnection.BadStatusLine('Badstatusline')
        return accessToken

    def md5(self, str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()

    def getStatusCode(self, res):
        """
        获取Response中的StatusCode
        """
        try:
            # python3和Python2在套接字返回值解码上有区别
            # decode():bytes变为str
            # encode():str变为decode
            res = res.decode()
            res = res.replace('false', 'False')
            res = res.replace('true', 'True')
            res_dict = eval(res)
            return res_dict["code"]
        except NameError as e:
            return 1

    def getResData(self, res):
        """
        获取Response中的Data
        """
        try:
            res = res.decode()
            res = res.replace('false', 'False')
            res = res.replace('true', 'True')
            res_dict = eval(res)
            return res_dict["data"]
        except Exception as e:
            return 1

    def UAPI_POST(self, url, param):
        body = json.JSONEncoder().encode(param)
        response = b""
        headers = {"Connection": "keep-alive",
                   "Content-Length": len(body),
                   "Cache-Control": "no-cache",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
                   "Authorization": self.token,
                   "Content-Type": "application/json",
                   "charset": "UTF-8", "Origin": "http://ucs.uniview.com", "Referer": "http://ucs.uniview.com",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.9"
                   }
        try:
            self.httpClient.request('POST', url, body=body, headers=headers)
            time.sleep(1)
            response = self.httpClient.getresponse().read()
        except Exception as e:
            self.httpClient.close()
            self.httpClient = http.client.HTTPConnection(self.server_ip, 80, timeout=30)  # 重新建立链接
            # raise http.client.BadStatusLine('Badstatusline')
        return response


if __name__ == '__main__':
    h = HttpMethod()
    url = "/openapi/user/organization/device/list"
    param = {"organizationId": "30933827639574529", "pageNo": 0, "pageSize": 20}
    res = h.UAPI_POST(url, param)
    ret = h.getStatusCode(res)
    resData = h.getResData(res)
    url1 = "/openapi/user/organization/sub/query"
    param = {"pageNo": 0, "pageSize": 100}
    res1 = h.UAPI_POST(url1, param)
    ret1 = h.getStatusCode(res1)
    resData1 = h.getResData(res1)

    # print(h)
    # print(url_)
    # print(param)
    print(res)
    print(ret)
    print(resData)
    # print(url1)
    # print(param)
    print(res1)
    print(ret1)
    print(resData1)
