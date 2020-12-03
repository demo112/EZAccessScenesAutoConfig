# 快捷方式

from Main.__init__ import *
from Main.components.ControlByInterface import *
from Main.components.ControlByAutomation import *


class PersonMgtInk(HttpMethod):
    def __init__(self):
        super().__init__()
        self.sql = SqlIO()

    def do_batch_remove_person_by_dp(self, department):
        """
        删除指定部门所有人员
        :param department: 部门Id，鼠标悬浮于部门名称可见
        :return:
        """
        pim = PersonInterfaceManagement()
        _personList = self.sql.readInfo("person_id", "dept_id", department, "ucs", "tbl_person")
        person_list = [int(per[0]) for per in _personList]
        pim.personRemove(person_list)

    def do_batch_remove_person_all(self):
        """
        批量删除所有人员
        :return:
        """
        deptList = self.sql.search("dept_id", "ucs", "tbl_dept")
        print(deptList)
        for dept in deptList:
            try:
                self.do_batch_remove_person_by_dp(dept[0])
            except:
                pass


if __name__ == '__main__':
    pmi = PersonMgtInk()
    pmi.do_batch_remove_person_by_dp(4097)
    # pmi.do_batch_remove_person_all()
