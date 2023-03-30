from tkinter import *
class MyWindow:
    def __init__(self,win):

#widgets start from here
        self.lbl1 = Label(win,text="1st No.")     #for label widget
        self.lbl1.place(x=100,y=50)
        self.lbl2 = Label(win, text= "2nd No.")
        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=100,y=150)
        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=200,y=50)
        self.txt2 = Entry(win,bd=1)
        self.txt2.place(x=200,y=100)
        self.txt3 = Entry(win,bd=3)
        self.txt3.place(x=200,y=150)

        self.btnclr= Button(win,text="Clear")
        self.btnclr.place(x=400,y=60)

        self.btnadd = Button(win,text="Addition")
        self.btnadd.place(x=400,y=120)
        self.btnsub = Button(win,text="Subtract")
        self.btnsub.place(x=400,y=180)

        self.btnmul = Button(win,text="Multiplication")
        self.btnmul.place(x=400,y=240)
        self.btndiv = Button(win, text="Division")
        self.btndiv.place(x=400, y=300)

        self.btnclr.bind('<Button-1>',self.clr)
        self.btnadd.bind('<Button-1>',self.add)
        self.btnsub.bind('<Button-1>',self.sub)
        self.btnmul.bind('<Button-1>',self.mul)
        self.btndiv.bind('<Button-1>',self.div)


#add event-handling /bind () method

    def add(self,add):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END,str(result))

# sub event-handler using command parameter
    def sub(self,sub):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1-num2
        self.txt3.insert(END, str(result))

    def mul(self,mul):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1*num2
        self.txt3.insert(END, str(result))


    def div(self,div):
        self.txt3.delete(0, 'end')
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1/num2
        self.txt3.insert(END, str(result))

    def clr(self,clr):
        self.txt1.delete(0,'end')
        self.txt1.insert(END, str())
        self.txt2.delete(0, 'end')
        self.txt2.insert(END, str())
        self.txt3.delete(0, 'end')
        self.txt3.insert(END, str())

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()







