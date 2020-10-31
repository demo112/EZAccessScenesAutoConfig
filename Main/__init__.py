# 主程序，实现主业务流程
from Main.OtherTools.Log.CreateLog import *

log = CreateLog().get_logger()

HOMEPATH = os.path.abspath(os.path.join(os.path.abspath(__file__), "..\\.."))

CONFIGPATH = HOMEPATH + "\\Scenes"
PERSONINFO = HOMEPATH + "\\Data\\Person\\Info"
EXPORTPATH = HOMEPATH + "\\Data\\Person\\ExportFile"

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