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
        #장소 입력
        self.locationText = Label(menu, text='장소', width=6, bg="white", font=fontq, fg='#ff7878')
        self.locationText.place(x=100, y=70)

        self.inputLocation = Entry(self.menu, width=23, font=font, relief="groove", highlightthickness=2,
                                   highlightbackground="#8294cd")
        self.inputLocation.place(x=100, y=100)
        #뒤로 가기 버튼
        self.backButton = Button(self.menu, width=4, text='⇦', repeatdelay=20, bg='#ff7878', font=fontq,
                                 fg="white")  # command=self.to_receipt,
        self.backButton.place(x=20, y=25)
        #도움말 버튼
        self.infoButton = Button(self.menu, width=5, text='도움말', repeatdelay=20, bg='#ff7878', font=fontq,
                                 fg="white",command=self.Msgbox) # command=self.to_receipt,
        self.infoButton.place(x=800, y=25)
        #메뉴 입력
        self.locationText = Label(self.menu, text='어떤 메뉴를 먹었나요?', width=20,bg="white", font=fontq, fg='#ff7878')
        self.locationText.place(x=100, y=140)

        self.inputLocation = Entry(self.menu, width=80, font=font, relief="groove", highlightthickness=2,
                                   highlightbackground="#8294cd")
        self.inputLocation.place(x=100, y=170)

        # 이름 입력
        self.locationText = Label(self.menu, text='이름', width=10, bg="white", font=fontq, fg='#ff7878')
        self.locationText.place(x=100, y=210) #410
        #사람1
        self.person1name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                             highlightthickness=1,highlightbackground="#8294cd")
        self.person1name.place(x=100, y=250)
        # 사람2
        self.person2name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#8294cd")
        self.person2name.place(x=100, y=280)
        # 사람3
        self.person3name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#8294cd")
        self.person3name.place(x=100, y=310)
        # 사람4
        self.person4name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#8294cd")
        self.person4name.place(x=100, y=340)
        # 사람5
        self.person5name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#8294cd")
        self.person5name.place(x=100, y=370)
        # 사람6
        self.person6name = Entry(self.menu, width=20, font=font, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        self.person6name.place(x=100, y=400)
        
        #메뉴 가격
        self.priceText = Label(self.menu, text='메뉴 가격', width=10, bg="white", font=fontq, fg='#ff7878')
        self.priceText.place(x=330, y=210) #410
        #메뉴1
        self.person1menu = Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                             highlightthickness=1,highlightbackground="#8294cd")
        self.person1menu.place(x=330, y=250)
        # 메뉴2
        self.person2menu = Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#8294cd")
        self.person2menu.place(x=330, y=280)
        # 메뉴3
        self.person3menu = Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#8294cd")
        self.person3menu.place(x=330, y=310)
        # 메뉴4
        self.person4menu= Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#8294cd")
        self.person4menu.place(x=330, y=340)
        # 메뉴5
        self.person5menu = Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#8294cd")
        self.person5menu.place(x=330, y=370)
        # 메뉴6
        self.person6menu = Entry(self.menu, width=50, font=font, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        self.person6menu.place(x=330, y=400)

        #단체메뉴
        self.groupmenuText = Label(self.menu, text='단체메뉴 가격', width=10, bg="white", font=fontq, fg='#ff7878')
        self.groupmenuText.place(x=100, y=450)
        #단체메뉴
        self.groupmenu1 = Entry(self.menu, width=55, font=font, relief="groove", bg='white', fg='black',
                                  highlightthickness=1, highlightbackground="#8294cd")
        self.groupmenu1.place(x=100, y=500)

        #반올림
        self.groupText = Label(self.menu, text='반올림 단위 ', width=10, bg="white", font=fontq, fg='#ff7878')
        self.groupText.place(x=100, y=550)

        #라디오 버튼
        RadioVariety_1 = tkinter.IntVar()

        self.rd1 = Radiobutton(self.menu,text="100",bg="white",font=fontq, fg='#ff7878', value=1, variable=RadioVariety_1)
        self.rd1.place(x=100, y=600)

        self.rd2 = Radiobutton(self.menu, text="1000", bg="white", font=fontq, fg='#ff7878', value=2, variable=RadioVariety_1)
        self.rd2.place(x=200, y=600)

        self.rd3 = Radiobutton(self.menu, text="10000", bg="white", font=fontq, fg='#ff7878', value=3, variable=RadioVariety_1)
        self.rd3.place(x=300, y=600)

        #저장 버튼
        self.saveButton = Button(self.menu, width=30, text='G O !', repeatdelay=20,bg='#ff7878', font=fontq, fg="white",command=self.to_receipt)  # command=self.to_receipt,
        self.saveButton.place(x=300, y=650)

    def to_receipt(self):
       Move= receipt.Receipt(self.menu)

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
