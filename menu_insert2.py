import tkinter
import tkinter.ttk
import tkinter.font
from tkinter import *
import receipt


class Menuinsert:
    def __init__(self, menu):
        self.menu = menu

        self.menuBack = tkinter.PhotoImage(file="image/white.png")
        self.menuBackL = tkinter.Label(image=self.menuBack)
        self.menuBackL.place(x=-2, y=-2)

        font = tkinter.font.Font(size=11, weight='bold')
        fontq = tkinter.font.Font(size=13, weight='bold')
        self.locationText = Label(menu, text='위치:', width=6, bg="white", font=fontq, fg='#ff7878')
        self.locationText.place(x=600, y=5)

        self.inputLocation = Entry(self.menu, width=23, font=font, relief="groove", highlightthickness=2,
                                   highlightbackground="#808080")
        self.inputLocation.place(x=670, y=5)

        self.locationText = Label(self.menu, text='어떤 메뉴를 먹었나요?', width=20,bg="white", font=fontq, fg='#ff7878')
        self.locationText.place(x=20, y=50)

        self.inputLocation = Entry(self.menu, width=105, font=font, relief="groove", highlightthickness=2,
                                   highlightbackground="#808080")
        self.inputLocation.place(x=20, y=75)

        # self.locationText = Label(self.menu, text='이름을 입력해주세요', width=40, bg="#ff7878", font=fontq, fg='white')
        # self.locationText.place(x=200, y=150)

        self.locationText = Label(self.menu, text='이름', width=4, bg="white", font=fontq, fg='#ff7878')
        self.locationText.place(x=250, y=115) #410

        self.menuText = Label(self.menu, text='메뉴 가격', width=8, bg="white", font=fontq, fg='#ff7878')
        self.menuText.place(x=250, y=200)

        self.person1 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',highlightthickness=1,
                                   highlightbackground="#808080")
        self.person1.place(x=250, y=145)
        self.person1.insert(0, "ex) 사람 1")

        self.person1menu1 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                             highlightthickness=1,highlightbackground="#808080")
        self.person1menu1.place(x=250, y=230)

        self.person1menu2 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person1menu2.place(x=250, y=260)

        self.person1menu3 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person1menu3.place(x=250, y=290)

        self.person1menu4 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person1menu4.place(x=250, y=320)

        self.person1menu5 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person1menu5.place(x=250, y=350)


        self.person2 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',highlightthickness=1,
                                   highlightbackground="#808080")
        self.person2.place(x=500, y=145)
        self.person2.insert(0, "ex) 사람 2")

        self.person2menu1 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person2menu1.place(x=500, y=230)

        self.person2menu2 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person2menu2.place(x=500, y=260)

        self.person2menu3 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person2menu3.place(x=500, y=290)

        self.person2menu4 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person2menu4.place(x=500, y=320)

        self.person2menu5 = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person2menu5.place(x=500, y=350)


        self.groupText = Label(self.menu, text='단체메뉴 가격', width=10, bg="white", font=fontq, fg='#ff7878')
        self.groupText.place(x=250, y=405)

        self.groupmenu1 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.groupmenu1.place(x=250, y=445)

        self.groupmenu2 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#808080")
        self.groupmenu2.place(x=250, y=445)

        self.groupmenu3 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
                                highlightthickness=1, highlightbackground="#808080")
        self.groupmenu3.place(x=250, y=475)

        self.groupmenu4 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
                                highlightthickness=1, highlightbackground="#808080")
        self.groupmenu4.place(x=250, y=505)

        self.groupmenu5 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
                                highlightthickness=1, highlightbackground="#808080")
        self.groupmenu5.place(x=250, y=535)

        self.saveButton = Button(self.menu, width=30, text='GO!', repeatdelay=20,bg='#ff7878', font=fontq, fg="white")  # command=self.to_receipt,
        self.saveButton.place(x=300, y=650)

    # def to_receipt(self):
    #     Move= receipt.Receipt(self.menu)
    def play(self):
        self.menu.mainloop()


if __name__ == '__main__':
    menu = tkinter.Tk()
    menu.title("더치 페이")
    menu.geometry("900x700+100+100")
    menu.resizable(False, False)

    re = Menuinsert(menu)
    re.play()
