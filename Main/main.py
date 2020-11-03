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
        #     构造文件路径
        file = personList[index]
        fileName = PERSONINFO + "\\" + file
        #     导入人员信息
        pmc.BatchImportPerson(fileName=fileName)
        # 导入后根据屏蔽层  状态判断是否导入完成
        while True:
            if pm.chooseDepartment(targetId="4096"):
                break
            else:
                time.sleep(1)
                pass

def DoBatchImportPhoto():
    photoList = os.listdir(PHOTOCOPYPATH)
    for index in range(0, len(photoList)):
        #     构造文件路径
        file = photoList[index]
        fileName = PHOTOCOPYPATH + "\\" + file
        #     导入图片信息
        # pmc.BatchImportPhoto(fileName=fileName)
        time.sleep(5)
        print("Import Success")
        # 导入后根据屏蔽层  状态判断是否导入完成
        while True:
            if pm.chooseDepartment(targetId="4096"):
                print(11)
                break
            else:
                time.sleep(1)
                pass

if __name__ == '__main__':
    pm = PersonManagement()
    pmc = PersonManagementConfig()
    # DoBatchImportPerson()
    DoBatchImportPhoto()

