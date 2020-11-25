import tkinter

class DataList:
    def __init__(self, dataList):
        self.dataList = dataList

        # 내역리스트 화면 이미지
        self.mainBack = tkinter.PhotoImage(file="image/background.gif")
        self.mainBackL = tkinter.Label(image=self.mainBack)
        self.mainBackL.place(x=-2, y=-2)