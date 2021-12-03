[TOC]

# 在目录下创建py目录，并进行import导入

## 模块化

有些时候，我们需要借用写好的脚本中的函数或类，就需要在不同脚本之间进行交互，而被“借用”的py文件，就称为`模块`，与内置模块使用方法一致。

方法就是，在另外一个脚本里导入模块即可，和日常import区别不大（比较简单，不赘述）

## __name__属性

重点说下__name__属性

一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

```python
#!/usr/bin/python3
# Filename: using_name.py

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
```

输出结果：
1、运行文件本身的时候，则自己在运行
```shell
$ python using_name.py
程序自身在运行
```

2、导入模块的时候，则代表被引入
```python
>>> import using_name
我来自另一模块
```

 每个模块都有一个__name__属性，`当其值是" __main__ "时，表明该模块自身在运行，否则是被引入。`

## 练习

1、affairs.py代码完成https://mirror.coggle.club/dataset/affairs.txt文件的读取；

2、test6.py可以进行命令行解析，输出affairs.txt前10行内容

affairs.py ：

```python
import pandas as pd

def read():
	df = pd.read_csv('https://mirror.coggle.club/dataset/affairs.txt')
	return df
```
test6.py :

```python
import sys
import affairs
 
arg = sys.argv[1]
print(affairs.read()[:int(arg)])
```

`sys.argv`传参使用可参考上一篇的笔记[Linux基础（三）](https://mp.weixin.qq.com/s/Td3ZzOajZ2ts_XRwIXByKQ)

![20211204000530](https://s2.loli.net/2021/12/04/oVtgjMvkJw47BSc.png)


