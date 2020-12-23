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


class FakePostMan(HttpMethod):
    def do_try_url(self, url_, token_or_not_, params_):
        url_ = "http://%s:%d%s" % (self.server_ip, self.port, url_)
        header = {
            "Content-Length": 0,
            "Accept": "application/json, text/plain, */*",
            "Cache-Control": "no-cache",
            "Origin": "file://",
            "Authorization": "",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "x-user-id": "116312915581075456",
            "Forwarded": 'proto=http;host="127.0.0.1:10008";for="127.0.0.1:52461"',
            "X-Forwarded-For": "127.0.0.1",
            "X-Forwarded-Proto": "http",
            "X-Forwarded-Port": "10008",
            "X-Forwarded-Host": "127.0.0.1:10008",
            "host": "127.0.0.1:10008",
        }
        if token_or_not_:
            header["Authorization"] = self.token
        else:
            pass
        body = json.JSONEncoder().encode(params_)
        header["Content-Length"] = len(body)
        response = self.OPENAPI_POST(url_, header, body)
        return response


if __name__ == '__main__':
    fp = FakePostMan()
    # 批量补签
    url = "/openapi/atnd/attendance/supplement/add"
    token = True
    for p in range(1, 500):
        params = {
            "seqId": p,
            "personId": p + 4500,
            "signInTime": "2020/12/14 09:00",
            # "signOutTime": "2020/12/14 18:00",
        }
        res_True = fp.do_try_url(url, token, params)
        # res_False = fp.do_try_url(url, False, params)
        print("res_True:", res_True)
        # print("res_False:", res_False)
    # # 批量请假
    #
    # url = "/openapi/atnd/attendance/leave/add"
    # token = True
    # for p in range(300, 501):
    #     params = {"duration":900,
    #               "endTime":"2020/12/14 18:00",
    #               "personName":"jys0010000000%dABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv" % p,
    #               "primitive":"0",
    #               "remark":"",
    #               "startTime":"2020/12/14 09:00",
    #               "subtype":"0",
    #               "departName":"新节点1",
    #               "personCode":"jys0010000000%d" % p,
    #               "personId":4500+ p}
    #     res_True = fp.do_try_url(url, token, params)
    #     # res_False = fp.do_try_url(url, False, params)
    #     print("res_True:", res_True)
        # print("res_False:", res_False)
