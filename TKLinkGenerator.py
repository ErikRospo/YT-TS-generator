import re
from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Original link:')
        self.lbl2=Label(win, text='Start time:')
        self.lbl3=Label(win, text='End time:')
        self.lbl4=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.btn1 = Button(win, text='Go')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)
        self.lbl4.place(x=100, y=200)
        self.t4.place(x=200, y=200)
        self.b1=Button(win, text='Go', command=self.go)
        self.b1.place(x=100, y=250)
        self.v1 = IntVar()
        self.v2 = IntVar()
        self.C1 = Checkbutton(win, text = "Enabled?", variable = self.v1)
        self.C2 = Checkbutton(win, text = "Enabled?", variable = self.v2)
        self.v1.set(1)
        self.v2.set(1)
        self.C1.place(x=300, y=100)
        self.C2.place(x=300, y=150)

    def go(self):
        self.t4.delete(0, 'end')
        self.OriginalLink=self.t1.get()
        self.StartTime=int(self.t2.get())
        self.EndTime=int(self.t3.get())
        result=self.LinkEdit()
        self.t4.insert(END, str(result))
    def LinkEdit(self):
        stet=""
        v1gt=self.v1.get()
        v2gt=self.v2.get()
        if bool(v1gt):
            stet+=f"start={self.StartTime}"
        if bool(v1gt) and bool(v2gt):
            stet+="&"
        if bool(v2gt):
            stet+=f"end={self.EndTime}"
        return "https://www.youtube.com/embed/{}?{}".format((re.sub("(https://www\.youtube\.com/watch\?v\=)","",str(self.OriginalLink))),stet)


window=Tk()
mywin=MyWindow(window)
window.title('Link Converter')
window.geometry("400x300+10+10")
window.mainloop()
