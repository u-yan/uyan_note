# git分布式版本控制系统



##### 1. git 本地修改



###### 1.1更新git



```git update-git-for-windows```



基本语法



```git config --global user.name name```	 配置用户名



```git config --global user.email email``` 配置用户邮箱



```git config --list``` 查看配置，如果是windows那么在用户里有一个```.gitconfig```文件



###### 1.2初始化本地目录



```git init```是把当前目录初始化





```git status```是查看当前状态





由于没法使用vim是因为不在环境变量，那么就找到了git的目录，

 那么直接添加进入



重启一下windows terminal就可以了。



###### 1.3 添加暂存区



当在git目录修改文件后，修改的文件还未添加到暂存区，查看```git status```时是这个样子







```git add hello.txt```



添加之后，







从暂存区里去除







###### 1.4提交本地库



```git commit -m "commit_name```提交本地库





```git reflog```是精简版的log,```git log```是复杂版的log。





###### 1.5暂存区的修改



如果直接修改```hello.txt```文件，再次查看的时候，会是![image-20220510211707878](C:\Users\92800\AppData\Roaming\Typora\typora-user-images\image-20220510211707878.png)



再次提交暂存区，然后提交版本，







###### 1.6历史版本



根据reflog简略版本号，可以用```git reset --hard xxx```来进行到达你想要的版本，然后也会生成你跳转的信息，![image-20220510213704786](C:\Users\92800\AppData\Roaming\Typora\typora-user-images\image-20220510213704786.png)



```.git/HEAD```存储了当前版本的版本号的文件的位置，然后这个位置存储了当前版本号





##### 2. git分支



###### 2.1 查看分支



```git branch -v```





###### 2.2 创建分支





###### 2.3 切换分支



```git checkout xxx```切换到xxx所在的分支







\###### 2.4 合并分支



```git merge xxxx```



注意要把b分支加到a分支上，要在a分支写命令



###### 2.5 冲突合并





这个时候要自己修改然后commit是commit全部



# GitHub



##### 拉取和提交远程仓库



```git remote -v```查看本地所有git远程库别名



```git remote add xxx https://xxx```给远程库创建别名-

提交远程库的时候，```git push 别名 当前分支名```



```
MaterialDialog materialDialog = MaterialDialogHelper.materialDialog(BindSettingActivity.this, "title", "content", "first", "second", "thirdText",buttonCallback, true);
```



如果别人修改过了，那么要```git pull xxx master```拉取到本地。





