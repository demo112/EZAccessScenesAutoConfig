# 主程序，实现主业务流程
import os
from xml.etree import ElementTree  as  ET
# 路径配置
HOMEPATH = os.path.abspath(os.path.join(os.path.abspath(__file__), "..\\.."))
# 场景配置路径
CONFIGPATH = HOMEPATH + "\\Scenes"
# 文件保存路径
PERSONINFO = HOMEPATH + "\\Data\\Person\\Info"
PHOTOCOPYPATH = HOMEPATH + "\\Data\\Person\\Photo\\clonfile"
MOTHERFILEPATH = HOMEPATH + "\\Data\\Person\\Photo\\motherfile"
# 导出路径
EXPORTPATH = HOMEPATH + "\\Data\\Person\\ExportFile"
# 接口路径
INERTFACEPATH = HOMEPATH + "\\Data\\InterFAce"

# 配置文件读取
main_xl = ET.parse(CONFIGPATH + "\\" + "config.xml")
main_root = main_xl.getroot()

# 用户信息配置
USERINFO = {
    "username": main_root.find("UserInfo").find("username").text,
    "password": main_root.find("UserInfo").find("password").text,
}

# 设备信息配置
DEVICEUSERINFO = {
    "deviceName": main_root.find("DeviceInfo").find("deviceName").text,
    "VLAN": main_root.find("DeviceInfo").find("VLAN").text,
    "MaxDeviceNum": main_root.find("DeviceInfo").find("MaxDeviceNum").text,
    "Port": main_root.find("DeviceInfo").find("Port").text,
    "deviceUsername": main_root.find("DeviceInfo").find("deviceUsername").text,
    "devicePassword": main_root.find("DeviceInfo").find("devicePassword").text,
}

#数据库配置
# 登录账号密码
SQL = {
    "host": "127.0.0.1",
    "port": 10007,
    "username": "root",
    "password": "Smbtest0",
}

# 尝试次数限制
BreakOutTimes = 5
BreakOutTime = 30

PERSONDEPARTMENTLIST = [
    # todo 暂时只支持初始化创建，需增加自适应部门AutomationID功能
    "4097",
    "4098",
    "4099",
    "4100",
    "4101",
    "4102",
    "4103",
    "4104",
    "4105",
    "4106",
]

if __name__ == '__main__':

    # print(configRoot)
    print(USERINFO)