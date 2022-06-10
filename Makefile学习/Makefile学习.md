# Makefile学习
## Getting Started
`Makefile`是为了解决各种依赖问题，就像`java`里的`Gradle`等，都是为了防止重复编译未修改的依赖。
### First Running
创建文件名为`Makefile`然后直接运行命令`make`即可。
### Makefile 语法
```
targets: prerequisites
	command
	command
	command
```
- The targets are file names, separated by spaces. Typically, there is only one per rule.
- The commands are a series of steps typically used to make the target(s). These need to start with a tab character, not spaces.
- The prerequisites are also file names, separated by spaces. These files need to exist before the commands for the target are run. These are also called dependencies
### 变量
用`$()`或者`${}`表示字符串，然后`$@`是当前所要形成的文件，即语法中的`targets`，`$<`是自己依赖的，即语法中的`prerequisites`。