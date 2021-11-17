# 在目录下使用vi或vim编辑文件

在linux里的文本编辑，需要掌握一些快捷键操作。一般使用vim 、nano

## nano
nano相对vim来说，更容易上手一些，没有vim那些神奇的操作（用的6的人，感觉ta在变魔术）

1. 新建、保存文件

在底下有很多可选快捷键提醒（这就很友好了，一看就会~），`倒三角`就是`Ctrl`的意思
```shell
nano test.py #创建文件
```
![](https://inews.gtimg.com/newsapp_ls/0/14186353928/0.png)

随便编辑，然后保存，会提醒你是否保存（直接按Y，就算是按了Y，还会继续提醒你是否取消之类的选项，非常贴心啊~~），然后enter保存。
[![I5Ir0P.png](https://z3.ax1x.com/2021/11/17/I5Ir0P.png)](https://imgtu.com/i/I5Ir0P)

2. 常用快捷键

Ctrl + G ：取得线上说明（help），比较有用 （相当于指令说明书）。

[![I5o2E6.md.png](https://z3.ax1x.com/2021/11/17/I5o2E6.md.png)](https://imgtu.com/i/I5o2E6)

Ctrl + X ：`离开naon软件，如果有修改则会提示保存`。

Ctrl + R ：从其他文件读入数据，可以将某个文件的内容贴在本文件中（有意思的功能），**but 需要自己手动输入绝对路径，而且是不带路径提醒的输入**，有些麻烦了（文件名都想不起叫啥），需多开窗口或者提前复制好需要导入文件的绝对路径。

[![I5T4oV.md.png](https://z3.ax1x.com/2021/11/17/I5T4oV.md.png)](https://imgtu.com/i/I5T4oV)


Ctrl + C ：说明当前光标所在处的行数与列数等信息。

[![I5TsJS.md.png](https://z3.ax1x.com/2021/11/17/I5TsJS.md.png)](https://imgtu.com/i/I5TsJS)

Ctrl + _  ： 可以直接输入行号，光标快速移动到该行。

Alt + M： 可以支持鼠标来移动光标的功能，开关按钮（这个很方便了，对于win过来的用户）。


这里只列举了其中几种很便捷的快捷键，就算是忘记了也不要紧，ctrl+G看看就知道了，非常适合新手“玩家”。


## vi/vim

vim 是最强大的编辑器（不接受反驳）。功能多到你压根就别想记住的那种。

劝退图 ：（可以完全不用鼠标~）
[![I5H13D.md.png](https://z3.ax1x.com/2021/11/17/I5H13D.md.png)](https://imgtu.com/i/I5H13D)

在使用vim的时候，有3种模式
- 命令模式（刚进去就是这个模式）
- 输入模式
- 底线命令模式

1. 命令模式

一进去就是该模式，需要`键入 i 切换到输入模式`，底线出现insert,这个状态下才能编辑内容

在命令模式下，`输入x则是删除光标所在的字符`。

编辑完成后，`esc切换到命令模式下`，输入：，wq，按enter即可保存内容；或者输入q，直接退出编辑，不保存内容。

2. 输入模式

HOME/END，移动光标到行首/行尾

Page Up/Page Down，上/下翻页

ESC，退出输入模式，切换到命令模式

3. 底线命令模式

在命令模式下，键入：即进入底线命令模式

- q 退出程序
- w 保存文件
- wq 保存并退出

3种模式之间的关系和简单使用，如下图所示：

[![I5bbQg.md.png](https://z3.ax1x.com/2021/11/17/I5bbQg.md.png)](https://imgtu.com/i/I5bbQg)

## 简单练习

```shell

nano test.py #新建py文件，输入print语句

#!/usr/bin/env python3

print('Hello World!')

$ python3 test.py  # 运行python文件
Hello World!
```

