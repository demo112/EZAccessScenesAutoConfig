import json
import hashlib

# 解决python中无法处理null问题，将返回值中的null强制转化为空字符，''
import random
import time

import requests
import urllib3

from Data.Interface.__init__ import *
from Main.common.InterfaceCalling.sqlControl import SqlIO
from IPy import IP
from Main.OtherTools.Log.CreateLog import CreateLog

global null
sql = SqlIO()
log = CreateLog().get_logger()


class StrToAes:
    def __init__(self):
        pass


class HttpsMethod(object):
    def __init__(self, username=USERINFO["username"], password=USERINFO["password"], port=10008):
        self.server_ip = '127.0.0.1'
        self.port = port
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
            TOKEN_PARAM["password"] = sql.readPassword()
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


class PersonInterfaceManagement(HttpsMethod):
    def personRemove(self, idList=None):
        """
        默认删除所有人，或指定删除某一部分人
        :param idList: 待删除的人员界面序列列表
        :return:
        """
        # 预处信息
        if (idList == None) or ("all" == idList):
            sq = SqlIO()
            _allPerson = sq.search("person_id", "ucs", "tbl_person")
            allPerson = [int(per[0]) for per in _allPerson]
            allPerson = allPerson
        elif idList:
            allPerson = idList
        else:
            allPerson = []
            log.info('人员列表有误，未删除人员，请核验后重试')
        # allPerson = idList
        # 基于接口构造请求
        url = "https://%s:%d%s" % (self.server_ip, self.port, PERSON_REMOVE_URL)
        headers = PERSON_REMOVE_HEADERS
        accessData = PERSON_REMOVE_PARAM
        # 调整请求体内容
        accessData["idList"] = allPerson
        body = json.JSONEncoder().encode(accessData)
        # 调整请求头内容
        headers["Content-Length"] = str(len(body))
        headers["Authorization"] = self.token
        # 发起请求并捕捉响应报文
        response = self.OPENAPI_POST(url, headers, body)

        return response


