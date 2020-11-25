import tkinter
import tkinter.ttk
import tkinter.font
import tkinter.messagebox
from tkinter import *

import main
import receipt
import numPeople


class Menuinsert:
    def __init__(self,menu):
        self.menu = menu
        self.num=2

        self.menuBack = tkinter.PhotoImage(file="image/white.png")
        self.menuBackL = tkinter.Label(image=self.menuBack)
        self.menuBackL.place(x=-2, y=-2)

        fonts = tkinter.font.Font(size=11, weight='bold')
        fontm = tkinter.font.Font(size=13, weight='bold')
        # 장소 입력
        self.locationText = Label(menu, text='장소', width=6, bg="white", font=fontm, fg='#ff7878')
        self.locationText.place(x=100, y=70)

        self.inputLocation = Entry(self.menu, width=23, font=fonts, relief="groove", highlightthickness=2,
                                   highlightbackground="#8294cd")
        self.inputLocation.place(x=100, y=100)
        # 뒤로 가기 버튼
        self.backButton = Button(self.menu, width=4, text='⇦', repeatdelay=20, bg='#ff7878', font=fontm,
                                 fg="white", command=self.moveTonumPeople)  # command=self.to_receipt,
        self.backButton.place(x=20, y=25)
        # 도움말 버튼
        self.infoButton = Button(self.menu, width=5, text='도움말', repeatdelay=20, bg='#ff7878', font=fontm,
                                 fg="white", command=self.Msgbox)  # command=self.to_receipt,
        self.infoButton.place(x=800, y=25)
        # 메뉴 입력
        self.menuText = Label(self.menu, text='더치페이 할 품목', width=20, bg="white", font=fontm, fg='#ff7878')
        self.menuText.place(x=90, y=140)

        self.inputMenu = Entry(self.menu, width=80, font=fonts, relief="groove", highlightthickness=2,
                               highlightbackground="#8294cd")
        self.inputMenu.place(x=100, y=170)

        # 이름 입력
        self.locationText = Label(self.menu, text='이름', width=10, bg="white", font=fontm, fg='#ff7878')
        self.locationText.place(x=100, y=210)  # 410
        # 사람1
        self.person1name = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 사람2
        self.person2name = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 사람3
        self.person3name = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 사람4
        self.person4name = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 사람5
        self.person5name = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 사람6
        self.person6name = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 사람 수 만큼 칸 보여주기
        if (self.num == 2):
            self.person1name.place(x=100, y=250)
            self.person2name.place(x=100, y=280)
        elif (self.num == 3):
            self.person1name.place(x=100, y=250)
            self.person2name.place(x=100, y=280)
            self.person3name.place(x=100, y=310)
        elif (self.num == 4):
            self.person1name.place(x=100, y=250)
            self.person2name.place(x=100, y=280)
            self.person3name.place(x=100, y=310)
            self.person4name.place(x=100, y=340)
        elif (self.num == 5):
            self.person1name.place(x=100, y=250)
            self.person2name.place(x=100, y=280)
            self.person3name.place(x=100, y=310)
            self.person4name.place(x=100, y=340)
            self.person5name.place(x=100, y=370)
        elif (self.num == 6):
            self.person1name.place(x=100, y=250)
            self.person2name.place(x=100, y=280)
            self.person3name.place(x=100, y=310)
            self.person4name.place(x=100, y=340)
            self.person5name.place(x=100, y=370)
            self.person6name.place(x=100, y=400)

        # 메뉴 가격
        self.priceText = Label(self.menu, text='메뉴 가격', width=10, bg="white", font=fontm, fg='#ff7878')
        self.priceText.place(x=330, y=210)  # 410
        # 메뉴1
        self.person1menu = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 메뉴2
        self.person2menu = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 메뉴3
        self.person3menu = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 메뉴4
        self.person4menu = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 메뉴5
        self.person5menu = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 메뉴6
        self.person6menu = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                 highlightthickness=1, highlightbackground="#8294cd")
        # 단체메뉴
        self.groupmenuText = Label(self.menu, text='단체메뉴 가격', width=10, bg="white", font=fontm, fg='#ff7878')
        self.groupmenuText.place(x=100, y=450)
        # 단체메뉴
        self.groupmenu = Entry(self.menu, width=55, font=fonts, relief="groove", bg='white', fg='black',
                               highlightthickness=1, highlightbackground="#8294cd")
        self.groupmenu.place(x=100, y=500)

        if (self.num == 2):
            self.person1menu.place(x=330, y=250)
            self.person2menu.place(x=330, y=280)
        elif (self.num == 3):
            self.person1menu.place(x=330, y=250)
            self.person2menu.place(x=330, y=280)
            self.person3menu.place(x=330, y=310)
        elif (self.num == 4):
            self.person1menu.place(x=330, y=250)
            self.person2menu.place(x=330, y=280)
            self.person3menu.place(x=330, y=310)
            self.person4menu.place(x=330, y=340)
        elif (self.num == 5):
            self.person1menu.place(x=330, y=250)
            self.person2menu.place(x=330, y=280)
            self.person3menu.place(x=330, y=310)
            self.person4menu.place(x=330, y=340)
            self.person5menu.place(x=330, y=370)
        elif (self.num == 6):
            self.person1menu.place(x=330, y=250)
            self.person2menu.place(x=330, y=280)
            self.person3menu.place(x=330, y=310)
            self.person4menu.place(x=330, y=340)
            self.person5menu.place(x=330, y=370)
            self.person6menu.place(x=330, y=400)

        # 반올림
        self.groupText = Label(self.menu, text='반올림 단위 ', width=10, bg="white", font=fontm, fg='#ff7878')
        self.groupText.place(x=100, y=550)

        # 라디오 버튼
        self.RadioVariety_1 = tkinter.IntVar()

        self.rd1 = Radiobutton(self.menu, text="100", bg="white", font=fontm, fg='#ff7878', value=1,
                               variable=self.RadioVariety_1)
        self.rd1.place(x=100, y=600)

        self.rd2 = Radiobutton(self.menu, text="1000", bg="white", font=fontm, fg='#ff7878', value=2,
                               variable=self.RadioVariety_1)
        self.rd2.place(x=200, y=600)

        self.rd3 = Radiobutton(self.menu, text="10000", bg="white", font=fontm, fg='#ff7878', value=3,
                               variable=self.RadioVariety_1)
        self.rd3.place(x=300, y=600)

        # 저장 버튼
        self.saveButton = Button(self.menu, width=30, text='G O !', repeatdelay=20, bg='#ff7878',
                                 font=fontm, fg="white", command=self.to_receipt)  # command=self.to_receipt,
        self.saveButton.place(x=300, y=650)

    def to_receipt(self):
        #     #self,inputLocation,inputMenu,person1name,person2name,person3name,person4name,
        # person5name,person6name,person1menu,person2menu,person3menu,person4menu,person5menu,
        # person6menu,groupmenu,updown

            inputm = [self.inputLocation.get(), self.inputMenu.get(),
                      [self.person1name.get(), self.person1menu.get()],
                      [self.person2name.get(), self.person2menu.get()],
                      [self.person3name.get(), self.person3menu.get()],
                      [self.person4name.get(), self.person4menu.get()],
                      [self.person5name.get(), self.person5menu.get()],
                      [self.person6name.get(), self.person6menu.get()],
                      self.groupmenu.get(), self.RadioVariety_1.get()]
        # [위치,메뉴,[1],[2],[3],[4],[5],[6],group,단위]
            Move = receipt.Receipt(self.menu, inputm)

    def moveTonumPeople(self):
        Move = numPeople.NumPeople(self.menu)

    def to_main(self):
        Move = main.Main(self.menu)

    def play(self):
        self.menu.mainloop()

    def Msgbox(self):
        tkinter.messagebox.showinfo("도움말", "1.이름 밑 칸에는 이름을 입력해주세요."
                                           "\n2.가격을 입력하실 때에는 첫번째칸부터 '/'로 가격을 나누어서 꼭 모두 입력해주세요. "
                                           "\n3.단체메뉴 가격도 '/'로 가격을 나누어서 입력해주세요."
                                           "\n4.입력을 끝냈다면 GO! 버튼을 눌러주세요.")
if __name__ == '__main__':
    menu = tkinter.Tk()
    menu.title("더치 페이")
    menu.geometry("900x700+100+100")
    menu.resizable(False, False)

    re = Menuinsert(menu)
    re.play()
