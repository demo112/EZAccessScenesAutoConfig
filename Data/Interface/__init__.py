from Main.__init__ import *

# 命名规则
# 主语+动词+宾语
# 以小驼峰法命名
xl = ET.parse(INERTFACEPATH + "\\" + "interFAce.xml")
root = xl.getroot()

COMMON_HEADERS = {
    "Content-Length": 0,
    "Accept": "application/json, text/plain, */*",
    "Cache-Control": "no-cache",
    "Origin": "file://",
    "Authorization": "",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "x-user-id": "116312915581075456",
    "Forwarded": 'proto=http;host="127.0.0.1:10008";for="127.0.0.1:52461"',
    "X-Forwarded-For": "127.0.0.1",
    "X-Forwarded-Proto": "http",
    "X-Forwarded-Port": "10008",
    "X-Forwarded-Host": "127.0.0.1:10008",
    "host": "127.0.0.1:10008",
}

# token请求头
TOKEN_URL = "/openapi/user/account/token/get"
TOKEN_HEADERS = {
    "Connection": "keep-alive",
    "Content-Length": 0,
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
    "loginName": "",
    "password": "",
}

PERSON_REMOVE_URL = "/openapi/person/delete"
PERSON_REMOVE_HEADERS = COMMON_HEADERS
PERSON_REMOVE_PARAM = {
    "idList": []
}

DEVICE_ADD_URL = "/openapi/device/ac/add"
DEVICE_ADD_HEADERS = COMMON_HEADERS
DEVICE_ADD_PARAM = {
    "deviceName": "",
    "deviceIP": "",
    "devicePort": "80",
    "deviceUserName": "admin",
    "devicePassword": ""
}

DEVICE_SEARCH_URL = "/openapi/device/ac/list"
DEVICE_SEARCH_HEADERS = COMMON_HEADERS
DEVICE_SEARCH_PARAM = {}

DEVICE_REMOVE_URL = "/openapi/device/ac/batch/delete"
DEVICE_REMOVE_HEADERS = COMMON_HEADERS
DEVICE_REMOVE_PARAM = {
    "deviceIdList": [],
}

ACCESS_ADD_URL = "/openapi/acs/permission/group/add"
ACCESS_ADD_HEADERS = COMMON_HEADERS
ACCESS_ADD_PARAM = {
    "permissionGroupName": "",
    "personIdList": [],
    "deviceIdList": []
}

ACCESS_SEARCH_URL = "/openapi/acs/permission/group/list"
ACCESS_SEARCH_HEADERS = COMMON_HEADERS
ACCESS_SEARCH_PARAM = {}

ACCESS_REMOVE_URL = "/openapi/acs/permission/group/delete"
ACCESS_REMOVE_HEADERS = COMMON_HEADERS
ACCESS_REMOVE_PARAM = {
    "permissionGroupId": ""
}

REGULATION_UPDATE_URL = "/atnd/attendance/rule/update?randomKey=1605748746845"
REGULATION_UPDATE_HEADERS = COMMON_HEADERS
REGULATION_UPDATE_PARAM = {
    "dayStartTime": "04:00",
    "timeStep": 0,
    "afterWorkMinute": 0,
    "beforeWorkEndMinute": 0,
    "unSignInTag": 0,
    "unSignOutTag": 0
}

LEAVE_ADD_URL = "/openapi/atnd/attendance/leave/add"
LEAVE_ADD_HEADERS = COMMON_HEADERS
LEAVE_ADD_PARAM = {
    "duration":900,
    "endTime":"2020/12/12 18:00",
    "personName":"jys0030000000001ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv",
    "primitive":"0",
    "remark":"",
    "startTime":"2020/12/12 09:00",
    "subtype":"0",
    "departName":".........1",
    "personCode":"jys0030000000001",
    "personId":1
}

if __name__ == '__main__':
    pass
