from tkinter import *
import tkinter as tk

import csv
from PIL import Image, ImageTk
import time


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
    titleLabel = tk.Label(root, text="Welcome!" + '\n', font=("微软雅黑", 20))
    titleLabel.grid(row=0, columnspan=6, sticky=W + E + N + S)

    priceLabel=tk.Label(root,text="Price",font=("黑体",15),justify="left",fg='black')
    priceLabel.grid(column=0,row=0)
    nameLable=tk.Label(root,text="Information",font=("黑体",15),fg='black')#左对齐
    nameLable.grid(column=0,row=1)
    codeLabel = tk.Label(root, text="Bar Code",font=("黑体",15),relief="sunken",borderwidth=5,fg='black')  # 左对齐
    codeLabel.grid(column=0,row=2)


def show_information():
    global  price, name
    global Code
    global item_number, item_price, item_name

    # print("进入show_information函数")
    price = tk.Label(root, text='\n\n'+item_price+' Yuan', font=("Times", 20),fg='red')
    price.grid(column=1, row=0)
    # print("show_information函数price："+item_price)
    name=tk.Label(root,text='\n\n'+item_name,font=("Times",20),fg='red')
    name.grid(column=1,row=1)

    # print("进入show_information函数name"+item_name)


def scan_the_iteam():
    print("进入scan_the_iteam函数")
    global Code
    global item_number, item_price, item_name
    # ['\ufeffcode', 'name', 'price']
    # ['6921168509256 ', '农夫山泉', '3']
    # ['6931487800156 ', '统一冰红茶', '4']
    i_row = 0
    Iterms_csv = csv.reader(open('Iterms.csv', 'r', encoding='utf-8'))
    for row in Iterms_csv:  # 循环扫描文件中’code‘一列
        print(row)
        if (Code in row[0]) :
            item_number= str(i_row)
            item_name = str(row[1])  # 匹配成功则输出相关信息
            item_price=str(row[2])
            #返回商品序号，price，name
        i_row = i_row + 1

########从录入窗口获取条形码字符串，并清空窗口
def clean_the_code(event=None):
    # print("进入clean_the_code函数")
    global Code
    global item_number, item_price, item_name
    global price, name, imgLabel,imgLabel_noitem,imgLabel_price,price_pay

    Code = e.get()
    price.grid_remove()
    price_pay.grid_remove()
    name.grid_remove()
    imgLabel.grid_remove()
    imgLabel_noitem.grid_remove()
    imgLabel_price.grid_remove()

    print('主函数code={}'.format(Code))

    if len(Code) == 13:
        clean_the_input()
        #显示商品价格，名称
        scan_the_iteam()
        show_information()
        #显示商品图片
        photo_dir = item_number + '.gif'

        Image_of_water = Image.open(photo_dir)
        Tkimage = ImageTk.PhotoImage(Image_of_water)
        imgLabel = tk.Label(root, image=Tkimage)  # 把图片整合到标签类中
        imgLabel.grid(column=2, row=1)

        #显示价格二维码
        #print('item_price:'+item_price)
        if(item_price == '3'):
            price_pay = tk.Label(root, text='\n ***Thank You For Buying*** \n', font=("Times", 15), bg="#AAAABB", fg="white")
            price_pay.grid(column=3, row=0)
            photo_price_dir='3yuan.gif'
            image_of_price= Image.open(photo_price_dir)
            Tkimage_price=ImageTk.PhotoImage(image_of_price)
            imgLabel_price=tk.Label(root,image=Tkimage_price)
            imgLabel_price.grid(column=3,row=1)
        if (item_price == '4'):
            price_pay = tk.Label(root, text='\n ***Thank You For Buying*** \n',font=("Times", 15), bg="#AAAAAA", fg="white")
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
    time.sleep(1)
    entry_window.delete(0,END)


if __name__ =="__main__":
    global Code
    global item_number, item_price, item_name
    global price, name,imgLabel,imgLabel_noitem,imgLabel_price,price_pay
    Code='default'

    item_number, item_price, item_name = 'default', '***', '***'
    root = Tk(className="Smart Shop")
    center_window(root, 900, 600)
    root.resizable(width=800, height=600)

    # background_image = Image.open('background.gif')
    # image_background = ImageTk.PhotoImage(background_image)
    # background_label = tk.Label(root,image=image_background)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #弹窗输入条形码文字设置
    #Iterms = pd.read_csv('Iterms.csv')  # 读取CSV文件
    Iterms_csv = csv.reader(open('Iterms.csv','r',encoding='utf-8'))

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

    ################ get the first default image ##################
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
        price_pay = tk.Label(root, text='\nPleace Scan the Code Below\n', font=("宋体", 15), bg="#AAAABB", fg="white")
        price_pay.grid(column=3, row=0)
        photo_price_dir = 'default_price.gif'
        image_of_price = Image.open(photo_price_dir)
        Tkimage_price = ImageTk.PhotoImage(image_of_price)
        imgLabel_price = tk.Label(root, image=Tkimage_price)
        imgLabel_price.grid(column=3, row=1)
    #######################loop##############################

    root.mainloop()


