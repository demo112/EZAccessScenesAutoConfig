from Main.components.personConfig import *
from Main.common.InterfaceCalling.sqlControl import *
from Main.common.InterfaceCalling.interFaceControl import *

def demo():
    pass


def DoBatchImportPerson():
    # 遍历导入文件
    pm = PersonManagement()
    pmc = PersonManagementConfig()
    personList = os.listdir(PERSONINFO)
    for index in range(0, len(personList)):
        #     定位部门
        dp = PERSONDEPARTMENTLIST[index]
        pm.chooseDepartment(targetId=dp)
        #     构造文件路径
        file = personList[index]
        fileName = PERSONINFO + "\\" + file
        #     导入人员信息
        pmc.BatchImportPerson(fileName=fileName)


def DoBatchImportPhoto():
    pmc = PersonManagementConfig()
    photoList = os.listdir(PHOTOCOPYPATH)
    for index in range(0, len(photoList)):
        #     构造文件路径
        file = photoList[index]
        fileName = PHOTOCOPYPATH + "\\" + file
        #     导入图片信息
        print(file)
        pmc.BatchImportPhoto(fileName=fileName)

def DoBatchAddDevice():
    dim = DeviceInterfaceManagement()
    MaxDeviceNum = DEVICEUSERINFO["MaxDeviceNum"]
    dim.devicesAdd(range(MaxDeviceNum))


if __name__ == '__main__':
    DoBatchImportPerson()
    DoBatchImportPhoto()
