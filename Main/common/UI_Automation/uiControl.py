# 该文件主要放置基本操作，如：点击切换页面，为某文本框赋值，删除某条记录等
import sys
import os

import uiautomation

from .__init__ import EXPORTPATH

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import datetime

from .controlOperation import *


class ControlClint:
    """
    客户端控制：除业务页签外的所有其他操作，登录、注销、修改密码、最大化、最小化、关闭等
    """

    def __init__(self):
        self.co = ControlOperation()

    def send_user_name(self, username, Name="用户名", Depth=9, foundIndex=1):
        """
        登陆处填写用户名
        :param username: 用户名字符串
        :param Name: 元素名称
        :param Depth: 元素深度
        :param foundIndex: 索引序列号
        :return: 无
        """
        try:
            flag = uiautomation.EditControl(Name=Name, Depth=Depth, foundIndex=foundIndex)
            flag = self.co.give_value(flag, username)
            log.info(str(flag.GetValuePattern().Value))
        except Exception as e:
            # log.info("Can not control EZAccess, because: %s" % e)
            log.debug("Can not control EZAccess, because: %s" % e)

    def send_password(self, pwd, Name="密码", Depth=9, foundIndex=2):
        """
        登陆处填写密码
        :param pwd: 用户名字符串
        :param Name: 元素名称
        :param Depth: 元素深度
        :param foundIndex: 索引序列号
        :return: 无
        """
        try:
            flag = uiautomation.EditControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag = self.co.give_value(flag, pwd)
            log.info(str(flag.GetValuePattern().Value))
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def accountMore(self, AutomationId="ACMainWindowClass.ACSystemTitle.systemTitleWidget.loginWidget.UserButton"):
        """
        展开更多用户操作
        :param AutomationId: 元素的automantionid
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(AutomationId=AutomationId)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def logOut(self, status):
        """
        注销登录,并处理提示
        :param status: 注销确认结果：
        1、是
        2、否
        3、取消
        :return:
        """
        status = int(status)
        try:
            pos = autoit.mouse_get_pos()
            autoit.mouse_click(button="left", x=pos[0], y=pos[1] + 50, clicks=1, speed=1)
            if status == 1:
                flag = uiautomation.ButtonControl(AutomationId="DialogBK.btnOk")
                flag.Click()
            elif status == 2:
                flag = uiautomation.ButtonControl(AutomationId="DialogBK.btnCancel")
                flag.Click()
            elif status == 3:
                flag = uiautomation.ButtonControl(AutomationId="DialogBK.DialogTitle.FrameTitle.titleFrame.FrameClose")
                flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def userInfo(self, AutomationId="ACMainWindowClass.ACSystemTitle.systemTitleWidget.loginWidget.UserInfoButton"):
        """
        查看用户信息
        :param AutomationId: 元素的automantionid
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(AutomationId=AutomationId)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def helpInfo(self, AutomationId="ACMainWindowClass.ACSystemTitle.systemTitleWidget.loginWidget.helpBtn"):
        """
        查看帮助信息
        :param AutomationId: 元素的automantionid
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(AutomationId=AutomationId)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def minClient(self, AutomationId="ACMainWindowClass.ACSystemTitle.systemTitleWidget.titleWidget.minBtn"):
        """
        窗口最小化
        :param AutomationId: 元素的automantionid
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(AutomationId=AutomationId)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def maxClient(self, AutomationId="ACMainWindowClass.ACSystemTitle.systemTitleWidget.titleWidget.maxBtn"):
        """
        窗口最大化
        :param AutomationId: 元素的automantionid
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(AutomationId=AutomationId)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def closeClient(self, AutomationId="ACMainWindowClass.ACSystemTitle.systemTitleWidget.titleWidget.closeWinBtn"):
        """
        关闭窗口
        :param AutomationId: 元素的automantionid
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(AutomationId=AutomationId)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def confirmTemplate(self, status="confirm"):
        """
        确认请假状态
        :param status:
        confirm 确认（默认）
        cancel 取消
        :return:
        """
        try:
            if status == "confirm":
                flag = uiautomation.ButtonControl(AutomationId="btn_confirmTemplate")
            elif status == "cancel":
                flag = uiautomation.ButtonControl(AutomationId="btn_cancelTemplate")
            else:
                flag = None
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)


