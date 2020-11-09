import time

import pymysql

pymysql.install_as_MySQLdb()
from Main.common.UI_Automation.uiControl import *


class SqlIO(object):
    def __init__(self):
        pass

    def link(self, db_wm):
        db = pymysql.connect(host=SQL["host"], port=SQL["port"], user=SQL["username"], passwd=SQL["password"], db=db_wm,
                             charset='utf8')
        cursor = db.cursor()
        return db, cursor
    def search(self, row, db_wm, db_nm):
        db, cursor = self.link(db_wm)
        query = "SELECT {} FROM {}".format(row, db_nm)
        cursor.execute(query)

        db.commit()
        data = cursor.fetchall()
        return data

    def readPassword(self):
        pw = self.search("user_password", "ucs", "tbl_user")[0][0]
        return pw


if __name__ == '__main__':
    sqlio = SqlIO()
    sqlio.readPassword()
