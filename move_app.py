# -*- coding: utf-8 -*-

import tkinter as tk
import os
import pyperclip
import time
import sys
app_path = ""
external_path = ""
#窗口
window=tk.Tk()
window.title('MacOS软件迁移至外置硬盘')
width = 600
height = 300
scr_width = 1920
scr_height = 1080

def set_window_center(window,width=None,height=None):
  '''窗口屏幕居中
	屏幕缩放: 自适应缩放率
  '''
  global scr_height,scr_width
  if width == None:
    width=600
  if height== None:
    height=300
  scr_width = window.winfo_screenwidth()
  scr_height = window.winfo_screenheight()
  size_position = f'{width}x{height}+{(scr_width-width-16)//2}+{(scr_height-height-32)//2}'
  window.geometry(size_position)

set_window_center(window)

# 画布放置图片
# canvas=tk.Canvas(window,height=300,width=500)
# imagefile=tk.PhotoImage(file='qm.png')
# image=canvas.create_image(0,0,anchor='nw',image=imagefile)
# canvas.pack(side='top')
  
# 软件原路径
tk.Label(window,text='请输入软件原路径:').place(x=100,y=75)
tk.Label(window,text='请输入外置硬盘的路径:').place(x=100,y=140)
var_app_path=tk.StringVar()
entry_app_path=tk.Entry(window,textvariable=var_app_path)
entry_app_path.place(x=100,y=100,width=400)
def get_app_path():
  app_path = pyperclip.paste()
  entry_app_path.delete(0,tk.END)
  entry_app_path.insert(0,app_path)


button_get_app_path = tk.Button(window,text="从剪贴板获取",command=get_app_path)
button_get_app_path.place(x=380,y=70)
# 外置硬盘路径
var_external_path=tk.StringVar()
entry_external_path=tk.Entry(window,textvariable=var_external_path)
entry_external_path.place(x=100,y=170,width=400)
def get_external_path():
  external_path = pyperclip.paste()
  entry_external_path.delete(0,tk.END)
  entry_external_path.insert(0,external_path)
button_get_external_path = tk.Button(window,text="从剪贴板获取",command=get_external_path)
button_get_external_path.place(x=380,y=140)

# 移动操作
def confirm_move_app():
  app_path = entry_app_path.get()
  external_path = entry_external_path.get()
  app_name = app_path.split("Applications/")[1].strip().replace(" ","\ ")
  move_command = "sudo mv " + app_path.replace(" ","\ ") + " " + external_path
  connect_command = "ln -s " + external_path + "/" + app_name +" /Applications/"
  print("请输入当前账户密码(本操作需要管理员权限):")
  os.system(move_command)
  os.system(connect_command)
  print(move_command)
  print(connect_command)
  print("移动完成,3s后自动退出")
  time.sleep(3)
  sys.exit(0)

button_move_app = tk.Button(window,text="开始移动",command=confirm_move_app)
button_move_app.place(x=405,y=200)

# 主循环
window.mainloop()