class DeviceInterfaceManagement(HttpsMethod):

    def deviceAdd(self, name, ip, port, deviceUsername, devicePassword):
        url = "https://%s:%d%s" % (self.server_ip, self.port, DEVICE_ADD_URL)
        deviceData = DEVICE_ADD_PARAM
        headers = DEVICE_ADD_HEADERS

        deviceData["deviceName"] = name
        deviceData["deviceIP"] = ip
        deviceData["devicePort"] = port
        deviceData["deviceUsername"] = deviceUsername
        deviceData["devicePassword"] = devicePassword

        param = json.JSONEncoder().encode(deviceData)
        headers["Content-Length"] = str(len(param))
        headers["Authorization"] = self.token

        response = self.OPENAPI_POST(url, headers, param)
        return response

    def devices_add(self, DNS, index, Num):
        """

        :param DNS: 掩码
        :param index: 掩码长度
        :param Num: 设备数量
        :return:
        """
        IpList = IP("%s/%d" % (DNS, int(index)))[2:(int(Num) + 2)]
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

        response = self.deviceList()
        # 筛选删除范围
        if args:
            device_list = [self.getResData(response)["deviceList"][i - 1] for i in args]
        else:
            device_list = self.getResData(response)["deviceList"]

        device_id_list = []
        for device in device_list:
            device_id = device["deviceId"]
            device_id_list.append(device_id)

        url = "https://%s:%d%s" % (self.server_ip, self.port, DEVICE_REMOVE_URL)
        # 获取需删除设备deviceId,构建请求内容，添加需删除设备
        deviceData = DEVICE_REMOVE_PARAM
        headers = DEVICE_REMOVE_HEADERS

        deviceData["deviceIdList"] = device_id_list
        body = json.JSONEncoder().encode(deviceData)

        headers["Content-Length"] = str(len(body))
        headers["Authorization"] = self.token
        response = self.OPENAPI_POST(url, headers, body)
        return response

    def deviceUpdate(self):

        pass

    def deviceList(self):
        """

        :return:返回所有设备的信息
        	"code": 200,
            "message": "succeed",
            "data": {
                "total": 32,
                "device_list": [
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
        url = "https://%s:%d%s" % (self.server_ip, self.port, DEVICE_SEARCH_URL)
        # 获取需删除设备deviceId,构建请求内容，添加需删除设备
        headers = DEVICE_REMOVE_HEADERS
        deviceData = DEVICE_REMOVE_PARAM
        body = json.JSONEncoder().encode(deviceData)

        headers["Content-Length"] = str(len(body))
        headers["Authorization"] = self.token
        response = self.OPENAPI_POST(url, headers, body)
        return response


class VisitorInterfaceManagement(HttpsMethod):
    def visitor_add(self, name, sex, visitor_number, id_aes, ic, telephone_aes, visitor_dp, remark,
                    employee_id, employee_dp, device_list,
                    startTime, endTime):
        url = "https://%s:%d%s" % (self.server_ip, self.port, VISITOR_ADD_URL)
        headers = DEVICE_ADD_HEADERS
        visitor_data = VISITOR_ADD_PARAM
        visitor_data["visitorName"] = name
        visitor_data["visitorNumber"] = visitor_number
        visitor_data["visitorSex"] = sex or random.randrange(0, 2, 1)
        visitor_data["visitorDepartment"] = visitor_dp
        visitor_data["receptionistId"] = employee_id
        visitor_data["receptionistDepartment"] = employee_dp
        visitor_data["telephone"] = telephone_aes
        visitor_data["identificationList"] = [{"type": 0, "number": id_aes}, {"type": 1, "number": ic}]
        visitor_data["remarks"] = remark
        visitor_data["imageList"] = []

        visitor_data["deviceSerialList"] = device_list
        visitor_data["startTime"] = startTime
        visitor_data["endTime"] = endTime

        param = json.JSONEncoder().encode(visitor_data)
        headers["Content-Length"] = str(len(param))
        headers["Authorization"] = self.token
        response = self.OPENAPI_POST(url, headers, param)
        print(param)
        print(response)
        return response
        pass

    def visitor_batch_add(self):
        tbl_person = sql.search("*", "ucs", "tbl_person")
        for person in tbl_person[1:10000]:
            print(person)
            visitor_number = person[0] + 5000
            name = "visitor" + person[2][3:60]
            sex = person[3]
            id_aes = person[5]
            ic = person[10]
            telephone_aes = person[7]
            visitor_dp = "visitor" + str(person[8])
            remark = person[12]
            employee_id = person[0]
            employee_dp = sql.readInfo("dept_name", "dept_id", int(person[8]), "ucs", "tbl_dept")[0][0]

            device_list = [str(random.choice(sql.search("dev_id", "ucs", "tbl_ac_device"))[0])]
            start_time = int(time.time())
            end_time = start_time + 10800
            print("=========================================================================")
            # print("name:", name)
            # print("sex:", sex)
            # print("visitor_number:", visitor_number)
            # print("id_aes:", id_aes)
            # print("ic:", ic)
            # print("telephone_aes:", telephone_aes)
            # print("visitor_dp:", visitor_dp)
            # print("remark:", remark)
            # print("employee_id:", employee_id)
            # print("employee_dp:", employee_dp)
            # print("device_list:", device_list)
            self.visitor_add(name, sex, visitor_number, id_aes, ic, telephone_aes, visitor_dp, remark,
                             employee_id, employee_dp, device_list,
                             start_time, end_time)

    def visitor_change(self):
        pass

    def visitor_delete(self):
        pass


class AccessInterfaceManagement(HttpsMethod):
    def access_add(self, name, person_list, device_list):
        """
        创建门禁收授权
        :param name: 授权组名称
        :param person_list: 授权人员的序列编号列表
        :param device_list: 授权设备的序列编号列表
        :return:
        """

        def index_to_id(tbl_type, index_list):
            """
            根据需求获取指定人员、设备的唯一id
            :param index_list:
            :return:
            """
            sql = SqlIO()
            maxNum = int(DEVICEUSERINFO["MaxDeviceNum"])
            # 判断所需列表
            if "device" == tbl_type:
                # index_list = index_list[0:maxNum]
                idList = sql.search("dev_id", "ucs", "tbl_ac_device")
            elif "person" == tbl_type:
                idList = sql.search("person_id", "ucs", "tbl_person")
            else:
                idList = []
            _needList = []
            for i in index_list:
                _needList.append(int(idList[i - 1][0]))
            return _needList

        url = "https://%s:%d%s" % (self.server_ip, self.port, ACCESS_ADD_URL)
        headers = ACCESS_ADD_HEADERS
        accessData = ACCESS_ADD_PARAM
        accessData["permissionGroupName"] = name
        print(accessData)
        accessData["personIdList"] = index_to_id("person", person_list)
        accessData["deviceIdList"] = index_to_id("device", device_list)
        body = json.JSONEncoder().encode(accessData)

        headers["Content-Length"] = str(len(body))
        headers["Authorization"] = self.token
        response = self.OPENAPI_POST(url, headers, body)
        return response

    def access_remove(self, name):
        """

        :param name: 需删除的权限组名称
        :return:
        """
        # 预处理指定授权组信息
        sq = SqlIO()
        group_id = sq.readInfo("fl_permission_id", "fl_permission_name", name, "ucs", "tbl_acs_permission")
        url = "https://%s:%d%s" % (self.server_ip, self.port, ACCESS_REMOVE_URL)
        headers = ACCESS_REMOVE_HEADERS
        accessData = ACCESS_REMOVE_PARAM
        accessData["permissionGroupId"] = group_id[0][0]
        body = json.JSONEncoder().encode(accessData)

        headers["Content-Length"] = str(len(body))
        headers["Authorization"] = self.token
        response = self.OPENAPI_POST(url, headers, body)
        return response

    def accessUpdate(self):
        pass

    def accessSearch(self):
        sq = SqlIO()
        groupId = sq.search("fl_permission_name", "ucs", "tbl_acs_permission")
        url = "https://%s:%d%s" % (self.server_ip, self.port, ACCESS_SEARCH_URL)
        headers = ACCESS_SEARCH_HEADERS
        accessData = ACCESS_SEARCH_PARAM
        body = json.JSONEncoder().encode(accessData)

        headers["Content-Length"] = str(len(body))
        headers["Authorization"] = self.token
        response = self.OPENAPI_POST(url, headers, body)
        return response


class AttendanceInterfaceManagement(HttpsMethod):
    def attendanceAdd(self):
        pass

    def attendanceRemove(self):
        pass

    def attendanceUpdate(self):
        pass

    def attendanceSearch(self):
        pass


class RegulationInterFaceMgt(AttendanceInterfaceManagement):
    def regulation_update(self):
        pass


class StaffScheduleInterFaceMgt(AttendanceInterfaceManagement):
    pass


class AttendanceMgtInterFaceMgt(AttendanceInterfaceManagement):
    def leave_add(self, person_id, start_time, end_time):
        # """
        #
        # :param args: 输入设备列表序列指定删除设备，输入“all”删除所有
        # :return:
        # """
        # # 对设备列表数据进行预处理
        #
        #
        # # 筛选删除范围
        # person_info = {}
        #
        # url = "https://%s:%d%s" % (self.server_ip, self.port, LEAVE_ADD_URL)
        # # 获取需删除设备deviceId,构建请求内容，添加需删除设备
        # leave_data = person_info
        # leave_data = LEAVE_ADD_PARAM
        # headers = DEVICE_REMOVE_HEADERS
        #
        # deviceData["deviceIdList"] = device_id_list
        # body = json.JSONEncoder().encode(deviceData)
        #
        # headers["Content-Length"] = str(len(body))
        # headers["Authorization"] = self.token
        # response = self.OPENAPI_POST(url, headers, body)
        # return response
        pass

    def batch_leave_add(self, person_list):
        pass


class AttendanceStaticInterFaceMgt(AttendanceInterfaceManagement):
    pass


class PassThuInterfaceManagement(HttpsMethod):
    pass


class SystemConfigurationManagement(HttpsMethod):
    pass


if __name__ == '__main__':
    # dim = DeviceInterfaceManagement()
    # list = dim.deviceList()
    # print(list)
    # aim = AccessInterfaceManagement()
    # a_l = aim.accessSearch()
    # print(a_l)
    h = HttpsMethod()
    t = h.getAccessToken()
    print(t)

    pass
