import math
import tkinter
import tkinter.ttk
import tkinter.font

import menu_insert
from tkinter import *


# 개인 메뉴 잘 보여줌
# 반올림 기능 해야함

class Receipt:
    def __init__(self, receipt, inputmenu, personnum):
        # inputm = 1[self.inputLocation.get(), self.inputMenu.get(),
        #           2[self.personname[1 - 1].get(), self.personmenu[1 - 1].get()],
        #           3[self.personname[2 - 1].get(), self.personmenu[2 - 1].get()],
        #           4[self.personname[3 - 1].get(), self.personmenu[3 - 1].get()],
        #          5[self.personname[4 - 1].get(), self.personmenu[4 - 1].get()],
        #           6[self.personname[5 - 1].get(), self.personmenu[5 - 1].get()],
        #          7[self.personname[6 - 1].get(), self.personmenu[6 - 1].get()],
        #           8,9self.groupmenu.get(), self.RadioVariety_1.get()]

        self.rpertotal =0
        self.receipt = receipt
        self.rpersonnum = personnum
        self.rpersonname = [0, 0, 0, 0, 0, 0]
        self.rpersonmenu = [0, 0, 0, 0, 0, 0]
        self.per_sum = [0, 0, 0, 0, 0, 0]
        self.per_tolsum = [0, 0, 0, 0, 0, 0]  # 계산
        self.rper_tolsum = [0, 0, 0, 0, 0, 0]  # 텍스트
        self.round_price = 0 #반올림 한 총합
        self.ori_price = 0 #반올림 전 총합


        # menu_insert에서 배열 받아옴
        self.person = inputmenu
        # 받아온 값 새로운 변수에 저장
        self.minputLocation = inputmenu[0]
        self.minputMenu = inputmenu[1]
        # 이름

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
        self.locationText.place(x=2, y=10)
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
        self.rpersonname[1 - 1] = Label(self.receipt, text=self.person[1 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람2이름
        self.rpersonname[2 - 1] = Label(self.receipt, text=self.person[2 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람3이름
        self.rpersonname[3 - 1] = Label(self.receipt, text=self.person[3 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람4이름
        self.rpersonname[4 - 1] = Label(self.receipt, text=self.person[4 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람5이름
        self.rpersonname[5 - 1] = Label(self.receipt, text=self.person[5 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람6이름
        self.rpersonname[6 - 1] = Label(self.receipt, text=self.person[6 + 1][0], fg='#db4455', font=fontm, bg='white')

        # 사람 이름 위치 지정
        for i in range(0, self.rpersonnum):
            self.rpersonname[i].place(x=50, y=160 + 40 * (i + 1))

        # 1. /로 나누기 2. 문자로 된 리스트 값 정수로 바꾸기 3. 합계 구하기
        # person[1+1][0]

        for i in range(0, self.rpersonnum):  # range 명수까지 입력
            p_split = self.person[i + 2][1].split('/')
            p_trans = map(int, p_split)
            self.per_sum[i] = sum(p_trans)

            # 그룹메뉴
            g_split = self.mgroupmenu.split('/')
            self.g_trans = sum(map(int, g_split))
            self.rgroupmenu = int(self.g_trans / self.rpersonnum)

        # 그룹메뉴 반올림
        if self.person[9] == 1:
            self.rgroupmenup = round(self.rgroupmenu, -1)
        elif self.person[9] == 2:
            self.rgroupmenup = round(self.rgroupmenu, -2)
        elif self.person[9] == 3:
            self.rgroupmenup = round(self.rgroupmenu, -3)
        elif self.person[9] == 4:
            self.rgroupmenup = round(self.rgroupmenu, -4)
        else:
            self.rgroupmenup = self.rgroupmenu

        # 사람1메뉴
        self.rpersonmenu[1 - 1] = Label(self.receipt,
                                        text=str(self.per_sum[0]) + '\t\t            ' + str(self.rgroupmenup),
                                        fg='#db4455', font=fontm, bg='white')
        # 사람2메뉴
        self.rpersonmenu[2 - 1] = Label(self.receipt,
                                        text=str(self.per_sum[1]) + '\t\t            ' + str(self.rgroupmenup),
                                        fg='#db4455', font=fontm, bg='white')
        # 사람3메뉴
        self.rpersonmenu[3 - 1] = Label(self.receipt,
                                        text=str(self.per_sum[2]) + '\t\t            ' + str(self.rgroupmenup),
                                        fg='#db4455', font=fontm, bg='white')
        # 사람4메뉴
        self.rpersonmenu[4 - 1] = Label(self.receipt,
                                        text=str(self.per_sum[3]) + '\t\t            ' + str(self.rgroupmenup),
                                        fg='#db4455', font=fontm, bg='white')
        # 사람5메뉴
        self.rpersonmenu[5 - 1] = Label(self.receipt,
                                        text=str(self.per_sum[4]) + '\t\t            ' + str(self.rgroupmenup),
                                        fg='#db4455', font=fontm, bg='white')
        # 사람6메뉴
        self.rpersonmenu[6 - 1] = Label(self.receipt,
                                        text=str(self.per_sum[5]) + '\t\t            ' + str(self.rgroupmenup),
                                        fg='#db4455', font=fontm, bg='white')
        # 메뉴 위치 지정
        for i in range(0, self.rpersonnum):
            self.rpersonmenu[i].place(x=275, y=160 + 40 * (i + 1))

        # 개인 토탈금액 계산
        for i in range(0, self.rpersonnum):
            self.per_tolsum[i] += self.per_sum[i]
            self.per_tolsum[i] += self.rgroupmenup
            self.rpertotal += self.per_tolsum[i]

        self.rper_tolsum[1 - 1] = Label(self.receipt, text=self.per_tolsum[1 - 1], fg='#db4455', font=fontm,
                                        bg='white')
        self.rper_tolsum[2 - 1] = Label(self.receipt, text=self.per_tolsum[2 - 1], fg='#db4455', font=fontm,
                                        bg='white')
        self.rper_tolsum[3 - 1] = Label(self.receipt, text=self.per_tolsum[3 - 1], fg='#db4455', font=fontm,
                                        bg='white')
        self.rper_tolsum[4 - 1] = Label(self.receipt, text=self.per_tolsum[4 - 1], fg='#db4455', font=fontm,
                                        bg='white')
        self.rper_tolsum[5 - 1] = Label(self.receipt, text=self.per_tolsum[5 - 1], fg='#db4455', font=fontm,
                                        bg='white')
        self.rper_tolsum[6 - 1] = Label(self.receipt, text=self.per_tolsum[6 - 1], fg='#db4455', font=fontm,
                                        bg='white')

        # 개인 총합 위치지정
        for i in range(0, self.rpersonnum):
            self.rper_tolsum[i].place(x=750, y=160 + 40 * (i + 1))

        # 기존 총합 계산
        for i in range(0, self.rpersonnum):
            self.ori_price += self.per_sum[i]
        self.ori_price += self.g_trans

        #반올림한 총합
        for i in range(0, self.rpersonnum):
            self.round_price += self.per_sum[i]
            self.round_price += self.rgroupmenup

        #차액 계산 원래금액 - 개인토탈금액 >0
        self.odprice = self.ori_price - self.rpertotal

        if self.odprice>0:
            self.over_price = self.odprice
            self.under_price = 0
        elif self.odprice<0:
            self.under_price= abs(self.odprice)
        else:
            self.under_price=0
            self.over_price=0

        # 기존 금액 / 남은 금액 / 모자란 금액 440
        self.price = Label(self.receipt, text="반올림 전 총액: " + str(self.ori_price) + "   반올림 후 총액: " + str(self.round_price) +"   모자란 금액 : " +str(self.over_price) +"   남은 금액 :"+str(self.under_price),
                           fg='#db4455', font=fontm, bg='white')
        self.price.place(x=50, y=450)

    def back(self):
        Move = menu_insert.Menuinsert(self.receipt, self.rpersonnum)
