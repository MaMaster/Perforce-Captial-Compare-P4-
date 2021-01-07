# Python 访问 P4 depot
# 运行需要安装P4python
# python支持python3.0-python3.7.X
import os
from P4 import *

p4 = P4()
p4.user = "Account_name"
p4.password = "Accont_password"
p4.connect()
p4.run_login()
opened = p4.run_opened()


#读取P4目录,生成词典
#p4.run("dirs", '//Streams/dev-r6.1/Program/Client/Assets/...')
#depot路径后需要有“...”才会读取后续目录

def Create_dic():
    filedirs = input ("请输入要检查的分支路径：")
    filedic = p4.run("files", filedirs)
    return filedic

#列表元素取出，字典元素筛选,并去重
def SwitchDicToList():
    filedic = Create_dic()
    filelist = [item["depotFile"] for item in filedic for key in item]
    finallist = list(set(filelist))
    return finallist


#转换小写确保唯一性

def CaptialCheck():
    dataSet = set() 
    finallist = SwitchDicToList()
    for item in finallist:
        
        if item.lower() in dataSet:   # 判断小写的字符串是否在set中  如果有，说明重复了
            print(item)
            #print(item.lower())
        else:                           # 如果没有，说明是第一次出现这个字符串，将它变为小写加入到set中
            dataSet.add(item.lower())
    print ()
    print ("大小写检查完成，如果没有显示文件名称，那就是本目录没有大小写问题")

# p4 depot中会记录已删除的文件，本脚本同样能会识别一些已删除的文件名，待后续优化

CaptialCheck()


