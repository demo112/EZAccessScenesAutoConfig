import pymysql
pymysql.install_as_MySQLdb()


def db_count(db_wm,db_nm):
    # 显示有多少条记录
    db = pymysql.connect(host='localhost', port=10007, user='configRoot', passwd='Smbtest0', db=db_wm, charset='utf8')
    cursor = db.cursor()
    query = " select count(*) from {}".format(db_nm)
    cursor.execute(query)
    db.commit()
    count_wm = cursor.fetchall()
    print(db_nm,'数据库共有',count_wm[0][0],'数据')


if __name__=='__main__':
    db_wm = 'ucs' #mysql数据库名
    db_nm = 'tbl_person'  #mysql数据表名
    db_count(db_wm,db_nm)