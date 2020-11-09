# 该文件主要放置基础操作方法：如点击、赋值、编辑、选择等
from Main.common.UI_Automation.__init__ import *

import sys
import time
import autoit
from Main.common.UI_Automation.__init__ import *
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


class ControlOperation:
    """
    客户端具体操作方法类，
    如：
    多选框勾选；
    文本框编辑、删除、赋值；
    等
    """

    def __init__(self):
        pass

    # 操作方法
    def give_value(self, target=None, value="null"):
        """
        为查找到的文本框元素赋值
        :param target: 目标元素
        :param value: 需要赋的值
        :return: 已赋值的对象
        """
        value = str(value)
        try:
            if target:
                target.Click()
            else:
                pass
            # pynput模块，弃用
            # pynput.keyboard.Controller().type(value + "\n")
            autoit.send("^a" + "{DELETE}")
            autoit.send(value + "{LSHIFT}" + "{ENTER}")
            time.sleep(0.6)
        except Exception as e:
            log.warning("【%s】赋值【%s】失败，请处理！" % (target.Name, value))
            log.warning("原因：", e)
        return target

    def delete_value(self, target):
        """
        将找到的文本框内容删除
        :param target: 目标元素
        :return: 已赋值的对象
        """
        try:
            target.Click()
            # 全选文本框内内容，并删除
            autoit.send("^a" + "{DELETE}")
            time.sleep(.6)
        except Exception as e:
            log.warning("【%s】内容删除失败，请处理！" % (target.Name))
            log.warning("原因：", e)
        return target




if __name__ == '__main__':
    pass
