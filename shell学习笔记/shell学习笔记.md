- 第一行`#!/bin/bash` 带表你选择的解释器
- `source .bash_profile`， `~\.bash_profile`是用户的环境变量，所以修改的时候要`source .bash_profile`才能生效
- `echo $var`的时候千万不能忘记`$` 符号。
- 检测`bash`脚本是否有问题 `bash -n demo.sh`如果没有结果，就代表脚本没问题。
- `[set]Var_Name=Value` 全局变量的赋值，一般情况下使用全局变量即可，是作用于本脚本所有位置。
- `read`命令可读取用户输入，`-p`参数可以在后面添加提示`text`来让用户输入，然后变量放在最后。
- 统计文件数量`ls -l |grep "^-"|wc -l #统计当前文件夹里文件数量`
- 
- 提取文件名`name+=$(basename $path)`
- 复制文件夹
```shell
命令格式：cp [-adfilprsu] 源文件(source) 目标文件(destination)
cp [option] source1 source2 source3 ... directory
```
参数说明：
-a:是指archive的意思，也说是指复制所有的目录
-d:若源文件为连接文件(link file)，则复制连接文件属性而非文件本身
-f:强制(force)，若有重复或其它疑问时，不会询问用户，而强制复制
-i:若目标文件(destination)已存在，在覆盖时会先询问是否真的操作
-l:建立硬连接(hard link)的连接文件，而非复制文件本身
-p:与文件的属性一起复制，而非使用默认属性
-r:递归复制，用于目录的复制操作
-s:复制成符号连接文件(symbolic link)，即“快捷方式”文件
-u:若目标文件比源文件旧，更新目标文件 