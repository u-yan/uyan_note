import os
from pathlib import Path
#处理图片路径
path_input = input()
sourcePath = ""
for i in path_input:
    if i != '\'':
        sourcePath += i

goalPath = "./"
notePath = input()
goalPath += notePath + "/"
# 获取文件夹内文件数量
filenum, dirnum = 0, 0

for lists in os.listdir(Path(goalPath)):
    sub_path = os.path.join(goalPath, lists)
    print(sub_path)
    if os.path.isfile(sub_path):
        filenum = filenum+1
    elif os.path.isdir(sub_path):
        dirnum = dirnum+1

goalPath = goalPath + filenum

print(sourcePath)
print(goalPath)
print(filenum)
#路径获取正确
# os.rename(sourcePath, goalPath)