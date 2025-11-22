import tkinter as tk
from PIL import Image,ImageTk

global fci
global qnai
global cbi
global obji

#6a1aa6
#262626

fci = 1
qnai = 2
cbi = 3


class Main_Page(tk.Tk()):
    global fcB
    global qnaB
    global cbB
    global TITLECARD
    
    def __init__(self):
        self.super().__init__()
        self.title("TeachMeAI")
        self.configure(width = 450, height = 350)
        self.resizable(False,False)
        
        self.TITLECARD = tk.Label(self,text = "How shalth I assist THEE",fg = "#6a1aa6",bg = "#262626",font = ("Comic Sans","18","bold"),relief = tk.RAISED,borderwidth = 1)
        self.fcB = tk.Button(self,image= fci,fg = "#6a1aa6",bg = "#262626",borderwidth=1,width = 100,height = 300, relief= tk.RIDGE)
        self.qnaB = tk.Button(self,image= qnai,fg = "#6a1aa6",bg = "#262626",borderwidth=1,width = 100,height = 300, relief= tk.RIDGE)
        self.cbB = tk.Button(self,image= cbi,fg = "#6a1aa6",bg = "#262626",borderwidth=1,width = 100,height = 300, relief= tk.RIDGE)
        self.objB = tk.Button(self,image= obji,fg = "#6a1aa6",bg = "#262626",borderwidth=1,width = 100,height = 300, relief= tk.RIDGE)
        
        self.TITLECARD.place(x =0,y = 0)
        self.fcB.place(x = 10,y = 50)
        self.qnaB.place(x = 120,y = 50)
        self.cbB.place(x = 230,y = 50)
        self.objB.place(x= 340,y = 50)
        

class ChatBoxPg(tk.Tk()):
    global Rcan
    global Qbox
    global can
    
    def __init__(self):
        self.super().__init__()
        self.title("closeAI")
        self.config(width = 500,height = 400)
        self.resizable(False,False)
        
        self.SF1 = tk.Frame(self,width = 500,height= 350,borderwidth = 4,bg = "#262626",highlightbackground="#6a1aa6", highlightcolor="#6a1aa6",relief = tk.FLAT)
        self.SF2 = tk.Frame(self.SF1,width = 470,height= 320,borderwidth = 3,bg = "#262626",highlightbackground="#6a1aa6", highlightcolor="#6a1aa6",relief = tk.FLAT)
        self.can = tk.Canvas(self.SF2,width = 440,height = 290,scrollregion=(0,0,440,7000),bg = "#262626",fg = "#6a1aa6")
        
        
