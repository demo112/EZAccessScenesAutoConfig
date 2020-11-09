# 组件，集中基础功能实现，接口调用
from Main.common.UI_Automation.uiControl import *


pm = PersonManagement()
class PersonManagementConfig:
    def __init__(self):
        pass

    def BuildDepartments(self):
        pass


    def BatchImportPerson(self, fileName):
        pm.batchImport(name="批量导入", Depth=12, foundIndex=4)
        pm.batchImportChoose(fileName=fileName, name="人员名单.xls", Depth=17, foundIndex=1, winChooseID="1148")
        pm.batchImportConfirm()
        pm.checkProgress(name="人员名单.xls", Depth=17, foundIndex=1)

    def BatchImportPhoto(self, fileName):
        pm.batchImport(name="批量导图", Depth=12, foundIndex=7)
        pm.batchImportChoose(fileName=fileName, name="人员图片.zip", Depth=17, foundIndex=1, winChooseID="1148")
        pm.batchImportConfirm()
        pm.checkProgress(name="人员图片.zip", Depth=17, foundIndex=1)


if __name__ == '__main__':
    pmc = PersonManagementConfig()
    pmc.BatchImportPhoto(fileName="C:\\Users\\user\\PycharmProjects\\Tools\\EZAccessScenesAutoConfig\\Data\\Person\\Photo\\clonfile\\PhotoZip1.zip")
