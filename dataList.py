import tkinter
from tkinter import *
import os

class DataList:
    def __init__(self, dataList):
        self.dataList = dataList


        path_dir = "C:/Users/kangyeson/Desktop/Dutch_SampleFile"  #\를 /로 바꿔줘야 실행됨
        file_list = os.listdir(path_dir)

        # 내역리스트 화면 이미지
        self.mainBack = tkinter.PhotoImage(file="image/background.gif")
        self.mainBackL = tkinter.Label(image=self.mainBack)
        self.mainBackL.place(x=-2, y=-2)