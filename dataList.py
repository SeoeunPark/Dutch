import tkinter
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

import pymysql

import showReceipt
import start

class DataList:
    def __init__(self, dataList):

        self.dataList = dataList
        # 내역리스트 화면 이미지
        self.Back = tkinter.PhotoImage(file="image/listBackground.png")
        self.BackL = tkinter.Label(image=self.Back)
        self.BackL.place(x=-2, y=-2)

        # 폰트 설정
        fonts = tkinter.font.Font(size=11, weight='bold')
        fontm = tkinter.font.Font(size=18, weight='bold')
        treeFont = tkinter.font.Font(size=24, weight='bold')

        # 뒤로가기 버튼
        self.backButton = Button(self.dataList, width=4, text='⇦', repeatdelay=20, bg='#ff7878', font=fontm,
                                 fg="white", command=self.moveToStart)  # command=self.to_receipt,
        self.backButton.place(x=20, y=25)

        #리스트가 들어갈 프레임
        self.listFrame = Frame(dataList, borderwidth=0, width=50, height=300)
        self.listFrame.place(x=52, y=150)

        # 리스트 스크롤바
        self.treeStyle = ttk.Style()
        self.treeStyle.configure("style.Treeview", highlightthickness=0, bd=0, font=('Comic Sans MS', 13))
        self.ListView = ttk.Treeview(self.listFrame, style="style.Treeview", selectmode="extended", height=23)
        self.ListView['columns'] = ("id", "datetime", "rinputLocation")
        self.ListView.grid(row=1, column=1, columnspan=1)
        self.ListView.heading("#0", text="", anchor="w")
        self.ListView.column("#0", anchor="center", width=0, stretch=NO, minwidth=0)
        self.ListView.heading("id", text="id", anchor="center")
        self.ListView.column("id", anchor="center", width=100, stretch=NO, minwidth=100)
        self.ListView.heading("datetime", text="date", anchor="center")
        self.ListView.column("datetime", anchor="center", width=200, stretch=NO, minwidth=200)
        self.ListView.heading("rinputLocation", text="title", anchor="center")
        self.ListView.column("rinputLocation", anchor="center", width=470, stretch=NO, minwidth=470)
        self.ListViewScrollbar = ttk.Scrollbar(self.listFrame, orient="vertical", command=self.ListView.yview)
        self.ListView.configure(yscroll=self.ListViewScrollbar.set)
        self.ListViewScrollbar.grid(row=1, column=6, sticky="ns")
        self.treeviewUpdate()

        self.ListView.bind('<Double-Button-1>', self.showData)

    def treeviewUpdate(self):
        # DB연결
        sqlCon = pymysql.connect(host="127.0.0.1", user="root", password="goodday0722", database="dutchdb", charset="utf8")
        cur = sqlCon.cursor()

        #트리뷰 업데이트
        cur.execute("SELECT Id, datetime,rinputLocation FROM dutchdb")
        results = cur.fetchall()
        if len(results) != 0:
            # 트리뷰 초기화
            Remove = self.ListView.get_children()
            for child in Remove:
                self.ListView.delete(child)
            for r in results:
                self.ListView.insert('', END, values=(r[0], r[1], r[2]))

        sqlCon.commit()
        sqlCon.close()


    def showData(self, e, personnum=None, inputLocation=None, inputMenu=None, personname=[0, 0, 0, 0, 0, 0],
                 personmenu=[0, 0, 0, 0, 0, 0], groupmenu=None, RadioVariety_1=None):
        #values리스트에서 Id값만 빼옴
        currentItem = self.ListView.focus()
        print(self.ListView.item(currentItem)['values'][0])
        self.Id =self.ListView.item(currentItem)['values'][0]

        sqlCon = pymysql.connect(host="127.0.0.1", user="root", password="goodday0722", database="dutchdb",
                                 charset="utf8")
        cur = sqlCon.cursor()
        cur.execute("select * from dutchdb where Id=%s", self.Id)
        result = cur.fetchone()

        personnum = (result[2])
        inputLocation = (result[16])
        inputMenu = (result[17])
        personname[1 - 1] = (result[3])
        personname[2 - 1] = (result[4])
        personname[3 - 1] = (result[5])
        personname[4 - 1] = (result[6])
        personname[5 - 1] = (result[7])
        personname[6 - 1] = (result[8])
        personmenu[1 - 1] = (result[9])
        personmenu[2 - 1] = (result[10])
        personmenu[3 - 1] = (result[11])
        personmenu[4 - 1] = (result[12])
        personmenu[5 - 1] = (result[13])
        personmenu[6 - 1] = (result[14])
        groupmenu = (result[15])
        RadioVariety_1 = (result[18])

        inputm = [inputLocation, inputMenu,
                  [personname[1 - 1], personmenu[1 - 1]],
                  [personname[2 - 1], personmenu[2 - 1]],
                  [personname[3 - 1], personmenu[3 - 1]],
                  [personname[4 - 1], personmenu[4 - 1]],
                  [personname[5 - 1], personmenu[5 - 1]],
                  [personname[6 - 1], personmenu[6 - 1]],
                  groupmenu, RadioVariety_1]

        Move = showReceipt.ShowReceipt(self.dataList, inputm, personnum)
        sqlCon.commit()


    # start으로 넘어가기
    def moveToStart(self):
        Move = start.Start(self.dataList)

