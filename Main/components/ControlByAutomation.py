# 组件，集中基础功能实现，接口调用
from Main.OtherTools.makePersonInfo import MakePhoto, makePhotoZip
from Main.OtherTools.xmlFileOperation import XmlSearch
from Main.common.UI_Automation.uiControl import *
from Main.common.InterfaceCalling.sqlControl import SqlIO


def do_batch_import_person(filename=None):
    """

    :param filename: 导入文件的名称
    :return:
    """
    # 切换至人员管理界面
    pm = PersonManagement()
    pm.tab_person()

    # 遍历导入文件
    if filename:
        person_list = [filename]
    else:
        person_list = os.listdir(PERSONINFO)
    # todo 增加人员信息源文件判断及生成功能
    pm = PersonManagement()
    for index in range(0, len(person_list)):
        #     定位部门
        sq = SqlIO()
        dept_list = sq.search("dept_id", "ucs", 'tbl_dept')[1:]
        while True:
            time.sleep(1)
            dp = str(dept_list[index][0])
            flag = pm.chooseDepartment(targetId=dp)
            #     构造文件路径
            file = person_list[index]
            file_name = PERSONINFO + "\\" + file
            #     导入人员信息
            flag1 = pm.batchImport(name="批量导入", Depth=12, foundIndex=5)
            # 没有人员划归就是4，有就是5，数批量导入是第几个按钮即可
            # flag1 = pm.batchImport(name="批量导入", Depth=12, foundIndex=4)
            flag2 = pm.batchImportChoose(fileName=file_name, name="人员名单.xls", Depth=17, foundIndex=1, winChooseID="1148")
            flag3 = pm.batch_import_confirm()
            if flag * flag1 * flag2 * flag3:
                break
            else:
                pass
        #     todo 增加人员导入结果确认功能
        # """通过校验导入前后的人员数量确认”“”
        # pm.checkProgress(name="人员名单.xls", Depth=17, foundIndex=1)


def do_batch_import_photo(filename=None):
    """

    :param filename: 导入照片压缩包名称
    :return:
    """

    def checkProgress(flag=None):
        sio = SqlIO()
        timeout = 10
        times = 0
        f = False
        while True:
            # 设置超时机制
            if times >= timeout:
                break
            try:
                finish = uiautomation.EditControl(name="人员图片.zip", Depth=17, foundIndex=1)
                print(finish)
                end_num = sio.count("ucs", "tbl_person_pic")
                print(end_num)
                if flag[0] - end_num == flag[1]:
                    f = True
                    if finish:
                        pass
                    else:
                        break
                else:
                    time.sleep(1)
            except Exception as e:
                print(e)
                times += 1
            return f

    if filename:
        photo_list = [filename, ]
    else:
        photo_list = os.listdir(PHOTOCOPYPATH)
        # 判断当前材料状况，无素材自动生成一份
        if len(photo_list) == 0:
            makePhotoZip()
        else:
            pass
    pm = PersonManagement()
    # 预读每次导入会新增几张照片
    config_tree = xf.read_xml(CONFIGPATH + "\config.xml")
    each_zip_num = xs.find_nodes(config_tree, "PersonPicture/eachZipNum")
    sio = SqlIO()
    start_num = sio.count("ucs", "tbl_person_pic")
    for index in range(0, len(photo_list)):
        #     构造文件路径
        file = photo_list[index]
        file_name = PHOTOCOPYPATH + "\\" + file
        print(file_name)
        #     导入图片信息
        pm.batchImport(name="批量导图", Depth=12, foundIndex=8)
        pm.batchImportChoose(fileName=file_name, name="人员图片.zip", Depth=17, foundIndex=1, winChooseID="1148")
        pm.batch_import_confirm()
        status = pm.checkProgress(name="人员图片.zip", Depth=17, foundIndex=1)
        if status:
            os.remove(filename)


if __name__ == '__main__':
    do_batch_import_person()
    # do_batch_import_photo(
    #     "C:\\Users\\user\\PycharmProjects\\Tools\\EZAccessScenesAutoConfig\\Data\\Person\\Photo\\clonfile\\PhotoZip1.zip")
