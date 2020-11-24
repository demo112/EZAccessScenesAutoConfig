from Main.__init__ import *
from Main.components.ControlByInterface import *
from Main.components.ControlByAutomation import *
# 判断是否要初始化
print(IFRESTORE)
if IFRESTORE:
    # DoRemoveAccess('111111')
    DoBatchRemovePerson()
    # DoBatchRemoveDevice()
    pass

# DoBatchAddDevice()
# DoBatchImportPerson()
DoBatchImportPhoto()
# 判断是否备份当前配置

# 挑选配置文件

# 执行配置

