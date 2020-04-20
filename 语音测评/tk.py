# -*- coding: utf-8 -*-
import time
import tkinter as tk
from threading import Thread
from record import Record

def updatetimer():
    timer=time.strftime("%H:%M:%S")
    timelabel.configure(text=timer)
    timelabel.after(1000,updatetimer)
    return timer

on_hit = False
i = 0
lt=["find","jack","tom","panda","car","work","song","sun","look"]
n =["2","3","4","5","6","7","8","9","10"]

v = Record()

def hit_me():
    global on_hit,i,v
    if on_hit == False:
        on_hit = True
        var.set('已录音完成')
        b.configure(text="下一个")
        voice(v)


    else:
        on_hit = False
        var.set('')
        b.configure(text="录音")
        word.configure(text=lt[i])
        number.configure(text="{}/10".format(n[i]))
        v.testword = lt[i]
        v.SessionId = 'test_'+str(n[i])
        v.RefText = lt[i]
        #print(v.testword,v.SessionId,v.RefText)
        i = i + 1



def voice(v):

    v.WAVE_OUTPUT_FILENAME = "voice//{}.mp3".format(i)
    t1 = Thread(target=v.recording())
    t1.setDaemon(True)
    t1.start()



def main():
    window.mainloop()

window = tk.Tk()
window.title('语音测评')
window.geometry('500x300')

timelabel = tk.Label(window,width=10,font=('Arial', 20))
timelabel.pack()
timelabel.after(1000,updatetimer)

number = tk.Label(window, width=10, text="1/10",font=('Arial', 15))
number.place(x=250, y=170, anchor='s')

word = tk.Label(window, width=10, text="hello",font=('Arial', 20))
word.place(x=250, y=120, anchor='s')

var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, font=('Arial', 12), width=20, height=1)
l.place(x=250, y=200, anchor='s')

b = tk.Button(window, text='录音', font=('Arial', 12), width=10, height=1, command=hit_me)
b.place(x=250, y=250, anchor='s')



if __name__ == '__main__':
    main()