class DeviceManagement:
    """
    设备管理
    """

    def __init__(self):
        pass

    def tab_device(self, Name="设备管理", Depth=13, foundIndex=2):
        """
        选择设备管理页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            # flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex) 已失效，弃用
            flag = uiautomation.CustomControl(AutomationId="LinkDeviceManagement")
            flag.Click()
            return flag

        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def butadd(self, Name="精确添加", Depth=14, foundIndex=7):
        """
        精确添加按钮
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def butdelete(self, Name="批量删除", Depth=14, foundIndex=8):
        """
                 批量删除按钮
                  :param Name:
                  :param Depth:
                  :param foundIndex:
                  :return:
         """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def refreshDevice(self, Name="刷新", Depth=14, foundIndex=9):
        """
                 刷新按钮
                  :param Name:
                  :param Depth:
                  :param foundIndex:
                  :return:
         """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def butconfiguration(self, Name="复选框", Depth=23, foundIndex=8):
        """
        复选框，暂未识别
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def deviceName(self, Name="设备名称", Depth=22, foundIndex=2):
        """
        设备名称
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def ipAddress(self, Name="IP地址", Depth=22, foundIndex=3):
        """
        IP地址
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def port(self, Name="端口", Depth=22, foundIndex=4):
        """
        端口号
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def deviceType(self, Name="设备类型", Depth=22, foundIndex=5):
        """
        设备类型
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def model(self, Name="设备型号", Depth=22, foundIndex=6):
        """
        设备型号
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def status(self, Name="在线状态", Depth=22, foundIndex=7):
        """
        在线状态
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def operation(self, Name="操作", Depth=22, foundIndex=8):
        """
        操作
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def butEdit(self, Name="编辑", Depth=22, foundIndex=8):
        """
        编辑，暂未识别
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def butdel(self, Name="删除", Depth=22, foundIndex=8):
        """
        删除，暂未识别
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def buttenConfiguRation(self, Name="访问", Depth=22, foundIndex=8):
        """
        访问，暂未识别
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def checkbox(self, Name="全选", Depth=22, foundIndex=8):
        """
        全选，暂未识别
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def select(self, Name="", Depth=18, foundIndex=1):
        """
        点击,选择每页条数，20条/页，100条/页
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.EditControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def buttenPressDown(self, Name="下一页", Depth=16, foundIndex=31):
        """
        点击跳转下一页
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def buttenPressUp(self, Name="上一页", Depth=16, foundIndex=30):
        """
        点击跳转上一页
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def buttenChangePage(self, Name="", Depth=16, foundIndex=30):
        """
        输入页码跳转，未识别
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def buttenSort(self, Name="排序", Depth=23, foundIndex=30):
        """
        点击按钮排序，未识别
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            return flag
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)


class PersonManagement:
    """
    人员管理
    """

    def __init__(self):
        pass

    def tab_person(self, Name="人员管理", Depth=12, foundIndex=3):
        """
        选择人员管理页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            # flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex)  已失效，弃用
            flag = uiautomation.CustomControl(AutomationId="LinkPersonManagement")
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)


class AccessControl:
    """
    访问控制
    """

    def __init__(self):
        pass

    def tab_access(self, Name="访问控制", Depth=12, foundIndex=4):
        """
        选择访问控制页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            # flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex)  已失效，弃用
            flag = uiautomation.CustomControl(AutomationId="LinkAccessControl")
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def accessPermissions(self, Name="门禁授权", Depth=11, foundIndex=1):
        """
        门禁授权
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def addAccess(self, Name="新增授权", Depth=12, foundIndex=7):
        """
        点击新增授权按钮
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()

        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def delAccess(self, Name="删除授权", Depth=12, foundIndex=8):
        """
        点击批量删除
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def refreshAccess(self, Name="刷新", Depth=12, foundIndex=9):
        """
        点击刷新，授权刷新
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def holidayManagement(self, Name="假日管理", Depth=11, foundIndex=2):
        """
        假日管理
        :param Name:
        :param Depth:
        :param foundIndex:
        :return:
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def holidayAdd(self, Name="新增假日", Depth=12, foundIndex=7):
        """
        点击新增，添加假日
        :return:
        """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def holidayDel(self, Name="删除假日", Depth=12, foundIndex=8):
        """
        点击删除

        :return:
        """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def keyWord(self, Name="关键字", Depth=13, foundIndex=1):
        """
        搜索框内输入假日关键字
        :return:
        """
        try:
            flag = uiautomation.EditControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def butSearch(self, Name="搜索", Depth=13, foundIndex=1):
        """
        点击搜索按键，foundIndex未识别
        :return:
        """
        try:
            flag = uiautomation.CustomControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def holidayPage(self, Name="", Depth=17, foundIndex=13):
        """
        点击每页20条,弹出20条/页，50条/页，100条/页，200条/页，foundIndex未识别
        :return:
        """
        try:
            flag = uiautomation.CustomControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def holidayPage1(self, Name="", Depth=10, foundIndex=13):
        """
        选择20条/页
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def holidayPage2(self, Name="", Depth=10, foundIndex=14):
        """
        选择50条/页
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def holidayPage3(self, Name="", Depth=10, foundIndex=15):
        """
        选择100条/页
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def holidayPage4(self, Name="", Depth=10, foundIndex=16):
        """
        选择200条/页
        :return:
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)


