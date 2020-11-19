from Main.components.ControlByAutomation import PersonManagementConfig
from Main.OtherTools.Log.CreateLog import CreateLog
from Main.common.InterfaceCalling.sqlControl import *
from Main.common.InterfaceCalling.interFaceControl import *

log = CreateLog().get_logger()


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


def DoBatchRomovePerson():
    pim = PersonInterfaceManagement()
    res = pim.personRemove("all")
    res = pim.getResData(res)
    print(res)

    pass


def DoBatchAddDevice():
    dim = DeviceInterfaceManagement()
    dim.devicesAdd()


def DoBatchRemoveDevice(*args):
    dim = DeviceInterfaceManagement()
    response = dim.deviceRemove(*args)
    response = dim.getResData(response)
    for device in response["deviceList"]:
        code = device["resultCode"]
        if code != 200:
            msg = "设备【{}】因:'{}'无法删除".format(device["deviceId"], device["resultMessage"])
            log.warning(msg)

def DoAddAccess(name, personList, deviceList):
    aim = AccessInterfaceManagement()
    aim.accessAdd(name, personList, deviceList)

def DoRemoveAccess(name):
    aim = AccessInterfaceManagement()
    aim.accessRemove(name)



if __name__ == '__main__':
    # DoBatchRemoveDevice("all")
    DoBatchRomovePerson()
    # DoBatchImportPerson()
    # DoBatchImportPhoto()