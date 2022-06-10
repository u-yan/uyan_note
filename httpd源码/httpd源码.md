# 打包文件Makefile

文件很短，就是首先编译`httpd.c`然后参数就是普通的`-g -W -Wall -o`不过加了一个线程（存疑）`-lpthread`，然后就是把`httpd.c`编译成`httpd`。
```
httpd: httpd.c
	gcc -g -W -Wall $(LIBS) -o $@ $<    
