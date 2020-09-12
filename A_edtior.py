# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 09:54:31 2020

@author: Lenovo
"
"""
'''
文章编辑器
功能：子函数实现
1静态存储一页文章，每行最多不超过80个字符，共N行,线性表存储
2统计整篇文章总字数，英文字母数，空格数，输出结果
3统计某一字符串在文章中出现的次数，输出结果
4删除某一子串，并将后面的字符前移
输入数据的形式和范围：可以输入大写、小写的英文字母、任何数字及标点符号。
输出形式：分4行输出"全部字母数"、"数字个数"、"空格个数"、"文章总字数"；输出删除某一字符串后的文章
'''
import tkinter
import tkinter.messagebox
import tkinter.filedialog

# 弹框函数
def MesBox(mesg):
    result = tkinter.messagebox.askokcancel(title = "提示",message = mesg) ##例mesg = '保存成功'
    print(result)

# 保存函数（文件操作选择、写入
def saveF():
    content=filemesg.get(0.0,tkinter.END)
    save_file = tkinter.filedialog.askopenfilename(
		filetypes=[('所有文件','*.*'),('文本文档','*.txt')])  #弹出文件对话框，设置选择文件的类型
    if save_file:   			#如果用户选择了文本，则进行打开       
        with open(save_file,'w',encoding='utf-8') as f:
            f.write(content)
        mesg = '保存成功'
        MesBox(mesg)
        
# 打开函数（文件操作选择、读取
def openF():
	input_file = tkinter.filedialog.askopenfilename(
		filetypes=[('所有文件','*.*'),('文本文档','*.txt')])  #弹出文件对话框，设置选择文件的类型
	
	if input_file:   			#如果用户选择了文本，则进行打开
		with open(input_file,'r',encoding='utf-8') as _file:
                    content=_file.read()
                    filemesg.delete(0.0,tkinter.END)
                    filemesg.insert(tkinter.END,content)
# 获取并输出函数（获取输入框内容输出结果
def getM():
    mes=results5.get()
    contents=filemesg.get(0.0,tkinter.END)
    mes_count=contents.count(mes)
    results5.delete(0,tkinter.END)
    results5.insert(tkinter.END,"出现次数为"+str(mes_count))
# 对打开的文件进行总字数统计
def countAll():
    contents=filemesg.get(0.0,tkinter.END)
    results4.delete(0,tkinter.END)
    contents_c=contents.rstrip()
    results4.insert(tkinter.END,len(contents_c))
# 对打开的文章进行空格数统计
def countSpace():
    contents=filemesg.get(0.0,tkinter.END)
    results3.delete(0,tkinter.END)
    i=contents.count(' ',0,len(contents))
    results3.insert(tkinter.END,i) 
# 对打开的文章进行字母数统计
def countApl():
    a=0
    Apl=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Apll=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    contents=filemesg.get(0.0,tkinter.END)
    results1.delete(0,tkinter.END)
    contents_list=list(contents)
    for i in range(len(contents_list)):
        if contents_list[i] in Apl or i in Apll:     
            a+=1
    results1.insert(tkinter.END,a)
# 对打开的文章进行数字数统计
def count_num():
    b=0
    contents=filemesg.get(0.0,tkinter.END)
    results2.delete(0,tkinter.END)
    contents_list=list(contents)
    num=['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(contents_list)):
        if contents_list[i] in num:
            b+=1
    results2.insert(tkinter.END,b)

# 创建主窗口
root = tkinter.Tk()
# 设置窗口大小及标题
root.minsize(800,800)
root.title("文章编辑器")


# 创建菜单栏
f = tkinter.Menu(root)
root['menu'] = f
# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = tkinter.Menu(f,tearoff = False)
filemenu.add_command(label="打开",accelerator = 'Ctrl+O',command=openF)
filemenu.add_command(label="保存",accelerator = 'Ctrl+S',command=saveF)
filemenu.add_separator()
filemenu.add_command(label="退出")
f.add_cascade(label="文件", menu=filemenu) 
# 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
editmenu = tkinter.Menu(f,tearoff = False)
editmenu.add_command(label="剪切",accelerator = 'Ctrl+X')
editmenu.add_command(label="拷贝",accelerator = 'Ctrl+C')
editmenu.add_command(label="粘贴",accelerator = 'Ctrl+V')
f.add_cascade(label="帮助", menu=editmenu)
# 创建放置一个多行文本框用以显示所打开的文章
filemesg = tkinter.Text(root,width=160,height = 40,bd=2)
filemesg.pack() ##设置大小以保证每行输出80字
# 创建放置一个单行文本框用以显示统计结果
label1=tkinter.Label(root,text='该文章的字母数为').place(x=250,y=530)
results1 = tkinter.Entry(root,width=10,bd=2)
results1.place(x=420,y=530)
bt1=tkinter.Button(root,text="字母数",command=countApl).place(x=500,y=530)
# 创建放置一个单行文本框用以显示统计结果
label2=tkinter.Label(root,text='该文章的数字数为').place(x=250,y=560)
results2 = tkinter.Entry(root,width=10,bd=2)
results2.place(x=420,y=560)
bt2=tkinter.Button(root,text="数字数",command=count_num).place(x=500,y=560)
# 创建放置一个单行文本框用以显示统计结果
label3=tkinter.Label(root,text='该文章的空格数为').place(x=250,y=590)
results3 = tkinter.Entry(root,width=10,bd=2)
results3.place(x=420,y=590)
bt3=tkinter.Button(root,text="空格数",command=countSpace).place(x=500,y=590)
# 创建放置一个单行文本框用以显示统计结果
label1=tkinter.Label(root,text='该文章的总字数为').place(x=250,y=620)
results4 = tkinter.Entry(root,width=10,bd=2)
results4.place(x=420,y=620)
bt4=tkinter.Button(root,text="总字数",command=countAll).place(x=500,y=620)
# 创建放置一个单行文本框用以显示统计结果
label5=tkinter.Label(root,text='请输入要查询的字符串：').place(x=650,y=550)
results5 = tkinter.Entry(root,width=15,bd=2)
results5.place(x=690,y=580)
bt5=tkinter.Button(root,text="统计",command=getM).place(x=800,y=575)
# 事件循环
root.mainloop()




