from Main.__init__ import *
from Main.components.ControlByInterface import *
from Main.components.ControlByAutomation import *

# 判断是否要初始化
if IFRESTORE == "True":
    do_batch_remove_access()
    do_batch_remove_person()
    do_batch_remove_device()

do_batch_add_device(DNS=DEVICEUSERINFO["VLAN"], index=DEVICEUSERINFO["LONG"], Num=DEVICEUSERINFO["MaxDeviceNum"])
print("即将进行人员信息配置，请切换至EZAccess客户端。导入前请不要操作鼠标")
time.sleep(3)
# do_batch_import_person()
# do_batch_import_photo()
# do_add_access(ACCESS_DEFAULT_INFO["name"],ACCESS_DEFAULT_INFO["personRange"], ACCESS_DEFAULT_INFO["deviceRange"])
do_add_access("示例", (1, 100), (1, 32))
do_add_access("示例11", (1, 10), (1, 3))
# 判断是否备份当前配置

# 挑选配置文件

# 执行配置
