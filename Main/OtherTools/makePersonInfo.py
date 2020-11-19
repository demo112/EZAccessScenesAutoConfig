# coding=utf-8

import random
import os
import time
from zipfile import ZipFile

import xlwt

from Main.OtherTools import *


def formatNum(num):
    """
    格式化编号
    :param num:
    :return:格式化后编号
    """
    if num < 10:
        fnum = "00" + str(num)
    elif num < 100:
        fnum = "0" + str(num)
    elif num < 1000:
        fnum = str(num)
    else:
        fnum = ""
    return fnum


class PersonList():

    def __init__(self):
        self.maxNumEachDp = maxNumEachDp
        self.DpNum = int(maxNumAllDp / maxNumEachDp)

    def readTemplats(self, filename):
        file = MOTHERFILEPATH + "\\" + filename
        with open(file, 'rb') as f:
            title = f.readlines()
            for t in title:
                t = t.decode('big5')
                print(t)
            return title

    def makePerson(self):
        """
        根据用户配置构建人员信息
        :return:满规格人员列表
        """
        all_person = {}

        for dp in range(1, self.DpNum + 1):
            dp_person = []
            dp = formatNum(dp)
            for num in range(1, self.maxNumEachDp + 1):
                num = formatNum(num)
                t = time.localtime()
                _person_info = []
                _person_info.append(PersonID % (dp, num))
                _person_info.append(Name % (dp, num))
                _person_info.append(random.randint(GenderRangeMin, GenderRangeMax))
                _person_info.append(IDNo % (dp, num))
                _person_info.append(ICCardNo % (dp, num))
                _person_info.append(DateOfBirth % (t.tm_year, t.tm_mon, t.tm_mday))
                _person_info.append(random.randint(PhoneRangeMin, PhoneRangeMax))
                _person_info.append(Address)

                dp_person.append(_person_info)
            all_person["dp:" + dp] = dp_person

        return all_person

    def writePersonList(self, all_person):
        """
        根据人员创建表格
        :param all_person: 满规格人员列表
        :return:
        """
        language = checkLanguage
        if "cn" == language:
            title = title_cn
        else:
            title = title_en

        for dp in range(1, self.DpNum + 1):
            # print(all_person)
            dp = formatNum(dp)
            dp_person = all_person["dp:" + dp]
            file = PERSONINFO + "\\" + language + dp + ".xls"

            f = xlwt.Workbook()
            sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
            # 写入表头
            for row in range(len(title)):
                sheet1.write(0, row, title[row])
            # 将数据写入第 i 行，第 j 列
            i = 1
            for person in dp_person:
                for row in range(len(person)):
                    sheet1.write(i, row, person[row])
                i = i + 1

            f.save(file)  # 保存文件


class MakePhoto:
    def __init__(self):
        pass

    def makePhoto(self, motherFilePath, copyFilePath):
        fileList = os.listdir(copyFilePath)
        for file in fileList:
            _filePath = copyFilePath + "\\" + file
            os.remove(_filePath)
        with open(motherFilePath, mode="rb") as reader:
            pic = reader.read()
        # 按部门轮巡
        for dp in range(1, int(maxNumAllDp / maxNumEachDp) + 1):
            dp = formatNum(dp)
            # 按人员轮巡
            for person in range(1, maxNumEachDp + 1):
                person = formatNum(person)
                for index in range(1, PhotoNum + 1):
                    name = copyFilePath + "\\" + PersonID % (dp, person) + "_" + str(index) + ".jpg"
                    with open(name, mode="wb") as target:
                        target.write(pic)

    def zipPhoto(self, motherFilePath, copyFilePath):
        # 收集路径下非zip文件
        fileList = os.listdir(copyFilePath)
        for file in fileList:
            if ".zip" in file:
                fileList.remove(file)
        # 计算每个文件中允许照片数量及压缩包数量
        motherFileSize = round(os.path.getsize(motherFilePath) / 1024, 2) + 0.2     #单张照片大小
        eachZipNum = int(zipFileSize * 1024 / motherFileSize)                 #单个包大小
        zipFileNum = int(len(fileList) / eachZipNum) + 1
        print(motherFileSize)
        print(eachZipNum)
        print(zipFileNum)

        for z in range(1, zipFileNum + 1):
            # 拆分列表分别写入
            _list = fileList[eachZipNum * (z - 1):eachZipNum * (z)]
            file = copyFilePath + "\\" + "PhotoZip%d.zip" % z
            with ZipFile(file, "w") as zf:
                for pic in _list:
                    _filePath = copyFilePath + "\\" + pic
                    zf.write(_filePath, arcname=pic, compress_type=None, compresslevel=None)
            for pic in _list:
                _filePath = copyFilePath + "\\" + pic
                os.remove(_filePath)
            time.sleep(1)


def makePersonList():
    pl = PersonList()
    all_person = pl.makePerson()
    pl.writePersonList(all_person)


def makePhotoZip():
    clon = MakePhoto()
    motherFilePath = MOTHERFILEPATH + "\\" + os.listdir(MOTHERFILEPATH)[0]
    copyFilePath = PHOTOCOPYPATH
    clon.makePhoto(motherFilePath, copyFilePath)
    clon.zipPhoto(motherFilePath, copyFilePath)


if __name__ == '__main__':
    # pl = PersonList()
    # title = title_cn
    # all_person = pl.makePerson()
    # pl.writePersonList(all_person)
    #
    # clon = MakePhoto()
    # motherFilePath = MOTHERFILEPATH + "\\" + os.listdir(MOTHERFILEPATH)[0]
    # copyFilePath = PHOTOCOPYPATH
    # clon.makePhoto(motherFilePath, copyFilePath)
    # clon.zipPhoto(motherFilePath, copyFilePath)
    makePersonList()
    # makePhotoZip()
    pass
