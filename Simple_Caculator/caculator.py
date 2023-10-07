from tkinter import *
from tkinter.font import Font

root=Tk()
root.geometry('320x320')
root.title("Caculator")
fts=Font(family='san',size=12)

mh=Label(root,bg='#4279A5',fg='#FFFFFF',width=320,height=3,font=fts)
mh.pack(side=TOP)
fr=Frame(root)
fr.pack()

#HAM TAO BIEU THUC DANG CHUOI
bieuthuc=''

def xyly(num):
    global bieuthuc
    bieuthuc=bieuthuc+str(num)
    mh.config(text=bieuthuc)

def TinhToan():
    global ketqua
    global bieuthuc
    ketqua=eval(bieuthuc)
    mh.config(text=ketqua)
    bieuthuc=''
def Xoa():
    global bieuthuc
    mh.config(text='')
    bieuthuc=''
    print(bieuthuc)

#HANG 1
bt7=Button(fr,text='7',font=fts,width=8,pady=5,command=lambda:xyly('7'))
bt7.grid(row=1,column=1)
bt8=Button(fr,text='8',font=fts,width=8,pady=5,command=lambda:xyly('8'))
bt8.grid(row=1,column=2)
bt9=Button(fr,text='9',font=fts,width=8,pady=5,command=lambda:xyly('9'))
bt9.grid(row=1,column=3)
btCong=Button(fr,text='+',font=fts,width=8,pady=5,command=lambda:xyly('+'))
btCong.grid(row=1,column=4)
#HANG 2
bt4=Button(fr,text='4',font=fts,width=8,pady=5,command=lambda:xyly('4'))
bt4.grid(row=2,column=1)
bt5=Button(fr,text='5',font=fts,width=8,pady=5,command=lambda:xyly('5'))
bt5.grid(row=2,column=2)
bt6=Button(fr,text='6',font=fts,width=8,pady=5,command=lambda:xyly('6'))
bt6.grid(row=2,column=3)
btTru=Button(fr,text='-',font=fts,width=8,pady=5,command=lambda:xyly('-'))
btTru.grid(row=2,column=4)
#HANG 3
bt1=Button(fr,text='1',font=fts,width=8,pady=5,command=lambda:xyly('1'))
bt1.grid(row=3,column=1)
bt2=Button(fr,text='2',font=fts,width=8,pady=5,command=lambda:xyly('2'))
bt2.grid(row=3,column=2)
bt3=Button(fr,text='3',font=fts,width=8,pady=5,command=lambda:xyly('3'))
bt3.grid(row=3,column=3)
btNhan=Button(fr,text='*',font=fts,width=8,pady=5,command=lambda:xyly('*'))
btNhan.grid(row=3,column=4)
#HANG 4
bt0=Button(fr,text='0',font=fts,width=8,pady=5,command=lambda:xyly('0'))
bt0.grid(row=4,column=3)
btChia=Button(fr,text='/',font=fts,width=8,pady=5,command=lambda:xyly('/'))
btChia.grid(row=4,column=4)
#HANG 5
btDel=Button(fr,text='Del',font=fts,width=8,pady=5,command=Xoa)
btDel.grid(row=5,column=3)
btBang=Button(fr,text='=',font=fts,width=8,pady=5,command=TinhToan)
btBang.grid(row=5,column=4)

root.mainloop()