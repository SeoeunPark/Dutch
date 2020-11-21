import tkinter
import tkinter.ttk
import tkinter.font

import menu_insert
from tkinter import *


class Receipt:
    def __init__(self, receipt):

        fontq = tkinter.font.Font(size=13, weight='bold')
        fontm = tkinter.font.Font(size=17, weight='bold')
        self.receipt = receipt

        self.receiptBack = tkinter.PhotoImage(file="image/eee.gif")
        self.receiptBackL = tkinter.Label(image=self.receiptBack)
        self.receiptBackL.place(x=-2, y=-2)

        self.locationText = Label(self.receipt, text='더치페이', width=10, fg='#ff7878', font=fontm, bg='#d8f4ff')
        self.locationText.place(x=400, y=10)

        self.backButton = Button(self.receipt, width=4, text='⇦', repeatdelay=20, bg='#ff7878', font=fontq,
                                 fg="white",command=self.back)  # command=self.to_receipt,
        self.backButton.place(x=20, y=25)

        self.saveButton = Button(self.receipt, width=30, text='저 장', repeatdelay=20,bg='#ff7878', font=fontq, fg="white")  # command=self.to_receipt,
        self.saveButton.place(x=300, y=650)


    def green(self):
        pass

    def yellow(self):
        pass

    def blue(self):
        pass

    def play(self):
        self.receipt.mainloop()

    def back(self):
        Move= menu_insert.Menuinsert(self.receipt)


if __name__=='__main__':
    menu = tkinter.Tk()
    menu.title("더치 페이")
    menu.geometry("900x700+100+100")
    menu.resizable(False, False)

    re = Receipt(menu)
    re.play()