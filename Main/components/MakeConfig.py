# 组件，集中基础功能实现，接口调用
from Main.common.UI_Automation.uiControl import *


per = PersonManagement()
class PersonManagementConfig:
    def __init__(self):
        pass

    def BuildDepartments(self):
        pass


    def BatchImportPerson(self, fileName):
        per.batchImport()
        per.batchImportChoose(fileName=fileName)
        per.batchInportConfirm()

if __name__ == '__main__':
    pr = PersonManagementConfig()
    pr.BatchImportPerson(fileName=HOMEPATH + "\\Data\\Person\\Info\\cn004.xls")
