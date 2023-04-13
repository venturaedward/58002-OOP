from tkinter import *
class MyWindow:
    def __init__(self,win):

#widgets start from here
        self.lbl1 = Label(win,text="Enter Circle Value")
        self.lbl1.place(x=250,y=50)

        self.lbl3 = Label(win, text="Radius Value")
        self.lbl3.place(x=250,y=100)

        self.lbl2 = Label(win, text="Diameter Value")
        self.lbl2.place(x=250, y=150)

        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=350,y=50)

        self.txt3 = Entry(win,bd=3)
        self.txt3.place(x=350,y=100)

        self.txt2 = Entry(win,bd=3)
        self.txt2.place(x=350,y=150)

        self.btnradius = Button(win,text="Radius")
        self.btnradius.place(x=250,y=200)

        self.btnradius.bind('<Button-1>', self.radius,self.diameter)
        self.btndiameter = Button(win,text="Diameter")
        self.btndiameter.place(x=300,y=200)
        self.btndiameter.bind('<Button-1>',self.diameter)

        self.btnclr = Button(win, text="Clear", fg="Red")
        self.btnclr.place(x=250, y=250)
        self.btnclr.bind('<Button-1>', self.clear)
#add event-handling /bind () method

    def radius(self,radius):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        result = (num1*num1)*3.1416
        result1 = 2*3.1416*(num1)
        self.txt3.insert(END, str(result))
        self.txt2.insert(END, str(result1))

    def diameter(self,diameter):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        result = ((num1/2)*(num1/2))*3.1416
        result1 = 2 * 3.1416 * (num1/2)
        self.txt3.insert(END, str(result))
        self.txt2.insert(END, str(result1))

    def clear(self, clear):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.geometry("800x600+20+20")
window.title("Circle Calculator")
window.mainloop()