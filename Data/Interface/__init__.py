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
    "host": "127.0.0.1:10005",
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
    "host": "127.0.0.1:10005",
}
TOKEN_PARAM = {
    "loginName": "",
    "password": "",
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

DEVICE_DELETE_URL = "/openapi/device/ac/batch/delete"
DEVICE_DELETE_HEADERS = COMMON_HEADERS
DEVICE_DELETE_PARAM = {
    "deviceIdList":[],
}

ACCESS_ADD_URL = "/openapi/acs/permission/group/add"
ACCESS_ADD_HEADERS = COMMON_HEADERS
ACCESS_ADD_PARAM = {
    "permissionGroupName":"",
    "personIdList":[],
    "deviceIdList":[]
}

if __name__ == '__main__':
    pass
