import tkinter
import numPeople
import dataList
import pymysql.cursors

class Start:
    def __init__(self, start):
        self.start = start

        # start 화면 이미지
        self.startImage = tkinter.PhotoImage(file="image/mainImage.png")
        self.startImagePlace = tkinter.Label(image=self.startImage)
        self.startImagePlace.place(x=-2, y=-2)

        # 시작버튼
        self.startButton = tkinter.Button(self.start, text="시작하기", command=self.moveToNum, bg="#000000", fg="#ffffff",
                                          font=("고도B", 20, "bold"), width=15, height=2)
        self.startButton.place(x=600, y=280)

        # 내역확인 버튼
        self.startButton = tkinter.Button(self.start, text="내역보기", command=self.moveToList, bg="#000000", fg="#ffffff",
                                          font=("고도B", 20, "bold"), width=15, height=2)
        self.startButton.place(x=600, y=150)

    def moveToNum(self):
        Move = numPeople.NumPeople(self.start)

    def moveToList(self):
        Move = dataList.DataList(self.start)

    def play(self):
        self.start.mainloop()

if __name__ == '__main__':
    start = tkinter.Tk()
    start.title("Dutch")
    start.geometry("900x700+250+50")
    start.resizable(False, False)

    dutch = Start(start)
    dutch.play()


