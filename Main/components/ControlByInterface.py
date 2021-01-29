from Main.common.InterfaceCalling.sqlControl import *
from Main.common.InterfaceCalling.interFaceControl import *


def do_batch_remove_person():
    pim = PersonInterfaceManagement()
    res = pim.personRemove("all")
    res = pim.getResData(res)


def do_batch_add_device(DNS, index, Num):
    dim = DeviceInterfaceManagement()
    dim.devices_add(DNS, index, Num)


def do_batch_remove_device(*args):
    dim = DeviceInterfaceManagement()
    res = dim.deviceRemove(*args)
    response = dim.getResData(res)
    for device in response["deviceList"]:
        code = device["resultCode"]
        if code != 200:
            msg = "设备【{}】因:'{}'无法删除".format(device["deviceId"], device["resultMessage"])
            log.warning(msg)


def do_add_access(name, person_set, device_set):
    """

    :param name: 授权组名称
    :param person_set: (person_min, person_max)
    :param device_set: (device_min, devide_max)
    :return: 无
    """
    aim = AccessInterfaceManagement()
    name = str(name)
    # person_list = range(person_set[1], person_set[3]+1)
    person_list = range(person_set[0], person_set[1] + 1)
    device_list = range(device_set[0], device_set[1] + 1)
    aim.access_add(name, person_list, device_list)


def do_batch_remove_access(name=None):
    aim = AccessInterfaceManagement()
    if name:
        name_list = [name, ]
    else:
        res = aim.accessSearch()
        name_list = aim.getResData(res)
    for _name in name_list:
        res = aim.access_remove(_name["permissionGroupName"])
        code = aim.getStatusCode(res)
        if code == 200:
            pass
        else:
            log.error("{}没有正确删除，请处理异常".format(_name))


if __name__ == '__main__':
    # do_batch_remove_device("all")
    # do_batch_add_device()
    # do_batch_remove_person()
    # do_batch_import_person()
    # do_batch_import_photo()
    do_batch_remove_access()
