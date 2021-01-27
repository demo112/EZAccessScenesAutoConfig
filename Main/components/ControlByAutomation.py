# 组件，集中基础功能实现，接口调用
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
            flag2 = pm.batchImportChoose(fileName=file_name, name="人员名单.xls", Depth=17, foundIndex=1, winChooseID="1148")
            flag3 = pm.batch_import_confirm()
            if flag*flag1*flag2*flag3:
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
    if filename:
        photo_list = [filename, ]
    else:
        photo_list = os.listdir(PHOTOCOPYPATH)

    pm = PersonManagement()
    for index in range(0, len(photo_list)):
        #     构造文件路径
        file = photo_list[index]
        file_name = PHOTOCOPYPATH + "\\" + file
        #     导入图片信息
        pm.batchImport(name="批量导图", Depth=12, foundIndex=8)
        pm.batchImportChoose(fileName=file_name, name="人员图片.zip", Depth=17, foundIndex=1, winChooseID="1148")
        pm.batch_import_confirm()
        pm.checkProgress(name="人员图片.zip", Depth=17, foundIndex=1)


if __name__ == '__main__':
    do_batch_import_person()
    # do_batch_import_photo(
    #     "C:\\Users\\user\\PycharmProjects\\Tools\\EZAccessScenesAutoConfig\\Data\\Person\\Photo\\clonfile\\PhotoZip1.zip")
