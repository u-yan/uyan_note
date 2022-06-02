- 第一行`#!/bin/bash` 带表你选择的解释器
- `source .bash_profile`， `~\.bash_profile`是用户的环境变量，所以修改的时候要`source .bash_profile`才能生效
- `echo $var`的时候千万不能忘记`$` 符号。
- 检测`bash`脚本是否有问题 `bash -n demo.sh`如果没有结果，就代表脚本没问题。
- `[set]Var_Name=Value` 全局变量的赋值，一般情况下使用全局变量即可，是作用于本脚本所有位置。
- `read`命令可读取用户输入，`-p`参数可以在后面添加提示`text`来让用户输入，然后变量放在最后。
- 统计文件数量`ls -l |grep "^-"|wc -l \\统计当前文件夹里文件数量`
- 
- 提取文件名`name+=$(basename $path)`
- 函数的创建
  - 

![./res/img/截屏2022-05-25 下午5.49.49.png](./res/img/截屏2022-05-25 下午5.49.49.png)

