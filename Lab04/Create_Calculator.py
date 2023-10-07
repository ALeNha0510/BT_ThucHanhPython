from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style

class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Calculator')
        
        Style().configure('TButton', padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)

        #create text
        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        #Create Button row1
        cls = Button(self, text="Cls")
        cls.grid(row=1, column=0)

        bck = Button(self, text='Back')
        bck.grid(row=1, column=1)

        cls = Button(self, text='Close')
        cls.grid(row=1, column=3)

        #Create Row2
        seven = Button(self, text='7')
        seven.grid(row=2, column=0)

        eight = Button(self, text='8')
        eight.grid(row=2, column=1)

        nine = Button(self, text='9')
        nine.grid(row=2, column=2)

        div = Button(self, text='/')
        div.grid(row=2, column=3)

        #create row3
        four = Button(self, text='4')
        four.grid(row=3, column=0)

        five = Button(self, text='5')
        five.grid(row=3, column=1)

        six = Button(self, text='6')
        six.grid(row=3, column=2)

        mul = Button(self, text='*')
        mul.grid(row=3, column=3)

        #Create row4
        one = Button(self, text='1')
        one.grid(row=4, column=0)

        two = Button(self, text='2')
        two.grid(row=4, column=1)

        three = Button(self, text='3')
        three.grid(row=4, column=2)

        sub = Button(self, text='-')
        sub.grid(row=4, column=3)

        #Create row5
        old = Button(self, text='0')
        old.grid(row=5, column=0)


        nine = Button(self, text='=')
        nine.grid(row=5, column=2)

        div = Button(self, text='+')
        div.grid(row=5, column=3)

        self.pack()


root = Tk()
app = Calculator(root)
root.mainloop()