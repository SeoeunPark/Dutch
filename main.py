import tkinter
import tkinter.ttk
import tkinter.font
import menu_insert
from tkinter import *


class Main:
    def __init__(self, main):
        self.main = main

        fontq = tkinter.font.Font(size=13, weight='bold')
        fontm = tkinter.font.Font(size=17, weight='bold')

        self.mainBack = tkinter.PhotoImage(file="image/main_back.png")
        self.mainBackL = tkinter.Label(image=self.mainBack)
        self.mainBackL.place(x=-2, y=-2)
        #입력창
        self.saveButton = Button(self.main, width=10, height=2, text='시작', repeatdelay=20, bg='white', font=fontm,
                                 fg='#ff7878', command=self.to_menuinsert,default='active')  # command=self.to_receipt,
        self.saveButton.place(x=680, y=250)
        #내역
        self.saveButton = Button(self.main, width=10, height=2, text='내역 보기', repeatdelay=20, bg='white', font=fontm,
                                 fg='#ff7878', default='active')  # command=self.to_receipt,
        self.saveButton.place(x=680, y=350)

    def to_menuinsert(self):
        Move = menu_insert.Menuinsert(self.main)

    def play(self):
        self.main.mainloop()

if __name__ == '__main__':
    main = tkinter.Tk()
    main.title("더치 페이")
    main.geometry("900x700+100+100")
    main.resizable(False, False)

    ma = Main(main)
    ma.play()
