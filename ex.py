from tkinter import *
from tkinter import ttk


class MyApp(Tk):
    def __init__(self):
        super(MyApp, self).__init__()

        self.geometry('950x500+100+100')
        self.NewTree = []

        label = Label(self,text='Table with some data', font=("Arial Bold", 25))
        label.pack()

        self.addLine()

        master_frame = Frame(self, bd=3, relief=RIDGE)
        master_frame.pack(side=BOTTOM)

        # Create a frame for the canvas and scrollbar(s).
        frame2 = Frame(master_frame)
        frame2.pack(side = BOTTOM)

        # Add a canvas in that frame.
        self.canvas = Canvas(frame2)
        self.canvas.grid(row=0, column=0)

        # Create a vertical scrollbar linked to the canvas.
        vsbar = Scrollbar(frame2, orient=VERTICAL, command=self.canvas.yview)
        vsbar.grid(row=0, column=1, sticky=NS)
        self.canvas.configure(yscrollcommand=vsbar.set)

        # Create a frame on the canvas to contain the buttons.
        self.table_frame = Frame(self.canvas)

        # Create canvas window to hold the buttons_frame.
        self.canvas.create_window((0,0), window=self.table_frame, anchor=NW)

    def addLine(self):
        #Make button for adding step
        bt = Button(self,text='Add Line',command=lambda: self.addLineMethod())
        bt.config(width=9, height=1)
        bt.pack()


    def addLineMethod(self):


        lineNumber = int(len(self.NewTree)/5)


        for index in range(5):

            s = ttk.Style()
            s.configure('MyStyle.Treeview', rowheight=25)
            self.NewTree.append(ttk.Treeview(self.table_frame, height=1,show="tree",columns=("0"),style='MyStyle.Treeview'))

            #Works fine when using this line instead of those above
            #self.NewTree.append(ttk.Treeview(self.table_frame, height=1,show="tree",columns=("0")))

            self.NewTree[index+5*lineNumber].grid(row=lineNumber, column=index+1)
            self.NewTree[index+5*lineNumber]['show'] = ''

            item = str(index+5*lineNumber)
            self.NewTree[index+5*lineNumber].column("0", width=180, anchor="w")
            self.NewTree[index+5*lineNumber].insert("", "end",item,text=item,values=('"Text text text"'))


        self.table_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = self.canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        self.canvas.configure(scrollregion=bbox, width=925, height=200)


app = MyApp()
app.mainloop()