import tkinter
import tkinter.ttk
import tkinter.font

import menu_insert
from tkinter import *


class Receipt:
    def __init__(self, receipt, inputmenu, personnum):
        self.receipt = receipt
        self.rpersonnum = personnum
        self.rpersonname = [0,0,0,0,0,0]
        self.rpersonmenu = [0,0,0,0,0,0]

        # menu_insert에서 배열 받아옴
        self.person = inputmenu
        # 받아온 값 새로운 변수에 저장
        self.minputLocation = inputmenu[0]
        self.minputMenu = inputmenu[1]
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
        self.rpersonname[1-1] = Label(self.receipt, text=self.person[1 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람2이름
        self.rpersonname[2-1] = Label(self.receipt, text=self.person[2 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람3이름
        self.rpersonname[3-1] = Label(self.receipt, text=self.person[3 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람4이름
        self.rpersonname[4-1] = Label(self.receipt, text=self.person[4 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람5이름
        self.rpersonname[5-1] = Label(self.receipt, text=self.person[5 + 1][0], fg='#db4455', font=fontm, bg='white')
        # 사람6이름
        self.rpersonname[6-1] = Label(self.receipt, text=self.person[6 + 1][0], fg='#db4455', font=fontm, bg='white')

        # 사람 수 만큼 칸 보여주기
        for i in range(0, self.rpersonnum):
            self.rpersonname[i].place(x=50, y=160 + 40 * (i + 1))

        # 1. /로 나누기 2. 문자로 된 리스트 값 정수로 바꾸기 3. 합계 구하기
        # person[1+1][0]
        self.per_sum = [0, 0, 0, 0, 0, 0]
        for i in range(0, self.rpersonnum):  # range 명수까지 입력
            p_split = self.person[i + 2][1].split('/')  # 값 계산 안됨....
            p_trans = map(int, p_split)
            self.per_sum[i] = sum(p_trans)

        # #그룹메뉴
            g_split = self.mgroupmenu.split('/')
            g_trans = map(int, g_split)
            self.rgroupmenu = sum(g_trans)

        # 사람1메뉴
        self.rpersonmenu[1-1] = Label(self.receipt, text=str(self.per_sum[0]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        # 사람2메뉴
        self.rpersonmenu[2-1] = Label(self.receipt, text=str(self.per_sum[1]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        # 사람3메뉴
        self.rpersonmenu[3-1] = Label(self.receipt, text=str(self.per_sum[2]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        # 사람4메뉴
        self.rpersonmenu[4-1] = Label(self.receipt, text=str(self.per_sum[3]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        # 사람5메뉴
        self.rpersonmenu[5-1] = Label(self.receipt, text=str(self.per_sum[4]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        # 사람6메뉴
        self.rpersonmenu[6-1] = Label(self.receipt, text=str(self.per_sum[5]) + '\t\t            ' + str(self.rgroupmenu),
                                  fg='#db4455', font=fontm, bg='white')
        #메뉴 위치 배정
        for i in range(0, self.rpersonnum):
            self.rpersonmenu[i].place(x=275, y=160 + 40 * (i + 1))
