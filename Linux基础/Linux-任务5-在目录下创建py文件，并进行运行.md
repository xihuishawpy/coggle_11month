

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

   ```shell
    [I have no name!@i-7lo31rsr Ceallach_Shaw]$python3 os_test.py 
    
    /home/coggle/Ceallach_Shaw
   ```

2. path.abspath('.')
   
   `.`代表当前路径，查看当前目录的绝对路径

   ```python
   import os

   #print(os.getcwd())

   print(os.path.abspath('.'))
    ```

    运行py文件：

    ```shell
    [I have no name!@i-7lo31rsr Ceallach_Shaw]$python3 os_test.py 
    
    /home/coggle/Ceallach_Shaw
    ```

    补充：
    - “.”表示当前目录，也可以用“./”表示；

    - “..”表示上一级目录，也可以用“../”表示；

    - “~” 代表用户的宿主目录；

    - “/”处于Linux文件系统树形结构的最顶端，我们称它为Linux文件系统的root，它是Linux文件系统的入口（参考上一篇文章内容中的目录结构图[Linux基础（一）](https://mp.weixin.qq.com/s/KjvEMM_dKfI5T9WxYyHl2w)）

3. listdir('.')

    列出当前目录下所有文件与目录

    ```python
    import os

    l=os.listdir('.')
    print(l)
    ```

    ![](https://files.catbox.moe/ga84oz.png)

    如果只是需要列出当前目录下的所有目录（文件不需要），则在for循环后面加个条件判断是否为目录 `if os.path.isdir(x)`
    ```python
    [x for x in os.listdir('.') if os.path.isdir(x)]
    ```
    ![](https://files.catbox.moe/h6e85x.png)


4. mkdir 、rmdir

   mkdir-创建目录、rmdir-删除目录

   在当前目录下创建一个dir2的目录：
   
   ```python
   import os

   os.mkdir(os.getcwd()+'/dir2')
   ```
   
   dir2目录创建成功：
    
   ```shell
   [I have no name!@i-7lo31rsr Ceallach_Shaw]$python3 os_test.py 
   [I have no name!@i-7lo31rsr Ceallach_Shaw]$ls
   affairs.txt  coggle  dir  dir2	os_test.py  test.py  test2.txt
   ```

   补充：
   - removedirs，递归删除目录
   - remove，移除文件

5. rename
   
   `文件或者目录`重命名 

   把目录dir2重命名为dir3:
   ```python
   import os

   os.rename('dir2','dir3')
   ```
    ```shell

    [I have no name!@i-7lo31rsr Ceallach_Shaw]$python3 os_test.py 
    [I have no name!@i-7lo31rsr Ceallach_Shaw]$ls
    affairs.txt  coggle  dir  dir3	os_test.py  test.py  test2.txt
    ```

6. path.splitext

    输入文件的绝对路径，得到文件扩展名

    ```python
    import os

    print(os.path.splitext(os.getcwd()+'os_test.py'))
    ```
    输出：

    ('/home/coggle/Ceallach_Shawos_test', '.py')

    列出当前目录下所有.py文件，需加上条件判断是否为文件 `if os.path.isfile(x)`:

    ```python
    l=[x for x in os.listdir('.') 
                if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
    
    print(l)
    ```
    ![](https://files.catbox.moe/we1n6d.png)

## 练习

使用os模块打印/usr/bin/路径下所有以m开头的文件




