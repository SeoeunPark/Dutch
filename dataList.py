import tkinter
import tkinter.font as tkFont
import tkinter.messagebox
from tkinter import *

import pymysql

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
        fontm = tkinter.font.Font(size=13, weight='bold')

        # 뒤로 가기 버튼
        self.backButton = tkinter.Button(self.dataList, width=4, text='⇦', repeatdelay=20, bg='#ff7878', font=fontm,
                                         fg="white", command=self.moveToStart)
        self.backButton.place(x=20, y=25)

        # 리스트가 들어갈 프레임
        listFrame = Frame(dataList, borderwidth=0, width=18, height=50, relief=RIDGE)
        listFrame.place(x=52, y=150)

        #리스트 스크롤바
        scrollbar = Scrollbar(listFrame)
        scrollbar.grid(row=0, column=0, sticky='ns')
        datalist = Listbox(listFrame, width=86, height=25,font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        datalist.bind('<<ListboxSelect>>')
        datalist.grid(row=0, column=0, padx=7, sticky='nsew')
        scrollbar.config(command=datalist.xview)


    def DisplayData(self):
        sqlCon = pymysql.connect(host="127.0.0.1", user="root", password="goodday0722", database="dutchdb")
        cur = sqlCon.cursor()
        cur.execute("select from dutchdb")
        result = cur.fetchall()
        for row in result:
            self.datalist.insert('', END, values = row)
        sqlCon.commit()
        sqlCon.Close()
        tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

        # start으로 넘어가기
    def moveToStart(self):
        Move = start.Start(self.dataList)

    DisplayData()

