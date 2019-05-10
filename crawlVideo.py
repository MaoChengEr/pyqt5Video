import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askdirectory
from threading import Event, Thread
from tkinter import Tk, ttk
from urllib.request import urlretrieve
import requests
import sys
import cv2

def selectPath():
    path_ = askdirectory()
    path.set(path_)
    #http://video.shsongyi.cn/webvideo/liupu/jishu/fadongji.mp4（地址1）
    #http://video.shsongyi.cn/webvideo/liupu/jishu/touming.mp4(地址2)
    #http://video.shsongyi.cn/webvideo/liupu/jishu/gongzhuang.mp4(地址3)

#视频或者歌曲的下载
# def scrapyVideo():
#     url = "http://video.shsongyi.cn/webvideo/liupu/jishu/fadongji.mp4"
#     path = "D:/4k图片/1.mp4"
#     # if link_entry.get() == '':
#     #
#     #     # tkinter.messagebox.showerror('wrong!', 'can not get the url or url is null\nplease check the url!')
#     # elif save_entry.get() == '':
#     #
#     #     # tkinter.messagebox.showerror('wrong!', 'can not get the path or path is null\nplease check the path!')
#     # else:
#     # url = link_entry.get()
#     filename ='/'+url.strip().split('/')[-1]
#     # path = save_entry.get()
#     response = re.get(url,stream = True).raw.read()  #获取二进制文件
#
#         # full_filename=path+filename
#         # with open(full_filename, 'wb') as file:
#         #     file.write(response)
#             # for chunk in response.iter_content(1024*1024):
#             # file.write(response)

def displayVedio():
    url = link_entry.get()
    name =url.strip().split('/')[-1]
    filename = name.split('.')[0]
    fullname = '/'+filename+choice.get()
    path = save_entry.get()
    full_filename=path+fullname
    cap = cv2.VideoCapture(full_filename)
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

#创建基本视频界面
#创建窗口
def download():
    url = link_entry.get()
        # 尝试请求
    # try:
    #     response = requests.get(url, timeout=20)
    # # 请求失败弹出错误框
    # except:
    #     tkinter.messagebox.showerror('错误!', '请填写url地址\n请求网址失败')
    #     return
    name =url.strip().split('/')[-1]
    filename = name.split('.')[0]
    fullname = '/'+filename+choice.get()
    path = save_entry.get()
    full_filename=path+fullname
    root = progressbar = quit_id = None
    ready = Event()
    def reporthook(blocknum, blocksize, totalsize):
        nonlocal quit_id
        if blocknum == 0: # started downloading
            def guiloop():
                nonlocal root, progressbar
                root = Tk()
                root.withdraw() # hide
                progressbar = ttk.Progressbar(root, length=400)
                progressbar.grid()
                # show progress bar if the download takes more than .5 seconds
                root.after(500, root.deiconify)
                ready.set() # gui is ready
                root.mainloop()
            Thread(target=guiloop).start()
        ready.wait(1) # wait until gui is ready
        percent = blocknum * blocksize * 1e2 / totalsize # assume totalsize > 0
        if quit_id is None:
            root.title('%%%.0f %s' % (percent, full_filename,))
            progressbar['value'] = percent # report progress
            if percent >= 100:  # finishing download
                quit_id = root.after(0, root.destroy) # close GUI

    return urlretrieve(url, full_filename, reporthook)

# download('http://video.shsongyi.cn/webvideo/liupu/jishu/fadongji.mp4','fadongji.mp4')
top = tk.Tk()

# 设置窗口标题和大小
top.title('Scrapy Vedio Version:1.0')
top.geometry('450x180')

# # 设置下载进度条
# tk.Label(top, text='下载进度:', ).place(x=10, y=140)
# canvas = tk.Canvas(top, width=350, height=22, bg="white")
# canvas.place(x=70, y=140)

# 显示下载进度
# def progress():
#     # 填充进度条
#     fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
#     x = 500  # 未知变量，可更改
#     n = 465 / x  # 465是矩形填充满的次数
#     for i in range(x):
#         n = n + 465 / x
#         canvas.coords(fill_line, (0, 0, n, 60))
#         top.update()
#         time.sleep(0.02)  # 控制进度条流动的速度
#
#     # 清空进度条
#     fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
#     x = 500  # 未知变量，可更改
#     n = 465 / x  # 465是矩形填充满的次数

    # for t in range(x):
    #     n = n + 465 / x
    #     # 以矩形的长度作为变量值更新
    #     canvas.coords(fill_line, (0, 0, n, 60))
    #     top.update()
    #     time.sleep(0)  # 时间为0，即飞速清空进度条

# btn_download = tk.Button(top, text='启动进度条', command=progress)
# btn_download.place(x=400, y=160)

# 版本说明
# version = tk.Label(top, text='version:1.0')
# version.pack()

# # 默认存储格式设置
# choice = tk.StringVar()
# choice.set('.png')

# # 开始抓取按钮
# button = tkinter.Button(top, text="start scrapy images")
# button.pack()

# 网站地址
lint_text = tk.StringVar()
link_add = tkinter.Label(top, text='scrapy url:')
link_add.place(x=10,y=10)

# 网站地址输入
link_entry = tkinter.Entry(top,textvariable=lint_text, width=50)
lint_text.set("http://video.shsongyi.cn/webvideo/liupu/jishu/touming.mp4")
link_entry.place(x=80,y=10)


# 选择地址按钮
path_choose = tkinter.Button(top, text='choose path',command=selectPath)
path_choose.place(x=185, y=35)


# 保存地址
save_add = tkinter.Label(top, text='save path:')
save_add.place(x=10,y=70)


# 输入地址
path=tk.StringVar()
save_entry = tkinter.Entry(top, width=50, textvariable=path)
save_entry.place(x=80, y=70)
path.set(sys.path[0])

#播放视频
play_vedio = tkinter.Button(top, text='play video',command=displayVedio)
play_vedio.place(x=225, y=140)

#保存视频
path_save = tkinter.Button(top, text='save file',command=download)
path_save.place(x=145, y=140)

#保存格式
choice = tk.StringVar()
choice.set(".mp4")
choice_label = tkinter.Label(top,text='保存格式')
choice_label.place(x=10,y=100)
choose_jpg = tkinter.Radiobutton(top, text='.mp4', variable=choice, value='.mp4')
choose_jpg.place(x=80, y=100)
choose_jpg = tkinter.Radiobutton(top, text='.wma', variable=choice, value='.wma')
choose_jpg.place(x=150, y=100)
choose_jpg = tkinter.Radiobutton(top, text='.rmvb', variable=choice, value='.rmvb')
choose_jpg.place(x=220, y=100)
choose_jpg = tkinter.Radiobutton(top, text='.avi', variable=choice, value='.avi')
choose_jpg.place(x=290, y=100)
choose_jpg = tkinter.Radiobutton(top, text='.3gp', variable=choice, value='.3gp')
choose_jpg.place(x=360, y=100)

top.mainloop()