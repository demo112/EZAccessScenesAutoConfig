from xml.etree import ElementTree  as  ET
from Main.__init__ import *

title_en = ["Person ID(*)", "Name(*)", "Gender(*)", "ID No.", "IC Card No.", "Date of Birth", "Phone", "Address"]
title_cn = ["人员编号(*)", "姓名(*)", "性别(*)", "身份证号", "IC卡号", "出生年月", "手机号码", "地址"]

# 人员配置规格
# 读取配置表格至root对象

config_xl = ET.parse(CONFIGPATH + "\\" + "config.xml")
configRoot = config_xl.getroot()

# 素材生成配置
checkLanguage = configRoot.find("checkLanguage").text

# 人员信息配置
maxNumAllDp = int(configRoot.find("DepartmentInfo").find("maxNumAllDp").text)
maxNumEachDp = int(configRoot.find("DepartmentInfo").find("maxNumEachDp").text)

PersonID = configRoot.find("PersonInfo").find("PersonID").text
Name = configRoot.find("PersonInfo").find("Name").text
GenderRangeMin = int(configRoot.find("PersonInfo").find("GenderRangeMin").text)
GenderRangeMax = int(configRoot.find("PersonInfo").find("GenderRangeMax").text)
IDNo = configRoot.find("PersonInfo").find("IDNo").text
ICCardNo = configRoot.find("PersonInfo").find("ICCardNo").text
DateOfBirth = configRoot.find("PersonInfo").find("DateOfBirth").text
PhoneRangeMin = int(configRoot.find("PersonInfo").find("PhoneRangeMin").text)
PhoneRangeMax = int(configRoot.find("PersonInfo").find("PhoneRangeMax").text)
Department = configRoot.find("PersonInfo").find("Department").text
Address = configRoot.find("PersonInfo").find("Address").text
PhotoNum = int(configRoot.find("PersonInfo").find("PhotoNum").text)

# 人员照片信息
zipFileSize = int(configRoot.find("PersonPicture").find("zipFileSize").text)