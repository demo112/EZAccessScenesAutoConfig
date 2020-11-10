import json
import time
import hashlib
import http.client

# 解决python中无法处理null问题，将返回值中的null强制转化为空字符，''
from Data.Interface.__init__ import *
from Main.common.InterfaceCalling.sqlControl import SqlIO
from IPy import IP

global null
null = ''
sql = SqlIO()


class StrToAes:
    def __init__(self):
        pass


class HttpMethod(object):
    def __init__(self, username=USERINFO["username"], password=USERINFO["password"], port=10008):
        self.server_ip = '127.0.0.1'
        self.port = 10008
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
        url = "http://%s:%d%s" % (self.server_ip, self.port, TOKEN_URL)
        accessToken = ""
        # 读取数据库中密码密文
        try:
            TOKEN_PARAM["loginName"] = self.username
            TOKEN_PARAM["password"] = sql.readPassword()
            param = json.JSONEncoder().encode(TOKEN_PARAM)

            TOKEN_HEADERS["Content-Length"] = len(param)
            headers = TOKEN_HEADERS
            self.httpClient.request('POST', url, body=param, headers=headers)
        except IndexError:
            print("未注册用户，请注册")
        try:
            time.sleep(1)
            response = self.httpClient.getresponse().read()
            res = self.getStatusCode(response)
            if res == 200:
                resdata = self.getResData(response)
                accessToken = resdata["accessToken"]
        except Exception as e:
            print(e)
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

    def OPENAPI_POST(self,url, headers, param):
        response = b""
        try:
            self.httpClient.request("POST", url, body=param, headers=headers)
            time.sleep(1)
            response = self.httpClient.getresponse().read()
        except Exception as e:
            self.httpClient.close()
            self.httpClient = http.client.HTTPConnection(self.server_ip, 80, timeout=30)  # 重新建立链接
            # raise http.client.BadStatusLine('Badstatusline')
        return response


class DeviceInterfaceManagement(HttpMethod):
    # def deviceAdd(self, name, ip, port, deviceUsername, devicePassword):
    #     url = "http://%s:%d%s" % (self.server_ip, self.port, DEVICE_ADD_URL)
    #     DEVICE_ADD_PARAM["deviceName"] = name
    #     DEVICE_ADD_PARAM["deviceIP"] = ip
    #     DEVICE_ADD_PARAM["devicePort"] = port
    #     DEVICE_ADD_PARAM["deviceUsername"] = deviceUsername
    #     DEVICE_ADD_PARAM["devicePassword"] = devicePassword
    #     deviceData = DEVICE_ADD_PARAM
    #     body = json.JSONEncoder().encode(deviceData)
    #     response = b""
    #     DEVICE_ADD_HEADERS["Content-Length"] = len(body)
    #     DEVICE_ADD_HEADERS["Authorization"] = self.token
    #     headers = DEVICE_ADD_HEADERS
    #     try:
    #         self.httpClient.request("POST", url, body=body, headers=headers)
    #         time.sleep(1)
    #         response = self.httpClient.getresponse().read()
    #     except Exception as e:
    #         self.httpClient.close()
    #         self.httpClient = http.client.HTTPConnection(self.server_ip, 80, timeout=30)  # 重新建立链接
    #         # raise http.client.BadStatusLine('Badstatusline')
    #     return response
    def deviceAdd(self, name, ip, port, deviceUsername, devicePassword):
        url = "http://%s:%d%s" % (self.server_ip, self.port, DEVICE_ADD_URL)
        deviceData = DEVICE_ADD_PARAM
        headers = DEVICE_ADD_HEADERS

        deviceData["deviceName"] = name
        deviceData["deviceIP"] = ip
        deviceData["devicePort"] = port
        deviceData["deviceUsername"] = deviceUsername
        deviceData["devicePassword"] = devicePassword

        param = json.JSONEncoder().encode(deviceData)
        headers["Content-Length"] = len(param)
        headers["Authorization"] = self.token

        response = self.OPENAPI_POST(url, headers, param)
        return response

    def devicesAdd(self, DNS="206.10.0.0", index=24, Num=DEVICEUSERINFO["MaxDeviceNum"]):
        """

        :param DNS: 掩码
        :param index: 掩码长度
        :param Num: 设备数量
        :return:
        """
        IpList = IP("%s/%d" % (DNS, index))[2:(int(Num) + 2)]
        port = int(DEVICEUSERINFO["Port"])
        deviceUsername = DEVICEUSERINFO["deviceUsername"]
        devicePassword = DEVICEUSERINFO["devicePassword"]
        for ip in IpList:
            ip = str(ip)
            name = DEVICEUSERINFO["deviceName"]
            name += ip
            try:
                res = self.deviceAdd(name, ip, port, deviceUsername, devicePassword)
                status = self.getStatusCode(res)
                if status != 200:
                    raise "%s设备添加失败,错误码%s" % (name, status)
            except Exception as e:
                log = CreateLog().get_logger()
                log.warning(e)

    def deviceRemove(self, *args):
        """

        :param args: 输入设备列表序列指定删除设备，输入“all”删除所有
        :return:
        """
        # 对设备列表数据进行预处理
        """

        :param deleteThem:
        :return:
        """
        response = self.deviceList()
        # 筛选删除范围
        if ("all" or "All") not in args:
            deviceList = [self.getResData(response)["deviceList"][i - 1] for i in args]
        else:
            deviceList = self.getResData(response)["deviceList"]

        deviceIDList = []
        for device in deviceList:
            deviceId = device["deviceId"]
            deviceIDList.append(deviceId)

        url = "http://%s:%d%s" % (self.server_ip, self.port, DEVICE_DELETE_URL)
        # 获取需删除设备deviceId,构建请求内容，添加需删除设备
        deviceData = DEVICE_DELETE_PARAM
        headers = DEVICE_DELETE_HEADERS

        deviceData["deviceIdList"] = deviceIDList
        body = json.JSONEncoder().encode(deviceData)

        headers["Content-Length"] = len(body)
        headers["Authorization"] = self.token
        response = self.OPENAPI_POST(url, headers, body)
        return response

    def deviceChange(self):

        pass

    def deviceList(self):
        """

        :return:返回所有设备的信息
        	"code": 200,
            "message": "succeed",
            "data": {
                "total": 32,
                "deviceList": [
                    {
                        "deviceName": "示例设备206.10.0.2",
                        "deviceUserName": "admin",
                        "devicePassword": "Smbtest00",
                        "deviceIP": "206.10.0.2",
                        "devicePort": 80,
                        "deviceModel": null,
                        "deviceVersion": null,
                        "deviceId": "116417820157280256",
                        "status": 0,
                        "deviceType": 0
                    },]}}
        """
        url = "http://%s:%d%s" % (self.server_ip, self.port, DEVICE_SEARCH_URL)
        # 获取需删除设备deviceId,构建请求内容，添加需删除设备
        headers = DEVICE_DELETE_HEADERS
        deviceData = DEVICE_DELETE_PARAM
        body = json.JSONEncoder().encode(deviceData)

        headers["Content-Length"] = len(body)
        headers["Authorization"] = self.token
        response = self.OPENAPI_POST(url, headers, body)
        return response


class AccessInterfaceManagement(HttpMethod):
    def accessAdd(self):
        pass

    def accessRemove(self):
        pass

    def accessChange(self):
        pass

    def accessSearch(self):
        pass


if __name__ == '__main__':
    dm = DeviceInterfaceManagement()
    # res = dm.devicesAdd()
    res1 = dm.deviceRemove("all")
