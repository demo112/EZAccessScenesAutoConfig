# 组件，集中基础功能实现，接口调用
from Main.common.UI_Automation.uiControl import *


def DoBatchImportPerson(filename=None):
    # 遍历导入文件
    if filename:
        personList = [filename]
    else:
        personList = os.listdir(PERSONINFO)

    pm = PersonManagement()
    for index in range(0, len(personList)):
        #     定位部门
        dp = PERSONDEPARTMENTLIST[index]
        pm.chooseDepartment(targetId=dp)
        #     构造文件路径
        file = personList[index]
        fileName = PERSONINFO + "\\" + file
        #     导入人员信息
        pm.batchImport(name="批量导入", Depth=12, foundIndex=4)
        pm.batchImportChoose(fileName=fileName, name="人员名单.xls", Depth=17, foundIndex=1, winChooseID="1148")
        pm.batchImportConfirm()
        pm.checkProgress(name="人员名单.xls", Depth=17, foundIndex=1)


def DoBatchImportPhoto(filename=None):
    if filename:
        photoList = [filename]
    else:
        photoList = os.listdir(PHOTOCOPYPATH)

    pm = PersonManagement()
    for index in range(0, len(photoList)):
        #     构造文件路径
        file = photoList[index]
        fileName = PHOTOCOPYPATH + "\\" + file
        #     导入图片信息
        pm.batchImport(name="批量导图", Depth=12, foundIndex=7)
        pm.batchImportChoose(fileName=fileName, name="人员图片.zip", Depth=17, foundIndex=1, winChooseID="1148")
        pm.batchImportConfirm()
        pm.checkProgress(name="人员图片.zip", Depth=17, foundIndex=1)


if __name__ == '__main__':
    DoBatchImportPerson()
    # DoBatchImportPhoto(
    #     "C:\\Users\\user\\PycharmProjects\\Tools\\EZAccessScenesAutoConfig\\Data\\Person\\Photo\\clonfile\\PhotoZip1.zip")
