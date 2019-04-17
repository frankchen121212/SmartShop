from tkinter import *
import tkinter as tk
import pandas as pd
from PIL import Image, ImageTk

def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()
def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()
def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    # print(size)

    root.geometry(size)
def show_information_guide():
    priceLabel=tk.Label(root,text="商品价格：",font=("黑体",15),justify="left")
    priceLabel.grid(column=0,row=0)
    nameLable=tk.Label(root,text="商品名称：",font=("黑体",15))#左对齐
    nameLable.grid(column=0,row=1)
    codeLabel = tk.Label(root, text="条形码：",font=("黑体",15),relief="sunken",borderwidth=5)  # 左对齐
    codeLabel.grid(column=0,row=2)
    imageLabel = tk.Label(root, text="\n******【商品图片】******\n", font=("黑体", 15), justify="left")
    imageLabel.grid(column=2, row=0)

def show_information():
    global  price ,name
    scan_the_iteam()
    # print("进入show_information函数")
    price = tk.Label(root, text='\n\n'+item_price+' 元', font=("宋体", 20),fg='blue')
    price.grid(column=1, row=0)
    # print("show_information函数price："+item_price)
    name=tk.Label(root,text='\n\n'+item_name,font=("宋体",20),fg='blue')
    name.grid(column=1,row=1)
    # print("进入show_information函数name"+item_name)

def scan_the_iteam():
    # print("进入scan_the_iteam函数")
    global Code
    global item_number, item_price, item_name
    n = 0  # 计数变量，用于确定条码所在行
    for i_code in Iterms['code']:  # 循环扫描文件中’code‘一列
        # print("i_code:  "+str(i_code)+"此时Code="+str(Code))
        if str(i_code) == Code:
            # print("成功返回商品序号，price，name\n")
            # print("商品序号返回为：" +str(n+1))
            # print("price返回为："+str(Iterms.iloc[n,2]))
            # print("name返回为：" + str(Iterms.iloc[n,1]))
            item_number= str(n+1)
            item_price=str(Iterms.iloc[n,2])
            item_name=str(Iterms.iloc[n,1]) # 匹配成功则输出相关信息
            #返回商品序号，price，name
        n = n + 1
    return 'default','***','暂时还未录入商品'  # 返回n,图片查找标识
########从录入窗口获取条形码字符串，并清空窗口
def clean_the_code(event=None):
    # print("进入clean_the_code函数")
    global Code,Old_Code
    global item_number, item_price, item_name
    global price, name, imgLabel,imgLabel_noitem,imgLabel_price
    Code = e.get()
    # if Code is not Old_Code :
        # print("***********清除**********")
    price.grid_remove()
    name.grid_remove()
    imgLabel.grid_remove()
    imgLabel_noitem.grid_remove()
    imgLabel_price.grid_remove()

    Old_Code=Code
    print('Code--{}'.format(Code))
    if len(Code) == 13:
        clean_the_input()
        #显示商品价格，名称
        show_information()
        #显示商品图片
        photo_dir = item_number + '.gif'

        Image_of_water = Image.open(photo_dir)
        Tkimage = ImageTk.PhotoImage(Image_of_water)
        imgLabel = tk.Label(root, image=Tkimage)  # 把图片整合到标签类中
        imgLabel.grid(column=2, row=1)

        #显示价格二维码
        print('item_price:'+item_price)
        if(item_price == '3'):
            price_pay = tk.Label(root, text='\n请扫描下方二维码付款\n', font=("宋体", 15), bg="#AAAABB", fg="white")
            price_pay.grid(column=3, row=0)
            photo_price_dir='3yuan.gif'
            image_of_price= Image.open(photo_price_dir)
            Tkimage_price=ImageTk.PhotoImage(image_of_price)
            imgLabel_price=tk.Label(root,image=Tkimage_price)
            imgLabel_price.grid(column=3,row=1)
        if (item_price == '4'):
            price_pay = tk.Label(root, text='\n请扫描下方二维码付款\n', font=("宋体", 15), bg="#AAAAAA", fg="white")
            price_pay.grid(column=3, row=0)
            photo_price_dir = '4yuan.gif'
            image_of_price = Image.open(photo_price_dir)
            Tkimage_price = ImageTk.PhotoImage(image_of_price)
            imgLabel_price = tk.Label(root, image=Tkimage_price)
            imgLabel_price.grid(column=3, row=1)
            # print("二维码显示成功！！")
        # print("图片显示成功！！\n"
        #       "第一次")
        root.mainloop()
    else:

        item_number, item_price, item_name = 'Noitem', '***', '***'
        clean_the_input()
        show_information()
        photo_dir = item_number + '.gif'
        Image_noitem = Image.open(photo_dir)
        Tkimage_noitem = ImageTk.PhotoImage(Image_noitem)
        imgLabel_noitem = tk.Label(root, image=Tkimage_noitem)  # 把图片整合到标签类中
        imgLabel_noitem.grid(column=2, row=1)
        photo_price_dir = 'default_price.gif'
        image_of_price = Image.open(photo_price_dir)
        Tkimage_price = ImageTk.PhotoImage(image_of_price)
        imgLabel_price = tk.Label(root, image=Tkimage_price)
        imgLabel_price.grid(column=3, row=1)
        root.mainloop()

def clean_the_input(event=None):
    entry_window.delete(0,END)





if __name__ =="__main__":
    global Code,Old_Code
    global item_number, item_price, item_name
    global price, name,imgLabel,imgLabel_noitem,imgLabel_price
    Code='default'
    Old_Code='default'
    item_number, item_price, item_name = 'default', '***', '***'


    root = Tk(className="Smart Shop")
    center_window(root, 800, 600)
    root.resizable(width=1200, height=1000)


    #弹窗输入条形码文字设置
    Iterms = pd.read_csv('Iterms.csv')  # 读取CSV文件
    show_information_guide()

    # 扫码枪扫取数据
    e = StringVar()
    entry_window = Entry(root, validate='key', textvariable=e, width=25)
    entry_window.grid(column=2, row=2)
    entry_window.bind('<Return>', clean_the_code)
    print("主函数中的Code:"+Code+'\n')
    #item_number, item_price, item_name = scan_the_iteam()
    #print("主函数中的价格(main)：" + item_price)
    #print("主函数中的名称(main)：" + item_name)

    ################show图片##################
    if (Code  is 'default'):
        item_number, item_price, item_name = 'default', '***', '***'
        show_information()
        photo_dir = item_number + '.gif'
        Image_of_water = Image.open(photo_dir)
        Tkimage = ImageTk.PhotoImage(Image_of_water)
        imgLabel = tk.Label(root, image=Tkimage)  # 把图片整合到标签类中
        imgLabel.grid(column=2, row=1, sticky=E)
        imgLabel_noitem = tk.Label(root, image=Tkimage)  # 把图片整合到标签类中
        imgLabel.grid(column=2, row=1, sticky=E)
        price_pay = tk.Label(root, text='\n请扫描下方二维码付款\n', font=("宋体", 15), bg="#AAAABB", fg="white")
        price_pay.grid(column=3, row=0)
        photo_price_dir = 'default_price.gif'
        image_of_price = Image.open(photo_price_dir)
        Tkimage_price = ImageTk.PhotoImage(image_of_price)
        imgLabel_price = tk.Label(root, image=Tkimage_price)
        imgLabel_price.grid(column=3, row=1)
    #######################loop##############################
    root.mainloop()


