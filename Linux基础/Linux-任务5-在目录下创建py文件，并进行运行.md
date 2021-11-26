

# 在目录下创建py文件，并进行运行


在Python中有一个内置库os，是一个系统接口库，operating system interfaces。在linux系统中处理数据、运行脚本的时候，经常会操作文件和目录，所以os库就是起这个作用，对于固定逻辑的文件、目录的操作，都可以写成脚本的形式。


下面就介绍几种常用方法：

1. getcwd
   获取当前目录路径

   ```python
    [I have no name!@i-7lo31rsr Ceallach_Shaw]$pwd
    /home/coggle/Ceallach_Shaw
    [I have no name!@i-7lo31rsr Ceallach_Shaw]$vi os_test.py

   ```
   新建py文件，引入os模块，利用getcwd方法，打印当前路径。注意：这里用的vi，所以退出保存的方法是，esc退出insert模式，切换到命令行模式，输入wq，回车保存。（后文对vi的使用不再赘述了，忘记了的同学就翻阅上一篇文章 [Linux基础（一）](https://mp.weixin.qq.com/s/KjvEMM_dKfI5T9WxYyHl2w)
   ```python
   import os

   print(os.getcwd())
   ```
   命令行下，运行py文件，打印的路径与当前路径一致。
   ```python
    [I have no name!@i-7lo31rsr Ceallach_Shaw]$python3 os_test.py 
    
    /home/coggle/Ceallach_Shaw
   ```

2. 