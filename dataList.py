import tkinter
import tkinter.font as tkFont
import tkinter.messagebox
from tkinter import *
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
        listFrame = Frame(borderwidth=0, width=20, height=50, relief=RIDGE)
        listFrame.pack(side=BOTTOM, fill=BOTH)

        #리스트 스크롤바
        scrollbar = Scrollbar(listFrame)
        scrollbar.grid(row=0, column=0, sticky='ns')
        datalist = Listbox(listFrame, width=90, height=20,font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set )
        datalist.bind('<<ListboxSelect>>')
        datalist.grid(row=0, column=0, padx=7, sticky='nsew')
        scrollbar.config(command=datalist.xview)

        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #

    #
    #
    #


    # start으로 넘어가기
    def moveToStart(self):
        Move = start.Start(self.dataList)
