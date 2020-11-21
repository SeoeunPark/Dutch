import tkinter
import tkinter.ttk
import tkinter.font
from tkinter import *
import receipt


class Menuinsert:
    def __init__(self, menu):
        self.menu = menu

        self.menuBack = tkinter.PhotoImage(file="image/pink_background.gif")
        self.menuBackL = tkinter.Label(image=self.menuBack)
        self.menuBackL.place(x=-2, y=-2)

        font = tkinter.font.Font(family="맑은 고딕",size=11)
        self.locationText = Label(menu, text='위치:', width=6, bg='#ff7878', font=font, fg="white")
        self.locationText.place(x=640, y=5)

        self.inputLocation = Entry(self.menu, width=23, font=font, relief="groove")
        self.inputLocation.place(x=700, y=5)

        self.locationText = Label(self.menu, text='어떤 메뉴를 먹었나요?', width=25, font=font, bg='#ff7878', fg="white")
        self.locationText.place(x=10, y=50)

        self.inputLocation = Entry(self.menu, width=50, font=font, relief="groove")
        self.inputLocation.place(x=10, y=75)

        self.saveButton = Button(self.menu, width=30, text='더치페이', font=font,repeatdelay=20,bg='white', fg="red")#command=self.to_receipt,
        self.saveButton.place(x=300, y=650)


    # def to_receipt(self):
    #     Move= receipt.Receipt(self.menu)
    def play(self):
        self.menu.mainloop()

if __name__=='__main__':
    menu = tkinter.Tk()
    menu.title("더치 페이")
    menu.geometry("900x700+100+100")
    menu.resizable(False, False)

    re = Menuinsert(menu)
    re.play()
