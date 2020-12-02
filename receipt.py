import tkinter
import tkinter.ttk
import datetime
import tkinter.font
import pymysql
import tkinter.messagebox

import menu_insert
import start
from tkinter import *

# 개인 메뉴 잘 보여줌
# 반올림 기능 해야함

class Receipt:

    def __init__(self, receipt, inputmenu, personnum):
        self.rpertotal = 0
        self.receipt = receipt
        self.rpersonnum = personnum
        self.rpersonname = [0, 0, 0, 0, 0, 0]  # 사람 이름
        self.rpersonmenu = [0, 0, 0, 0, 0, 0]  # 메뉴
        self.per_sum = [0, 0, 0, 0, 0, 0]  # 개인메뉴 합계
        self.per_tolsum = [0, 0, 0, 0, 0, 0]  # 계산
        self.rper_tolsum = [0, 0, 0, 0, 0, 0]  # 텍스트
        self.round_price = 0  # 반올림 한 총합
        self.ori_price = 0  # 반올림 전 총합

        # menu_insert에서 배열 받아옴
        self.person = inputmenu
        # 받아온 값 새로운 변수에 저장
        self.rinputLocation = inputmenu[0]
        self.rinputMenu = inputmenu[1]
        # 이름

        # 그룹메뉴
        self.mgroupmenu = inputmenu[8]
        self.mupdown = self.person[9]  # 라디오 버튼 1 : 10 ,2:100,3 :1000 4:10000 5 : 반올림 안 함
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
                                 fg="white", command=self.save)
        self.saveButton.place(x=300, y=650)

        # 화면 배치하기

        # 위치
        self.rinputLocation = Label(self.receipt, text=self.rinputLocation, fg='#db4455', font=fontm, bg='white')
        self.rinputLocation.place(x=130, y=530)
        # 메뉴
        self.rinputMenu = Label(self.receipt, text=self.rinputMenu, fg='#db4455', font=fontm, bg='white')
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
            p_split = self.person[i + 2][1].split('/')  # /로 나눠서 split
            p_trans = map(int, p_split)  # int 타입으로 변환
            p_sum = sum(p_trans)  # 리스트에 들어있는 값의 합을 구함
            if self.mupdown == 1:
                self.per_sum[i] = round(p_sum, -1)
            elif self.mupdown == 2:
                self.per_sum[i] = round(p_sum, -2)
            elif self.mupdown == 3:
                self.per_sum[i] = round(p_sum, -3)
            elif self.mupdown == 4:
                self.per_sum[i] = round(p_sum, -4)
            else:
                self.per_sum[i] = p_sum

        # 그룹메뉴
        g_split = self.mgroupmenu.split('/')
        self.g_trans = sum(map(int, g_split))
        self.rgroupmenu = int(self.g_trans / self.rpersonnum)  # 1/n 으로 나눔

        # 그룹메뉴 반올림
        if self.mupdown == 1:
            self.rgroupmenup = round(self.rgroupmenu, -1)
        elif self.mupdown == 2:
            self.rgroupmenup = round(self.rgroupmenu, -2)
        elif self.mupdown == 3:
            self.rgroupmenup = round(self.rgroupmenu, -3)
        elif self.mupdown == 4:
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

        # 반올림한 총합
        for i in range(0, self.rpersonnum):
            self.round_price += self.per_sum[i]
            self.round_price += self.rgroupmenup

        # 차액 계산 원래금액 - 전체 개인토탈금액 >0
        self.odprice = self.ori_price - self.rpertotal

        if self.odprice > 0:
            self.over_price = self.odprice
            self.under_price = 0
        elif self.odprice < 0:
            self.under_price = abs(self.odprice)
            self.over_price = 0
        else:
            self.under_price = 0
            self.over_price = 0

        # 기존 금액 / 남은 금액 / 모자란 금액 440
        self.price = Label(self.receipt, text="반올림 전 총액: " + str(self.ori_price) + "   반올림 후 총액: " + str(
            self.round_price) + "   모자란 금액 : " + str(self.over_price) + "   남은 금액 :" + str(self.under_price),
                           fg='#db4455', font=fonts, bg='white')
        self.price.place(x=50, y=450)

    def back(self):
        Move = menu_insert.Menuinsert(self.receipt, self.rpersonnum)

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
            self.rpersonname[1 - 1],  # 이름1
            self.rpersonname[1 - 2],  # 이름2
            self.rpersonname[1 - 3],  # 이름3
            self.rpersonname[1 - 4],  # 이름4
            self.rpersonname[1 - 5],  # 이름5
            self.rpersonname[1 - 6],  # 이름6

            self.rpersonmenu[1 - 1],  # 메뉴1
            self.rpersonmenu[1 - 2],  # 메뉴2
            self.rpersonmenu[1 - 3],  # 메뉴3
            self.rpersonmenu[1 - 4],  # 메뉴4
            self.rpersonmenu[1 - 5],  # 메뉴5
            self.rpersonmenu[1 - 6],  # 메뉴6

            self.rper_tolsum[1 - 1],         #개인메뉴 총합 금액
            self.rper_tolsum[1 - 2],         #개인메뉴 총합 금액
            self.rper_tolsum[1 - 3],         #개인메뉴 총합 금액
            self.rper_tolsum[1 - 4],         #개인메뉴 총합 금액
            self.rper_tolsum[1 - 5],         #개인메뉴 총합 금액
            self.rper_tolsum[1 - 6],         #개인메뉴 총합 금액
            self.rinputLocation,  # 장소
            self.rgroupmenup,  # 그룹메뉴가격
            self.ori_price,  # 반올림전총액
            self.round_price,  # 반올림후총액
            self.over_price,  # 모자란금액
            self.under_price  # 남은금액
        ))
        sqlCon.commit()
        sqlCon.Close()
        tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

        Move = start.Start(self.receipt)

