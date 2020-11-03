from xml.etree import ElementTree  as  ET
from Main.__init__ import *

title_en = ["Person ID(*)", "Name(*)", "Gender(*)", "ID No.", "IC Card No.", "Date of Birth", "Phone", "Address"]
title_cn = ["人员编号(*)", "姓名(*)", "性别(*)", "证件号码", "IC卡号", "出生年月", "手机号码", "地址"]

# 人员配置规格
# 读取配置表格至root对象
# xl = ET.parse(CONFIGPATH + "/" + "config.xml")
xl = ET.parse(r"C:/Users/user/PycharmProjects/Tools/EZAccessScenesAutoConfig/Scenes/config.xml")
root = xl.getroot()

# 素材生成配置
checkLanguage = root.find("checkLanguage").text

# 人员信息配置
maxNumAllDp = int(root.find("DepartmentInfo").find("maxNumAllDp").text)
maxNumEachDp = int(root.find("DepartmentInfo").find("maxNumEachDp").text)

PersonID = root.find("PersonInfo").find("PersonID").text
Name = root.find("PersonInfo").find("Name").text
GenderRangeMin = int(root.find("PersonInfo").find("GenderRangeMin").text)
GenderRangeMax = int(root.find("PersonInfo").find("GenderRangeMax").text)
IDNo = root.find("PersonInfo").find("IDNo").text
ICCardNo = root.find("PersonInfo").find("ICCardNo").text
DateOfBirth = root.find("PersonInfo").find("DateOfBirth").text
PhoneRangeMin = int(root.find("PersonInfo").find("PhoneRangeMin").text)
PhoneRangeMax = int(root.find("PersonInfo").find("PhoneRangeMax").text)
Department = root.find("PersonInfo").find("Department").text
Address = root.find("PersonInfo").find("Address").text
PhotoNum = int(root.find("PersonInfo").find("PhotoNum").text)

# 人员照片信息
zipFileSize = int(root.find("PersonPicture").find("zipFileSize").text)