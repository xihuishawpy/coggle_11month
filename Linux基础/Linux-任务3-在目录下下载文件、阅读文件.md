
# 在目录下下载文件、阅读文件

## 下载文件
一般情况下，都是用**wget**,从指定的URL下载文件，最大的优点就是比较稳定，网络适应性强（网速慢，也能稳定下载），就算是停电断网了，也能从历史下载位置继续下载。

1.1 单文件下载
```shell
wget http://www.linuxde.net/testfile.zip
```

1.2 下载并且以指定文件名保存

如下动态页面，如果不指定文件名保存，则保存为错误的文件名（download.aspx?id=1080）
```shell
wget -O wordpress.zip http://www.linuxde.net/download.aspx?id=1080
```

1.3 断点续传

-C ：代表重新启动下载中断的文件
```shell
wget -c http://www.linuxde.net/testfile.zip
```

1.4 后台下载

-b :下载大文件，后台进行下载
```shell
wget -b http://www.linuxde.net/testfile.zip

tail -f wget-log #查看进度
```


1.5 下载多个文件

先保存多个下载链接至txt文件，然后加上-i参数依次下载

```shell
cat > filelist.txt
url1
url2
url3
url4


wget -i filelist.txt
```

参考链接：https://www.cnblogs.com/pretty-ru/p/10936023.html



## 阅读文件

> cat : 从第一行开始显示文件内容
> 
> tac :  从最后一行开始显示
> 
> nl :显示行号
> 
> more : 一页一页显示文件内容
> 
> less : 往前翻页
> 
> tail : 只看结尾几行

2.1 cat 

-n : 打印行号(空白行也打印出来)

![](https://files.catbox.moe/jrh5nf.png)

-b : 打印行号（不打印空白行）

![](https://files.catbox.moe/li6g0d.png)


2.2 tac 

反着打印

![](https://files.catbox.moe/63ek71.png)

2.3 nl

在打印行号的场景下，cat 和 nl二选一（我选cat)

![](https://files.catbox.moe/slhmk6.png)


2.4 more

- 空格键（Space） ：向下翻一页

- Enter ：向下滚动一行


- :f ：立刻显示文件名以及目前显示的行数；

- q ：立刻离开more，不再显示该文件内容

- b或[ctrl]-b：代表往回翻页，不过这操作只对文件有用，对管道无用。

2.5 less

翻页的场景，more、less二选一（我选less），直接能替代more

- 空格键（Space） ：向下翻一页

- [PageDown]：向下翻动一页

- [PageUp]：向上翻动一页

- ?字符串：向上查询“字符串”这个关键字；

- q ：代表立刻离开less，不再显示该文件内容

2.6 tail

-n 20 : 最后20行
-n +100 : 100行以后的行
注：head也有类似参数，参数含义和tail正好相反，-n 20代表前20行，-n -100代表除了最后100行都打印

### 练习

```shell
$ pwd
/home/coggle
$ mkdir Ceallach_Shaw # 创建文件夹
$ cd Ceallach_Shaw/
$ mkdir coggle # 在Ceallach_Shaw文件夹下创建coggle
$ ls
coggle

$ wget https://mirror.coggle.club/dataset/affairs.txt
--2021-11-16 00:48:38--  https://mirror.coggle.club/dataset/affairs.txt
Resolving mirror.coggle.club (mirror.coggle.club)... 113.229.252.249, 2408:8731:c001:2:3::3fb
Connecting to mirror.coggle.club (mirror.coggle.club)|113.229.252.249|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 92161 (90K) [text/plain]
Saving to: ‘affairs.txt’

affairs.txt                             100%[============================================================================>]  90.00K  --.-KB/s    in 0.04s   

2021-11-16 00:48:38 (2.14 MB/s) - ‘affairs.txt’ saved [92161/92161]

$ ls
affairs.txt  coggle


$ cat -n affairs.txt # 共6367行
  ....................
  6363	4,22,2.5,0,3,0
  6364	5,22,2.5,0,2,0
  6365	5,32,13,2,3,0
  6366	4,32,13,1,1,0
  6367	5,22,2.5,0,2,0$ 

```

参考链接：https://www.cnblogs.com/jixp/p/10833801.html


