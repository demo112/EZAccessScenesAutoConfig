# 快捷方式

from Main.__init__ import *
from Main.components.ControlByInterface import *
from Main.components.ControlByAutomation import *


class PersonMgtInk(HttpMethod):
    def DoBatchRemovePersonByDp(self, department):
        """

        :param department: 部门Id，鼠标悬浮于部门名称可见
        :return:
        """
        pim = PersonInterfaceManagement()
        sql = SqlIO()
        _personList = sql.readInfo("person_id", "dept_id", department, "ucs", "tbl_person")
        person_list = [int(per[0]) for per in _personList]
        pim.personRemove(person_list)


if __name__ == '__main__':
    pmi = PersonMgtInk()
    pmi.DoBatchRemovePersonByDp(4098)
