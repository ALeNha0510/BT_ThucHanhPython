from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Information")
        self.pack(fill=BOTH, expand=True)

        #Freame 1
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text='ID', width=5)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        #Frame 2
        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text='Name', width=5)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, pady=5)

        #Frame 3
        frame3 = Frame(self)
        frame3.pack(fill=X)

        lbl3 = Label(frame3, text='Desc', width=5)
        lbl3.pack(side=LEFT, padx=5, pady=5, anchor=N)

        entry3 = Text(frame3)
        entry3.pack(fill=BOTH, padx=5, pady=5, expand=True)


root = Tk()
root.geometry('300x300+300+300')
app = Example(root)
root.mainloop()