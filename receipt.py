import tkinter
import tkinter.ttk
import tkinter.font
import menu_insert
from tkinter import *


class Receipt:
    def __init__(self, receipt):
        self.receipt = receipt

        self.receiptBack = tkinter.PhotoImage(file="image/blue.png")
        self.receiptBackL = tkinter.Label(image=self.receiptBack)
        self.receiptBackL.place(x=-2, y=-2)

        font = tkinter.font.Font(family="맑은 고딕", size=11)
        font2 = tkinter.font.Font(family="맑은 고딕", size=15)

        self.locationText = Label(self.receipt, text='더치페이', width=10, fg='#ff7878', font=font2, bg='#d8f4ff')
        self.locationText.place(x=420, y=5)

        # self.cl1 = Button(self.receipt, width=8, font=font, command=self.green, repeatdelay=20, bg='light green')
        # self.cl1.place(x=300, y=600)
        #
        # self.cl2 = Button(self.receipt, width=8, font=font, command=self.yellow, repeatdelay=20, bg='light yellow')
        # self.cl2.place(x=400, y=600)
        #
        # self.cl3 = Button(self.receipt, width=8, font=font, command=self.blue, repeatdelay=20, bg='light blue')
        # self.cl3.place(x=500, y=600)

        self.back = Button(self.receipt, width=8, text='<-',font=font, command=self.back, repeatdelay=20, bg='light blue')
        self.back.place(x=10, y=10)

        self.saveButton = Button(self.receipt, width=20, text='저장', font=font, repeatdelay=20, bg='white', fg="red")
        self.saveButton.place(x=350, y=650)


    def green(self):
        pass

    def yellow(self):
        pass

    def blue(self):
        pass
    def back(self):
        Move= menu_insert.Menuinsert(self.receipt)

    def play(self):
        self.receipt.mainloop()

if __name__=='__main__':
    menu = tkinter.Tk()
    menu.title("더치 페이")
    menu.geometry("900x700+100+100")
    menu.resizable(False, False)

    re = Receipt(menu)
    re.play()