class Attendance:
    """
    考勤统计
    """

    def __init__(self):
        self.co = ControlOperation()

    def tab_attendence(self, Name="考勤管理", Depth=12, foundIndex=4):
        """
        选择人员管理页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            # flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex)  已失效，弃用
            flag = uiautomation.CustomControl(AutomationId="LinkattendanceManagement")
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def OLD_openDepartmentOrPerson(self, departmentId="", personID=""):
        #     """
        #     界面策略更改，人员与部门平级，按顺序编号
        #     定位并展开对应目标
        #     :param departmentId: 部门编号，根部门为4096，已创建顺序类推，具体应到数据库中查询
        #     :param personID: 人员Id，从2开始，以此类推,目前建议操作15以内人员
        #     :return:
        #     """
        #     # todo 后续增加滚动滚动条方法以适配更多人员选项
        #     # todo 后续增加部门展开状态
        #     if departmentId:
        #         targetId = departmentId
        #     else:
        #         targetId = "treeDemo_1_a"
        #
        #     # if personID:
        #     #     targetId += "-" + personID
        #     # else:
        #     #     pass
        #
        #     try:
        #         flag = uiautomation.CustomControl(AutomationId=targetId).GetParentControl()
        #         flag.Click()
        #         # 以下用于人员选中，新版本不需要
        #         # if targetId > "treeDemo_1_a":
        #         #     flag = uiautomation.CustomControl(AutomationId=targetId).GetParentControl().GetFirstChildControl()
        #         # if not personID:
        #         #     flag.Click()
        #     except Exception as e:
        #         log.info("Can not control EZAccess, because: %s" % e)
        pass

    def openDepartmentOrPerson(self, targetId="", opentype=False):
        """
        人员与部门平级，按顺序编号
        :param targetId:
        :return:
        """
        # todo 后续增加滚动滚动条方法以适配更多人员选项
        # todo 后续增加部门展开状态
        if not targetId:
            targetId = "treeDemo_1_span"
        try:
            flag = uiautomation.CustomControl(AutomationId=targetId).GetParentControl()
            flag.Click()
            if opentype:
                pos = autoit.mouse_get_pos()
                autoit.mouse_click(button="left", x=pos[0] - 45, y=pos[1], clicks=1, speed=100)
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    # todo 待修改
    def attendanceRegulations(self, Name="考勤制度", Depth=23, foundIndex=6):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    # todo 待修改
    def attendanceRules(self, Name="考勤规则", Depth=23, foundIndex=6):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    # todo 待修改
    def staffSchedule(self, Name="人员排班", Depth=23, foundIndex=6):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def periodSettings(self, Name="时间段设置", Depth=23, foundIndex=6):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def shfitMgt(self, Name="班次管理", Depth=23, foundIndex=6):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def scheduleMgt(self, Name="排班管理", Depth=23, foundIndex=6):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    # todo 待修改
    def attendanceMgt(self, Name="考勤处理", Depth=23, foundIndex=6):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            # flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag = uiautomation.HyperlinkControl(AutomationId="LinkAttendanceDeal1")
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    # def LeaveMgt(self, Name="请假处理", Depth=24, foundIndex=13):
    def LeaveMgt(self, Name="请假处理", Depth=23, foundIndex=5):
        """
        选择请假处理页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def addLeaveTravel(self, Name="请假/出差", Depth=21, foundIndex=1):
        """
        点击请假/出差
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def tab_KeyWords(self, Name="请输入关键字", Depth=22, foundIndex=2):
        """
        点击右侧搜索框
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def resignInOutMgt(self, Name="补签处理", Depth=23, foundIndex=6):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.MenuItemControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def singndInOrOut(self, index=0, click="in" or "out"):
        """
        补签选中人员的某一条记录，可补签到或补签退
        注：当前仅能补签页面上展示的，无翻页和滚动功能
        :param index: 记录行数，以0开始
        :param click: 补签类型，签到，签退
        :return:
        """
        try:
            # 第四个Get进入某一行
            # 第五个Get定位至补签栏
            # todo 增加根据条数翻页功能
            # todo 增加根据条数滚动功能
            flag = uiautomation.CustomControl(AutomationId="tableContainer"). \
                GetFirstChildControl(). \
                GetChildren()[2]. \
                GetFirstChildControl(). \
                GetChildren()[index]. \
                GetChildren()[10]. \
                GetFirstChildControl()
            if click == "in":
                flag = flag.GetFirstChildControl()
            elif click == "out":
                flag = flag.GetChildren()[1]
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def attendanceStatistics(self):
        """
        选择考勤统计页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.HyperlinkControl(AutomationId="LinkAttendanceData2")
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def originalData(self, Name="原始数据", Depth=24, foundIndex=11):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def today(self, Name="当天", Depth=22, foundIndex=7):
        """
        点击当天
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def last7days(self, Name="最近7天", Depth=22, foundIndex=9):
        """
        点击最近七天
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def last30days(self, Name="最近三十天", Depth=22, foundIndex=11):
        """
        点击最近三十天
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def currentMonth(self, Name="当月", Depth=22, foundIndex=13):
        """
        点击当月
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def search(self, Name="查询", Depth=21, foundIndex=2):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def reset(self, Name="重置", Depth=21, foundIndex=1):
        """
        点击重置
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def export(self, Name="导出", Depth=22, foundIndex=3):
        """
        点击导出
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def exportToFile(self, days):
        """
        点击导出
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            # 触发导出保存界面
            Name = "导出"
            Depth = 22
            foundIndex = 3
            co = ControlOperation()
            flag = uiautomation.ButtonControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            time.sleep(60)
            #  配置保存路径
            # TODO 优化：判定路径是否存在，不存在则创建
            filePath = EXPORTPATH
            file = uiautomation.EditControl(AutomationId="1001")
            fileName = uiautomation.EditControl(AutomationId="1001").GetValuePattern().Value
            date = datetime.datetime.now().strftime("%Y%m%d")
            fileName = filePath + date + "_" + days + fileName + str(time.time())
            co.give_value(file, fileName)
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def personSearch(self, Name="请输入关键字", Depth=22, foundIndex=1):
        """
        选中人员筛选框
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.EditControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def setBodyTemperatureS(self, TemperatureS, Name="", Depth=22, foundIndex=4):
        """
        选中体温起始框,输入体温值
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        TemperatureS = str(TemperatureS)
        try:
            flag = uiautomation.EditControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            self.co.give_value(value=TemperatureS)
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def setBodyTemperatureE(self, TemperatureS, Name="", Depth=22, foundIndex=4):
        """
        选中体温起始框
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        TemperatureS = str(TemperatureS)
        try:
            flag = uiautomation.EditControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
            pos = autoit.mouse_get_pos()
            time.sleep(1)
            autoit.mouse_click(button="left", x=pos[0] + 70, y=pos[1], clicks=1, speed=100)
            self.co.give_value(value=TemperatureS)
            # autoit.send(TemperatureS)
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    # todo 待完善
    def wearingMask(self, Name="", Depth=24, foundIndex=6):
        """
        点击删除戴口罩选项
        点击展开口罩下拉框
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.CustomControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def maskUnknown(self, Name="未知", Depth=18, foundIndex=4):
        """
        点击选项：未知
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def maskNo(self, Name="否", Depth=18, foundIndex=6):
        """
        点击选项：否
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def maskYes(self, Name="是", Depth=18, foundIndex=8):
        """
        点击选项：是
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.TextControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def attendanceDetails(self, Name="考勤明细", Depth=24, foundIndex=12):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    def attendanceSummary(self, Name="考勤汇总", Depth=24, foundIndex=13):
        """
        选择原始数据页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            log.debug("Can not control EZAccess, because: %s" % e)

    # todo 待补充
    def chooseDays(self, startDay, endDay):
        pass


if __name__ == '__main__':
    pass
