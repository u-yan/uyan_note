

import pyperclip
import FileOperation
#处理图片路径
while True:
    path_input = input()
    if path_input == "exit":
        break
    sourcePath = ""
    for i in path_input:
        if i != '\'':
            sourcePath += i
    goalPath = "./"
    notePath = input()
    goalPath += notePath + "/img/"
    # 获取文件夹内文件数量
    
    filenum = FileOperation.FileOperation(goalPath).getImgCnt()
    #数量获取成功
    goalPath = goalPath + str(filenum)
    goalPath += ".png" # 
    print(sourcePath)
    print(goalPath)
    print(filenum)
    FileOperation.os.rename(sourcePath, goalPath)
    #更改路径成功
    FileOperation.os.system("bash submit.sh")
    copyContext = "![](" + "./img/" + str(filenum) + ".png)"# 图片相对路径转化成markdown
    pyperclip.copy(copyContext)
    print("************sucessed!**************")