

# 在目录下创建文件夹、删除文件夹

## Linux目录结构
1、开局一张图
![](https://inews.gtimg.com/newsapp_ls/0/14182432385/0.png)
不同目录，存放着不同的作用的文件。

2、部分目录解释

- /bin 
存放着经常使用的命令
- /boot
启动linux的文件（别乱删，不然gg）
- etc
系统管理需要的配置文件
- /home
用户的主目录，比如说新建一个普通用户，该用户的目录入口就在这
/lib
系统最基本的动态连接库
- /opt
安装软件所在的目录（安装的软件都放这）
- /tmp 
临时目录
- /usr 
（非常重要）应用程序和文件都在这，类似于 windows 下的 program files 目录
- /usr/bin
系统用户使用的应用
- usr/sbin
超级用户使用的比较高级的管理程序和系统守护程序

> 在 Linux 系统中，有几个目录是比较重要的，平时需要注意不要误删除或者随意更改内部文件。
>
>/etc： 上边也提到了，这个是系统中的配置文件，如果你更改了该目录下的某个文件可能会导致系统不能启动。
>
>/bin, /sbin, /usr/bin, /usr/sbin: 这是系统预设的执行文件的放置目录，比如 ls 就是在 /bin/ls 目录下的。
>
>/bin, /usr/bin 是给系统用户使用的指令（除root外的通用户），而/sbin, /usr/sbin 则是给 root 使用的指令。
>
>/var： 这是一个非常重要的目录，系统上跑了很多程序，那么每个程序都会有相应的日志产生，而这些日志就被记录到这个目录下，具体在 /var/log 目录下，另外 mail 的预设放置也是在这里.
>

参考链接：https://www.runoob.com/linux/linux-system-contents.html


## Linux 文件与目录管理

1、绝对路径 、相对路径

- 绝对路径
说人话就是，“非常完整”的路径。
这里指的就是绝对路径，当前位置的完整路径（从根目录/开始）
![](https://files.catbox.moe/7viwxj.png)

- 相对路径
指的就是，相对于当前位置的路径。
比如，现在从jims文件切到kuan文件下去，用..代表上一级目录的完整目录（就不用写/home/coggle/kuan这么长了）
![](https://inews.gtimg.com/newsapp_ls/0/14182761484/0.png)

2、处理目录的常用命令

- ls 
列出目录及文件名
- cd 
切换目录

- pwd
显示当前目录

- mkdir
创建目录

- rmdir 
删除一个空目录

- cp 
复制目录

- rm 
删除文件/目录

- mv 
移动文件/目录,还能修改文件/目录

另外，使用 man [命令] 来查看各个命令的使用文档，如 ：man cp

3、练习

```shell

$ pwd  # 当前目录
/home/coggle
$ mkdir Ceallach_Shaw #创建文件夹A
$ cd Ceallach_Shaw/ #进入文件夹A
$ pwd 
/home/coggle/Ceallach_Shaw
$ mkdir coggle # 在A下创建文件夹B
$ ls
coggle
$ cd coggle/ # 进入文件夹B
$ mkdir txt  # 在文件夹B下创建txt文件
$ ls
txt
$ rm -rf txt # 删除txt
$ ls
$ pwd
/home/coggle/Ceallach_Shaw/coggle
$ cd .. # 返回上一级目录
$ rm -rf coggle/ # 删除B文件夹
$ cd ..
$ rm -rf Ceallach_Shaw/ # 删除A文件夹
$ ls # 查看当前目录
4C79	LonelVino	  LonelVino.zip  dongyu  future_y  jaychou_lyrics.txt  lipufei	 myxc.tar.gz   s2.sh		t	  wordpress.zip
BelaF	LonelVino.tar	  Sunny		 elics	 gzg	   jims		       myxc	 myxc.zip      selenim.py.save	test5.py
Janayt	LonelVino.tar.gz  dengniewei	 foldit  hgw	   kuan		       myxc.tar  panda_zhangs  shell_0.sh	turkeymz
$ 

```


