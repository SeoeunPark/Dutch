import tkinter
import tkinter.ttk
import tkinter.font

import menu_insert
from tkinter import *


class Receipt:
    def __init__(self, receipt, inputmenu, personnum):
        self.receipt = receipt
        self.rpersonnum = personnum

        # 0,1[self.inputLocation.get(), self.inputMenu.get(),
        # 2 [self.person1name.get(), self.person1menu.get()],
        # 3 [self.person2name.get(), self.person2menu.get()],
        # 4 [self.person3name.get(), self.person3menu.get()],
        # 5 [self.person4name.get(), self.person4menu.get()],
        # 6 [self.person5name.get(), self.person5menu.get()],
        # 7 [self.person6name.get(), self.person6menu.get()],
        # 8,9 self.groupmenu.get(), self.RadioVariety_1.get()]

        # menu_insert에서 배열 받아옴
        self.person = inputmenu
        # 받아온 값 새로운 변수에 저장
        self.minputLocation = inputmenu[0]
        self.minputMenu = inputmenu[1]
        # 이름
        # #self.mperson1name = inputmenu[2][0]
        # self.mperson2name = inputmenu[3][0]
        # self.mperson3name = inputmenu[4][0]
        # self.mperson4name = inputmenu[5][0]
        # self.mperson5name = inputmenu[6][0]
        # self.mperson6name = inputmenu[7][0]
        # 메뉴
        # self.mperson1menu = inputmenu[2][1]
        # self.mperson2menu = inputmenu[3][1]
        # self.mperson3menu = inputmenu[4][1]
        # self.mperson4menu = inputmenu[5][1]
        # self.mperson5menu = inputmenu[6][1]
        # self.mperson6menu = inputmenu[7][1]
        # 그룹메뉴
        self.mgroupmenu = inputmenu[8]
        self.mupdown = inputmenu[9]
        # 폰트
        fonts = tkinter.font.Font(size=10, weight='bold')
        fontm = tkinter.font.Font(size=14, weight='bold')
        # 배경
        self.receiptBack = tkinter.PhotoImage(file="image/receipt_back.png")
        self.receiptBackL = tkinter.Label(image=self.receiptBack)
        self.receiptBackL.place(x=-2, y=-2)
        # 잘 들어가는 지 확인
        self.locationText = Label(self.receipt, text=self.person, fg='#ff7878', font=fonts, bg='white')
        self.locationText.place(x=400, y=10)
        # 뒤로가기 버튼
        self.backButton = Button(self.receipt, width=4, text='⇦', repeatdelay=20, bg='#ff7878', font=fontm,
                                 fg="white", command=self.back)  # command=self.to_receipt,
        self.backButton.place(x=20, y=25)
        # 저장 버튼
        self.saveButton = Button(self.receipt, width=30, text='저 장', repeatdelay=20, bg='#ff7878', font=fontm,
                                 fg="white")
        self.saveButton.place(x=300, y=650)

        # 화면 배치하기

        # 위치
        self.rinputLocation = Label(self.receipt, text=self.minputLocation, fg='#db4455', font=fontm, bg='white')
        self.rinputLocation.place(x=130, y=530)
        # 메뉴
        self.rinputMenu = Label(self.receipt, text=self.minputMenu, fg='#db4455', font=fontm, bg='white')
        self.rinputMenu.place(x=90, y=570)
        # 사람1이름
        self.rperson1name = Label(self.receipt, text=self.person[1 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람2이름
        self.rperson2name = Label(self.receipt, text=self.person[2 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람3이름
        self.rperson3name = Label(self.receipt, text=self.person[3 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람4이름
        self.rperson4name = Label(self.receipt, text=self.person[4 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람5이름
        self.rperson5name = Label(self.receipt, text=self.person[5 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람6이름
        self.rperson6name = Label(self.receipt, text=self.person[6 + 1][0], fg='#db4455', font=fontm, bg='white')

        if (self.rpersonnum == 2):
            self.rperson1name.place(x=50, y=200)
            self.rperson2name.place(x=50, y=240)
        elif (self.rpersonnum == 3):
            self.rperson1name.place(x=50, y=200)
            self.rperson2name.place(x=50, y=240)
            self.rperson3name.place(x=50, y=280)
        elif (self.rpersonnum == 4):
            self.rperson1name.place(x=50, y=200)
            self.rperson2name.place(x=50, y=240)
            self.rperson3name.place(x=50, y=280)
            self.rperson4name.place(x=50, y=320)
        elif (self.rpersonnum == 5):
            self.rperson1name.place(x=50, y=200)
            self.rperson2name.place(x=50, y=240)
            self.rperson3name.place(x=50, y=280)
            self.rperson4name.place(x=50, y=320)
            self.rperson5name.place(x=50, y=360)
        elif (self.rpersonnum == 6):
            self.rperson1name.place(x=50, y=200)
            self.rperson2name.place(x=50, y=240)
            self.rperson3name.place(x=50, y=280)
            self.rperson4name.place(x=50, y=320)
            self.rperson5name.place(x=50, y=360)
            self.rperson6name.place(x=50, y=400)

        # 1. /로 나누기 2. 문자로 된 리스트 값 정수로 바꾸기 3. 합계 구하기
        # person[1+1][0]
        self.per_sum = [0, 0, 0, 0, 0, 0]
        for i in range(0, self.rpersonnum):  # range 명수까지 입력
            p_split = self.person[i + 2][1].split('/')  # 값 계산 안됨....
            p_trans = map(int, p_split)
            self.per_sum[i] = sum(p_trans)

        # #그룹메뉴
        if (self.mgroupmenu != ''):
            g_split = self.mgroupmenu.split('/')
            g_trans = map(int, g_split)
            self.rgroupmenu = sum(g_trans)
        else:
            self.rgroupmenu = '1000'

        # 사람1메뉴
        self.rperson1menu = Label(self.receipt, text=str(self.per_sum[0]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        # 사람2메뉴
        self.rperson2menu = Label(self.receipt, text=str(self.per_sum[1]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        # 사람3메뉴
        self.rperson3menu = Label(self.receipt, text=str(self.per_sum[2]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        # 사람4메뉴
        self.rperson4menu = Label(self.receipt, text=str(self.per_sum[3]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        # 사람5메뉴
        self.rperson5menu = Label(self.receipt, text=str(self.per_sum[4]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        # 사람6메뉴
        self.rperson6menu = Label(self.receipt, text=str(self.per_sum[5]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')

        if (self.rpersonnum == 2):
            self.rperson1menu.place(x=275, y=200)
            self.rperson2menu.place(x=275, y=240)
        elif (self.rpersonnum == 3):
            self.rperson1menu.place(x=275, y=200)
            self.rperson2menu.place(x=275, y=240)
            self.rperson3menu.place(x=275, y=280)
        elif (self.rpersonnum == 4):
            self.rperson1menu.place(x=275, y=200)
            self.rperson2menu.place(x=275, y=240)
            self.rperson3menu.place(x=275, y=280)
            self.rperson4menu.place(x=275, y=320)
        elif (self.rpersonnum == 5):
            self.rperson1menu.place(x=275, y=200)
            self.rperson2menu.place(x=275, y=240)
            self.rperson3menu.place(x=275, y=280)
            self.rperson4menu.place(x=275, y=320)
            self.rperson5menu.place(x=275, y=360)
        elif (self.rpersonnum == 6):
            self.rperson1menu.place(x=275, y=200)
            self.rperson2menu.place(x=275, y=240)
            self.rperson3menu.place(x=275, y=280)
            self.rperson4menu.place(x=275, y=320)
            self.rperson5menu.place(x=275, y=360)
            self.rperson6menu.place(x=275, y=400)

    def back(self):
        Move = menu_insert.Menuinsert(self.receipt)
