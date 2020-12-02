import tkinter
import tkinter.ttk
import tkinter.font
import tkinter.messagebox
from tkinter import *

import pymysql

import receipt
import numPeople

class Menuinsert:

    def __init__(self, menu, n):
        self.menu = menu
        self.personnum = n
        self.personname = [0, 0, 0, 0, 0, 0]
        self.personmenu = [0, 0, 0, 0, 0, 0]
        self.persontotal =[0, 0, 0, 0, 0, 0]

        # 배경 설정
        self.menuBack = tkinter.PhotoImage(file="image/white.png")
        self.menuBackL = tkinter.Label(image=self.menuBack)
        self.menuBackL.place(x=-2, y=-2)
        # 폰트 설정
        fonts = tkinter.font.Font(size=11, weight='bold')
        fontm = tkinter.font.Font(size=13, weight='bold')
        # 장소 입력
        self.locationText = Label(menu, text='장소', width=6, bg="white", font=fontm, fg='#ff7878')
        self.locationText.place(x=100, y=70)

        # 입력수에 제한받지 않고 필수로 나타나는 칸

        # 위치 입력칸
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
        self.menuText.place(x=65, y=140)

        self.inputMenu = Entry(self.menu, width=80, font=fonts, relief="groove", highlightthickness=2,
                               highlightbackground="#8294cd")
        self.inputMenu.place(x=100, y=170)

        # 이름 입력
        self.locationText = Label(self.menu, text='이름', width=10, bg="white", font=fontm, fg='#ff7878')
        self.locationText.place(x=70, y=210)  # 410
        # 사람1
        self.personname[1 - 1] = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 사람2
        self.personname[2 - 1] = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 사람3
        self.personname[3 - 1] = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 사람4
        self.personname[4 - 1] = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 사람5
        self.personname[5 - 1] = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 사람6
        self.personname[6 - 1] = Entry(self.menu, width=20, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")

        # 사람 수 만큼 칸 보여주기
        for i in range(0, self.personnum):
            self.personname[i].place(x=100, y=220 + 30 * (i + 1))

        # 메뉴 가격
        self.priceText = Label(self.menu, text='개인 메뉴 가격', width=10, bg="white", font=fontm, fg='#ff7878')
        self.priceText.place(x=330, y=210)  # 410
        # 메뉴1
        self.personmenu[1 - 1] = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 메뉴2
        self.personmenu[2 - 1] = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 메뉴3
        self.personmenu[3 - 1] = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 메뉴4
        self.personmenu[4 - 1] = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 메뉴5
        self.personmenu[5 - 1] = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 메뉴6
        self.personmenu[6 - 1] = Entry(self.menu, width=50, font=fonts, relief="groove", bg='white', fg='black',
                                       highlightthickness=1, highlightbackground="#8294cd")
        # 단체메뉴
        self.groupmenuText = Label(self.menu, text='단체메뉴 가격', width=10, bg="white", font=fontm, fg='#ff7878')
        self.groupmenuText.place(x=100, y=450)
        # 단체메뉴
        self.groupmenu = Entry(self.menu, width=55, font=fonts, relief="groove", bg='white', fg='black',
                               highlightthickness=1, highlightbackground="#8294cd")
        self.groupmenu.place(x=100, y=500)

        # 사람 수 만큼 메뉴칸 보여주기
        for i in range(0, self.personnum):
            self.personmenu[i].place(x=330, y=220 + 30 * (i + 1))

        # 반올림
        self.updown = Label(self.menu, text='반올림 단위 ', width=10, bg="white", font=fontm, fg='#ff7878')
        self.updown.place(x=100, y=550)

        # 라디오 버튼
        self.RadioVariety_1 = tkinter.IntVar()

        self.rd1 = Radiobutton(self.menu, text="10", bg="white", font=fontm, fg='#ff7878', value=1,
                               variable=self.RadioVariety_1)
        self.rd1.place(x=100, y=600)

        self.rd2 = Radiobutton(self.menu, text="100", bg="white", font=fontm, fg='#ff7878', value=2,
                               variable=self.RadioVariety_1)
        self.rd2.place(x=200, y=600)

        self.rd3 = Radiobutton(self.menu, text="1000", bg="white", font=fontm, fg='#ff7878', value=3,
                               variable=self.RadioVariety_1)
        self.rd3.place(x=300, y=600)

        self.rd4 = Radiobutton(self.menu, text="10000", bg="white", font=fontm, fg='#ff7878', value=4,
                               variable=self.RadioVariety_1)
        self.rd4.place(x=400, y=600)

        self.rd5 = Radiobutton(self.menu, text="반올림 안 함", bg="white", font=fontm, fg='#ff7878', value=5,
                               variable=self.RadioVariety_1)
        self.rd5.place(x=500, y=600)

        # 저장 버튼
        self.saveButton = Button(self.menu, width=30, text='G O !', repeatdelay=20, bg='#ff7878',
                                 font=fontm, fg="white", command=self.to_receipt)  # command=self.to_receipt,
        self.saveButton.place(x=300, y=650)

    def to_receipt(self):
        for i in range(0, self.personnum):
            if not self.personname[0].get():
                tkinter.messagebox.showinfo("이름 입력", "모든 사람의 이름을 입력해주세요.")
                break
            if not self.personmenu[i].get():
                tkinter.messagebox.showinfo("개인메뉴 가격 입력", "모든 개인메뉴 가격을 입력해주세요."
                                                          "\n개임메뉴가격이 없는 경우 0을 입력해주세요")
                break
            if not self.groupmenu.get():
                tkinter.messagebox.showinfo("그룹메뉴 가격 입력", "그룹메뉴 가격을 입력해주세요."
                                                          "\n그룹메뉴가격이 없는 경우 0을 입력해주세요")
                break
            else:
                inputm = [self.inputLocation.get(), self.inputMenu.get(),
                          [self.personname[1 - 1].get(), self.personmenu[1 - 1].get()],
                          [self.personname[2 - 1].get(), self.personmenu[2 - 1].get()],
                          [self.personname[3 - 1].get(), self.personmenu[3 - 1].get()],
                          [self.personname[4 - 1].get(), self.personmenu[4 - 1].get()],
                          [self.personname[5 - 1].get(), self.personmenu[5 - 1].get()],
                          [self.personname[6 - 1].get(), self.personmenu[6 - 1].get()],
                          self.groupmenu.get(), self.RadioVariety_1.get()]
                Move = receipt.Receipt(self.menu, inputm, self.personnum)
                break

    def moveTonumPeople(self):
        Move = numPeople.NumPeople(self.menu)

    def play(self):
        self.menu.mainloop()

    def Msgbox(self):
        tkinter.messagebox.showinfo("도움말", "1.이름 밑 칸에는 이름을 입력해주세요."
                                           "\n2.가격을 입력하실 때에는 첫번째칸부터 '/'로 가격을 나누어서 꼭 모두 입력해주세요. "
                                           "\n3.단체메뉴 가격도 '/'로 가격을 나누어서 입력해주세요."
                                           "\n4.입력을 끝냈다면 GO! 버튼을 눌러주세요.")

    def save(self):
        #dt = datetime.datetime.now()
        #self.filename = dt.strftime('%Y_%m_%d_%H%M%S')

        sqlCon = pymysql.connect(host="127.0.0.1", user="root", password="goodday0722", database="dutchdb")
        cur = sqlCon.cursor()
        cur.execute("INSERT INTO department (rpersonnum, rpersonname1, rpersonname2, rpersonname3, rpersonname4, rpersonname5, rpersonname6" \
              "rinputMenu1, rinputMenu2, rinputMenu3, rinputMenu4, rinputMenu5, rinputMenu6, " \
              "rper_tolsum1, rper_tolsum2, rper_tolsum3, rper_tolsum4, rper_tolsum5, rper_tolsum6, " \
              "rinputLocation, rgroupmenup, ori_price, round_price, over_price, under_price) " \
              "VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d, %d, %d, %d)", (
            self.rpersonnum,  # 명수
            self.rpersonname[1 - 1].get(),  # 이름1
            self.rpersonname[1 - 2].get(),  # 이름2
            self.rpersonname[1 - 3].get(),  # 이름3
            self.rpersonname[1 - 4].get(),  # 이름4
            self.rpersonname[1 - 5].get(),  # 이름5
            self.rpersonname[1 - 6].get(),  # 이름6

            self.rpersonmenu[1 - 1].get(),  # 메뉴1
            self.rpersonmenu[1 - 2].get(),  # 메뉴2
            self.rpersonmenu[1 - 3].get(),  # 메뉴3
            self.rpersonmenu[1 - 4].get(),  # 메뉴4
            self.rpersonmenu[1 - 5].get(),  # 메뉴5
            self.rpersonmenu[1 - 6].get(),  # 메뉴6

            self.rper_tolsum[1 - 1].get(),         #개인메뉴 총합 금액
            self.rper_tolsum[1 - 2].get(),         #개인메뉴 총합 금액
            self.rper_tolsum[1 - 3].get(),         #개인메뉴 총합 금액
            self.rper_tolsum[1 - 4].get(),         #개인메뉴 총합 금액
            self.rper_tolsum[1 - 5].get(),         #개인메뉴 총합 금액
            self.rper_tolsum[1 - 6].get(),         #개인메뉴 총합 금액
            self.rinputLocation.get(),  # 장소
            self.groupmenu,  # 그룹메뉴가격
            self.ori_price,  # 반올림전총액
            self.round_price,  # 반올림후총액
            self.over_price,  # 모자란금액
            self.under_price  # 남은금액
        ))
        sqlCon.commit()
        sqlCon.Close()
        tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")


if __name__ == '__main__':
    menu = tkinter.Tk()
    menu.title("더치 페이")
    menu.geometry("900x700+100+100")
    menu.resizable(False, False)

    re = Menuinsert(menu)
    re.play()
