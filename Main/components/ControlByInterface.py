from Main.common.InterfaceCalling.sqlControl import *
from Main.common.InterfaceCalling.interFaceControl import *


def DoBatchRemovePerson():
    pim = PersonInterfaceManagement()
    res = pim.personRemove("all")
    res = pim.getResData(res)
    print(res)


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
    DoBatchAddDevice()
    # DoBatchRemovePerson()
    # DoBatchImportPerson()
    # DoBatchImportPhoto()
