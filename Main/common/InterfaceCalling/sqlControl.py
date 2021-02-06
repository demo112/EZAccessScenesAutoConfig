import time

import pymysql

from Main import SQL

pymysql.install_as_MySQLdb()
# from Main.common.UI_Automation.uiControl import


class SqlIO(object):
    def __init__(self):
        pass

    def link(self, db_wm):
        """
        连接数据库
        :param db_wm:
        :return:
        """
        db = pymysql.connect(host=SQL["host"], port=SQL["port"], user=SQL["username"], passwd=SQL["password"], db=db_wm,
                             charset='utf8')
        cursor = db.cursor()
        return db, cursor

    def search(self, row, db_wm, db_nm):
        """
        查找指定库-表-字段中所有内容
        :param row:字段名称
        :param db_wm:库名
        :param db_nm:表名
        :return:
        """
        db, cursor = self.link(db_wm)
        query = "SELECT {} FROM {}".format(row, db_nm)
        cursor.execute(query)

        db.commit()
        data = cursor.fetchall()
        return data

    def count(self, db_wm, db_nm):
        """
        :param db_wm:库名
        :param db_nm:表名
        :return: 指定表中条数
        """
        # 显示有多少条记录
        db, cursor = self.link(db_wm)
        query = " select count(*) from {}".format(db_nm)
        cursor.execute(query)
        db.commit()
        count_wm = cursor.fetchall()[0][0]
        return int(count_wm)

    def readPassword(self):
        """
        读取管理员密码密文
        :return:
        """
        pw = self.search("user_password", "ucs", "tbl_user")[0][0]
        return pw

    def readInfo(self, targetRow, infoRow, info, db_wm, db_nm):
        """
        :param targetRow:
        :param infoRow:
        :param info:
        :param db_wm:
        :param db_nm:
        :return:
        """
        db, cursor = self.link(db_wm)
        query = "SELECT {} FROM {} WHERE {} LIKE '{}'".format(targetRow, db_nm, infoRow, info)
        cursor.execute(query)
        db.commit()
        data = cursor.fetchall()
        return data


if __name__ == '__main__':
    sqlio = SqlIO()
    sqlio.readPassword()
