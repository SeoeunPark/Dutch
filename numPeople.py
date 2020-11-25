import tkinter
import tkinter.font as tkFont
import menu_insert

class NumPeople:
    def __init__(self, numPeople):
        self.numPeople = numPeople

        # 인원수 저장 화면 이미지
        self.numImage = tkinter.PhotoImage(file="image/numPeopleImage.png")
        self.numImagePlace = tkinter.Label(image=self.numImage)
        self.numImagePlace.place(x=-2, y=-2)

        #인원수
        self.num = tkinter.StringVar()
        self.num.set('2')
        self.fontStyle = tkFont.Font(family="고도B", size=80, weight="bold")
        self.numLabel = tkinter.Label(self.numPeople, textvariable=self.num, font=self.fontStyle, bg="#ffffff", fg="#FF7878")
        self.numLabel.place(x=415, y=240)

        # 인원수 추가 버튼
        self.plusImage = tkinter.PhotoImage(file="image/plusImage.png")
        self.plusButton = tkinter.Button(self.numPeople, image=self.plusImage,
                                         command=self.increase_num, bd="0", highlightthickness="0")  #bd=테두리두께, highlightthickness=선택시 하이라이트 두께
        self.plusButton.place(x=600, y=270)

        # 인원수 빼기 버튼
        self.minusImage = tkinter.PhotoImage(file="image/minusImage.png")
        self.minusButton = tkinter.Button(self.numPeople, image=self.minusImage,
                                          command=self.decrease_num, bd="0", highlightthickness="0")
        self.minusButton.place(x=230, y=270)

        #인원수에 따라 대사 바뀜
        self.NextfontStyle = tkFont.Font(family="고도B", size=30, weight="bold", slant="italic")
        self.nextPageButton = tkinter.Button(self.numPeople, text="묻고 더블로 가!⇨", font=self.NextfontStyle,
                                            command=self.moveToMenu, bg="#FF7878", bd="0", highlightthickness="0")
        self.nextPageButton.place(x=180, y=555)

    #메인화면으로 넘어가기
    def moveToMenu(self):
        Move = menu_insert.Menuinsert(self.numPeople)

    #+버튼
    def increase_num(self):
        self.NextfontStyle = tkFont.Font(family="고도B", size=30, weight="bold", slant="italic")
        n = int(self.num.get())
        if(2<= n <= 5):
            n += 1
            self.num.set(n)
        if(n==2):
            self.nextPageButton['text'] = "묻고 더블로 가!⇨"
            self.nextPageButton.place(x=180, y=555)
        elif(n==3):
            self.nextPageButton['text'] = "따따블로 가!⇨"
            self.nextPageButton.place(x=210, y=555)
        elif(n==4):
            self.nextPageButton['text'] = "사딸라!⇨"
            self.nextPageButton.place(x=250, y=555)
        elif(n==5):
            self.nextPageButton['text'] = "오딸라!⇨"
            self.nextPageButton.place(x=250, y=555)
        elif(n==6):
            self.nextPageButton['text'] = "육따블로 가!⇨"
            self.nextPageButton.place(x=210, y=555)
    # -버튼
    def decrease_num(self):
        self.NextfontStyle = tkFont.Font(family="고도B", size=30, weight="bold", slant="italic")
        n = int(self.num.get())
        if (3 <= n <= 6):
            n -= 1
            self.num.set(n)
        if (n == 2):
            self.nextPageButton['text'] = "묻고 더블로 가!⇨"
            self.nextPageButton.place(x=180, y=555)
            return self.numPeople
        elif (n == 3):
            self.nextPageButton['text'] = "따따블로 가!⇨"
            self.nextPageButton.place(x=210, y=555)
        elif (n == 4):
            self.nextPageButton['text'] = "사딸라!⇨"
            self.nextPageButton.place(x=250, y=555)
        elif (n == 5):
            self.nextPageButton['text'] = "오딸라!⇨"
            self.nextPageButton.place(x=250, y=555)
        elif (n == 6):
            self.nextPageButton['text'] = "육따블로 가!⇨"
            self.nextPageButton.place(x=210, y=555)
