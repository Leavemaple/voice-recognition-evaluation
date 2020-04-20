# -*- coding: utf-8 -*-
import time
import tkinter as tk

def updatetimer():
    timer=time.strftime("%H:%M:%S")
    timelabel.configure(text=timer)
    timelabel.after(1000,updatetimer)
    return timer

on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('已录音完成')


    else:
        on_hit = False
        var.set('')
        b.configure(text="录音")


def main():
    window.mainloop()

window = tk.Tk()
window.title('语音测评')
window.geometry('500x300')

timelabel = tk.Label(window,width=10,font=('Arial', 20))
timelabel.pack()
timelabel.after(1000,updatetimer)

t = tk.Text(window, height=8,show = None)
t.pack()

var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, font=('Arial', 12), width=20, height=1)
l.place(x=250, y=200, anchor='s')

b = tk.Button(window, text='录音', font=('Arial', 12), width=10, height=1, command=hit_me)
b.place(x=250, y=250, anchor='s')



if __name__ == '__main__':
    main()