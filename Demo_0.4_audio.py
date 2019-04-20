from tkinter import *
import tkinter as tk
import csv
from PIL import Image, ImageTk
import time
import numpy as np
from pyaudio import PyAudio,paInt16
import wave
import json
import urllib.request
import pycurl

def show_images():
    global Code, Old_Code
    global item_number, item_price, item_name

    photo_dir = item_number + '.gif'
    Image_of_water = Image.open(photo_dir)
    Tkimage = ImageTk.PhotoImage(Image_of_water)
    imgLabel = tk.Label(root, image=Tkimage)  # 把图片整合到标签类中
    imgLabel.grid(column=2, row=1)

    # 显示价格二维码
    print('item_price:' + item_price)
    if (item_price == '3'):
        price_pay = tk.Label(root, text='\n请扫描下方二维码付款\n', font=("宋体", 15), bg="#AAAABB", fg="white")
        price_pay.grid(column=3, row=0)
        photo_price_dir = '3yuan.gif'
        image_of_price = Image.open(photo_price_dir)
        Tkimage_price = ImageTk.PhotoImage(image_of_price)
        imgLabel_price = tk.Label(root, image=Tkimage_price)
        imgLabel_price.grid(column=3, row=1)
    elif (item_price == '4'):
        price_pay = tk.Label(root, text='\n请扫描下方二维码付款\n', font=("宋体", 15), bg="#AAAAAA", fg="white")
        price_pay.grid(column=3, row=0)
        photo_price_dir = '4yuan.gif'
        image_of_price = Image.open(photo_price_dir)
        Tkimage_price = ImageTk.PhotoImage(image_of_price)
        imgLabel_price = tk.Label(root, image=Tkimage_price)
        imgLabel_price.grid(column=3, row=1)
    else:
        photo_price_dir = 'default_price.gif'
        image_of_price = Image.open(photo_price_dir)
        Tkimage_price = ImageTk.PhotoImage(image_of_price)
        imgLabel_price = tk.Label(root, image=Tkimage_price)
        imgLabel_price.grid(column=3, row=1)
        # print("二维码显示成功！！")
    # print("图片显示成功！！\n"
    #       "第一次")
    root.mainloop()

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
    global  price, name
    global Code
    global item_number, item_price, item_name

    # print("进入show_information函数")
    price = tk.Label(root, text='\n\n'+item_price+' Yuan', font=("Times", 20),fg='blue',compound='center')
    price.grid(column=1, row=0)
    # print("show_information函数price："+item_price)
    name=tk.Label(root,text='\n\n'+item_name,font=("Times",20),fg='blue')
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
        #print(row)
        if (Code in row[0]) :
            item_number= str(i_row)
            item_name = str(row[1])  # 匹配成功则输出相关信息
            item_price=str(row[2])
            #返回商品序号，price，name
        i_row = i_row + 1

#根据语音录入的文字查找
def scan_the_item_by_name(voice_result):
    global Code
    global item_number, item_price, item_name
    # ['\ufeffcode', 'name', 'price']
    # ['6921168509256 ', '农夫山泉', '3']
    # ['6931487800156 ', '统一冰红茶', '4']
    i_row = 0  # 计数变量，用于确定条码所在行
    Iterms_csv = csv.reader(open('Iterms.csv', 'r', encoding='utf-8'))
    item_number, item_price, item_name = 'Noitem', '***', '***'
    for row in Iterms_csv:  # 循环扫描文件中’code‘一列
        #print(row)
        if (row[1] in voice_result):
            item_number= str(i_row)
            item_name = str(row[1])  # 匹配成功则输出相关信息
            item_price=str(row[2])
            #返回商品序号，price，name
        i_row = i_row + 1

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
    price_pay.grid_remove()

    Old_Code=Code
    print('Code--{}'.format(Code))
    if len(Code) == 13:
        clean_the_input()
        #显示商品价格，名称
        scan_the_iteam()

        show_information()
        #显示图片，二维码
        show_images()

    else:
        item_number, item_price, item_name = 'Noitem', '***', '***'
        clean_the_input()
        show_information()
        show_images()
def clean_the_input(event=None):
    time.sleep(1)
    entry_window.delete(0,END)


NUM_SAMPLES = 2000
framerate = 16000
channels = 1
sampwidth = 2
#record time
RECORD_SECONDS = 4

