import hashlib
import json

import requests
import urllib3

null = ""
# 用户名密码，密码要求是md5加密后密文
USERNAME = "admin"
USEPASSWORD = "Dbckl4A3AsqW/e1zslLUSg=="

TOKEN_URL = "/openapi/user/account/token/get"
TOKEN_HEADERS = {
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Cache-Control": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "file://",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Forwarded": 'proto=http;host="127.0.0.1:10008";for="127.0.0.1:50348"',
    "X-Forwarded-For": "127.0.0.1",
    "X-Forwarded-Proto": "http",
    "X-Forwarded-Port": "10008",
    "X-Forwarded-Host": "127.0.0.1:10008",
    "host": "127.0.0.1:10008",
}
TOKEN_PARAM = {
    "loginName": "admin",
    "password": "Dbckl4A3AsqW/e1zslLUSg==",
}


class HttpsMethod(object):
    def __init__(self, username=USERNAME, password=USEPASSWORD, port=10008):
        self.server_ip = '127.0.0.1'
        self.port = 10008
        self.username = username
        self.password = password
        # 建立长链接，节约时间及网络带宽
        # self.httpClient = http.client.HTTPConnection(self.server_ip, port, timeout=60)
        # 获取鉴权token值
        self.token = self.getAccessToken()

    def getAccessToken(self):
        """
        获取鉴权Token值
        """
        url = "https://%s:%d%s" % (self.server_ip, self.port, TOKEN_URL)
        accessToken = ""
        # 读取数据库中密码密文
        try:
            TOKEN_PARAM["loginName"] = self.username
            TOKEN_PARAM["password"] = self.password
            param = json.JSONEncoder().encode(TOKEN_PARAM)

            TOKEN_HEADERS["Content-Length"] = str(len(param))
            headers = TOKEN_HEADERS
            urllib3.disable_warnings()
            response = self.getResponse(url, data=param, headers=headers)
            res = self.getStatusCode(response)
            if res == 200:
                resdata = self.getResData(response)
                accessToken = resdata["accessToken"]
        except Exception as e:
            print("gettoken:", e)
            # self.httpClient.close()
            # self.httpClient = http.client.HTTPConnection(self.server_ip, 80, timeout=60)  # 重新建立链接
            # raise http.client.HTTPConnection.BadStatusLine('Badstatusline')
        return accessToken

    def md5(self, str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()

    def getResponse(self, url, headers, data):
        """
        直接获取响应体对象
        :param url:
        :param data:
        :param headers:
        :return:响应的内容
        """
        response = requests.post(url, headers=headers, data=data, verify=False).content
        print(response)
        return response

    def getStatusCode(self, res):
        """
        获取Response中的StatusCode
        """
        try:
            # python3和Python2在套接字返回值解码上有区别
            # decode():bytes变为str
            # encode():str变为decode
            res = res.decode("utf-8")
            res = res.replace('false', 'False')
            res = res.replace('true', 'True')
            res_dic = eval(res)
            return res_dic["code"]
        except NameError as e:
            print("getStatusCode:", e)
            return 1

    def getResData(self, res):
        """
        获取Response中的Data
        """
        try:
            res = res.decode("utf-8")
            res = res.replace('false', 'False')
            res = res.replace('true', 'True')
            res_dic = eval(res)
            data = res_dic["data"]
            return data
        except Exception as e:
            print("getResData:", e)
            return 1

    def UAPI_POST(self, url, param):
        body = json.JSONEncoder().encode(param)
        response = b""
        headers = {"Connection": "keep-alive",
                   "Content-Length": str(len(body)),
                   "Cache-Control": "no-cache",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
                   "Authorization": self.token,
                   "Content-Type": "application/json",
                   "charset": "UTF-8", "Origin": "http://ucs.uniview.com", "Referer": "http://ucs.uniview.com",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.9"
                   }
        try:
            response = self.getResponse(url, headers, body)
        except Exception as e:
            pass
            # self.httpClient.close()
            # self.httpClient = http.client.HTTPConnection(self.server_ip, 80, timeout=30)  # 重新建立链接
            # raise http.client.BadStatusLine('Badstatusline')
        return response

    def OPENAPI_POST(self, url, headers, param):
        response = b""
        try:
            response = self.getResponse(url, headers, param)
        except Exception as e:
            pass
            # self.httpClient.close()
            # self.httpClient = http.client.HTTPConnection(self.server_ip, 80, timeout=30)  # 重新建立链接
            # raise http.client.BadStatusLine('Badstatusline')
        return response

if __name__ == '__main__':
    h = HttpsMethod()
    t = h.getAccessToken()
    print(t)