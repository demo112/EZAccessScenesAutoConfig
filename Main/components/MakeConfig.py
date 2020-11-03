# 组件，集中基础功能实现，接口调用
from Main.common.UI_Automation.uiControl import *


per = PersonManagement()
class PersonManagementConfig:
    def __init__(self):
        pass

    def BuildDepartments(self):
        pass


    def BatchImportPerson(self, fileName):
        per.batchImport(name="批量导入", Depth=12, foundIndex=4)
        per.batchImportChoose(fileName=fileName, name="人员名单.xls", Depth=17, foundIndex=1, winChooseID="1148")
        per.batchImportConfirm()

    def BatchImportPhoto(self, fileName):
        per.batchImport(name="批量导图", Depth=12, foundIndex=7)
        per.batchImportChoose(fileName=fileName, name="人员图片.zip", Depth=17, foundIndex=1, winChooseID="1148")
        per.batchImportConfirm()
        pass


if __name__ == '__main__':
    pmc = PersonManagementConfig()
    pmc.BatchImportPhoto(fileName="C:\\Users\\user\\PycharmProjects\\Tools\\EZAccessScenesAutoConfig\\Data\\Person\\Photo\\clonfile\\PhotoZip1.zip")