def save_wave_file(filename, data):
  '''save the date to the wav file'''
  wf = wave.open(filename, 'wb')
  wf.setnchannels(channels)
  wf.setsampwidth(sampwidth)
  wf.setframerate(framerate)
  wf.writeframes(b''.join(data))
  wf.close()

def record_button(root,label_text,button_text,button_func):
    '''''function of creat label and button'''
    #label details

    recordLabel = tk.Label(root, text=label_text, font=("黑体", 12), relief="sunken", borderwidth=5)  # 左对齐
    recordLabel.grid(column=0, row=3)
    #label details
    button = Button(root,bg="red")
    button['text'] = button_text
    button['command'] = button_func
    button.grid(column=1, row=3)

#
def record_wave():
  #open the input of wave
  global token
  global voice_result

  pa = PyAudio()
  stream = pa.open(format = paInt16, channels = 1,
          rate = framerate, input = True,
          frames_per_buffer = NUM_SAMPLES)
  save_buffer = []

  for i in range(0, int(framerate / 1024 * RECORD_SECONDS)):
    #read NUM_SAMPLES sampling data
    string_audio_data = stream.read(NUM_SAMPLES)
    save_buffer.append(string_audio_data)
    print ('.')
  filename = "1.wav"
  save_wave_file(filename, save_buffer)
  save_buffer = []
  print (filename, "saved")
  use_cloud(token)


def get_token():
    apiKey = "731pSlP7FXDttNwxcerGgUM5"
    secretKey = "l2lXqINb6wPspAF6FSPfVvMgZ1yBVeiF"
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey
    res = urllib.request.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']


def show_res(buf):
    global voice_result
    global item_number, item_price, item_name
    global price, name, imgLabel, imgLabel_noitem, imgLabel_price

    result_raw = str(buf,encoding='utf-8')
    begin_num = result_raw.find('[')+2
    end_num = result_raw.find(']')-2
    voice_result = result_raw[begin_num:end_num]
    print('识别结果————{}'.format(voice_result))
    scan_the_item_by_name(voice_result)

    if item_number != 'Noitem':
        price.grid_remove()
        name.grid_remove()
        imgLabel.grid_remove()
        imgLabel_noitem.grid_remove()
        imgLabel_price.grid_remove()
        show_information()
        show_images()
    else:
        item_number, item_price, item_name = 'Noitem', '***', '***'
        price.grid_remove()
        name.grid_remove()
        imgLabel.grid_remove()
        imgLabel_noitem.grid_remove()
        imgLabel_price.grid_remove()
        show_information()
        show_images()


## post audio to server
def use_cloud(token):
    #  fp = wave.open('test.pcm', 'rb')
    fp = wave.open('1.wav', 'rb')
    #  fp = wave.open('vad_1.wav', 'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    # mac addr
    cuid = "123456"
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/pcm; rate=16000',
        #  'Content-Type: audio/pcm; rate=8000',
        'Content-Length: %d' % f_len
    ]

    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url))  # curl doesn't support unicode
    # c.setopt(c.RETURNTRANSFER, 1)
    c.setopt(c.HTTPHEADER, http_header)  # must be list, not dict
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, show_res)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform()  # pycurl.perform() has no return val





if __name__ =="__main__":
    global token
    global Code,Old_Code
    global item_number, item_price, item_name
    global price, name,imgLabel,imgLabel_noitem,imgLabel_price
    global voice_result
    Code='default'
    Old_Code='default'
    item_number, item_price, item_name = 'default', '***', '***'
    root = Tk(className="Smart Shop")
    center_window(root, 1000, 600)
    root.resizable(width=1200, height=1000)

    #弹窗输入条形码文字设置
    Iterms_csv = csv.reader(open('Iterms.csv', 'r', encoding='utf-8'))
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
        price_pay = tk.Label(root, text='\n请扫描下方二维码付款\n', font=("宋体", 15), bg="#AAAABB", fg="white")
        price_pay.grid(column=3, row=0)
        photo_price_dir = 'default_price.gif'
        image_of_price = Image.open(photo_price_dir)
        Tkimage_price = ImageTk.PhotoImage(image_of_price)
        imgLabel_price = tk.Label(root, image=Tkimage_price)
        imgLabel_price.grid(column=3, row=1)
    #######################loop##############################
    record_button(root, "请说出您需要的商品名称", "录音", record_wave)
    token = get_token()
    root.mainloop()


