from Main.components.MakeConfig import *



def demo():
    pass


def DoBatchImportPerson():

    # 遍历导入文件
    personList = os.listdir(PERSONINFO)
    for index in range(0, len(personList)):
    #     定位部门
        dp = PERSONDEPARTMENTLIST[index]
        pm.chooseDepartment(targetId=dp)
    # #     构造文件路径
        file = personList[index]
        fileName = HOMEPATH + "\\Data\\Person\\Info\\" + file
    #     导入人员信息
        pmc.BatchImportPerson(fileName=fileName)
        time.sleep(5)

if __name__ == '__main__':
    pm = PersonManagement()
    pmc = PersonManagementConfig()
    DoBatchImportPerson()
