import tkinter
import tkinter.ttk
import tkinter.font
import tkinter.messagebox
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
        
        self.locationText = Label(menu, text='장소', width=6, bg="white", font=fontq, fg='#ff7878')
        self.locationText.place(x=100, y=30)

        self.inputLocation = Entry(self.menu, width=23, font=font, relief="groove", highlightthickness=2,
                                   highlightbackground="#808080")
        self.inputLocation.place(x=100, y=60)

        self.saveButton = Button(self.menu, width=4, text='⇦', repeatdelay=20, bg='#ff7878', font=fontq,
                                 fg="white")  # command=self.to_receipt,
        self.saveButton.place(x=20, y=25)

        self.saveButton = Button(self.menu, width=5, text='도움말', repeatdelay=20, bg='#ff7878', font=fontq,
                                 fg="white",command=self.Msgbox) # command=self.to_receipt,
        self.saveButton.place(x=800, y=25)

        self.locationText = Label(self.menu, text='어떤 메뉴를 먹었나요?', width=20,bg="white", font=fontq, fg='#ff7878')
        self.locationText.place(x=100, y=100)

        self.inputLocation = Entry(self.menu, width=80, font=font, relief="groove", highlightthickness=2,
                                   highlightbackground="#808080")
        self.inputLocation.place(x=100, y=130)

        # 이름입력

        self.locationText = Label(self.menu, text='이름', width=10, bg="white", font=fontq, fg='#ff7878')
        self.locationText.place(x=100, y=170) #410

        self.person1name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                             highlightthickness=1,highlightbackground="#808080")
        self.person1name.place(x=100, y=200)

        self.person2name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person2name.place(x=100, y=230)

        self.person3name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person3name.place(x=100, y=260)

        self.person4name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person4name.place(x=100, y=290)

        self.person5name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person5name.place(x=100, y=320)

        self.person6name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#808080")
        self.person6name.place(x=100, y=350)
        
        #메뉴

        self.locationText = Label(self.menu, text='메뉴 가격', width=10, bg="white", font=fontq, fg='#ff7878')
        self.locationText.place(x=330, y=170) #410

        self.person1menu = Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                             highlightthickness=1,highlightbackground="#808080")
        self.person1menu.place(x=330, y=200)

        self.person2menu = Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person2menu.place(x=330, y=230)

        self.person3menu = Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person3menu.place(x=330, y=260)

        self.person4menu= Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person4menu.place(x=330, y=290)

        self.person5menu = Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.person5menu.place(x=330, y=320)

        self.person6menu = Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#808080")
        self.person6menu.place(x=330, y=350)

        # self.groupText = Label(self.menu, text='-'*150, width=85, bg="white", font=fontq, fg='#ff7878')
        # self.groupText.place(x=20, y=350)


        self.groupText = Label(self.menu, text='단체메뉴 가격', width=10, bg="white", font=fontq, fg='#ff7878')
        self.groupText.place(x=100, y=400)

        self.groupmenu1 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#808080")
        self.groupmenu1.place(x=100, y=430)

        self.groupText = Label(self.menu, text='반올림 단위 ', width=10, bg="white", font=fontq, fg='#ff7878')
        self.groupText.place(x=100, y=470)

        #라디오 버튼
        RadioVariety_1 = tkinter.IntVar()

        self.rd1 = Radiobutton(self.menu,text="100",bg="white",font=fontq, fg='#ff7878', value=1, variable=RadioVariety_1)
        self.rd1.place(x=100, y=510)

        self.rd2 = Radiobutton(self.menu, text="1000", bg="white", font=fontq, fg='#ff7878', value=2, variable=RadioVariety_1)
        self.rd2.place(x=200, y=510)

        self.rd3 = Radiobutton(self.menu, text="10000", bg="white", font=fontq, fg='#ff7878', value=3, variable=RadioVariety_1)
        self.rd3.place(x=300, y=510)
        #
        # self.groupmenu2 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
        #                          highlightthickness=1, highlightbackground="#808080")
        # self.groupmenu2.place(x=20, y=445)
        #
        # self.groupmenu3 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
        #                         highlightthickness=1, highlightbackground="#808080")
        # self.groupmenu3.place(x=20, y=445)
        #
        # self.groupmenu4 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
        #                         highlightthickness=1, highlightbackground="#808080")
        # self.groupmenu4.place(x=20, y=475)
        #
        # self.groupmenu5 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
        #                         highlightthickness=1, highlightbackground="#808080")
        # self.groupmenu5.place(x=20, y=505)

        self.saveButton = Button(self.menu, width=30, text='GO!', repeatdelay=20,bg='#ff7878', font=fontq, fg="white")  # command=self.to_receipt,
        self.saveButton.place(x=300, y=650)

    # def to_receipt(self):
    #     Move= receipt.Receipt(self.menu)
    def play(self):
        self.menu.mainloop()
    def Msgbox(self):
        tkinter.messagebox.showinfo("도움말","1.이름 밑 칸에는 이름을 입력해주세요."
                                          "\n2.가격을 입력하실 때에는 '/'로 가격을 나누어서 입력해주세요. "
                                          "\n3.단체메뉴 가격도 '/'로 가격을 나누어서 입력해주세요."
                                          "\n4.입력을 끝냈다면 GO! 버튼을 눌러주세요.")


if __name__ == '__main__':
    menu = tkinter.Tk()
    menu.title("더치 페이")
    menu.geometry("900x700+100+100")
    menu.resizable(False, False)

    re = Menuinsert(menu)
    re.play()
