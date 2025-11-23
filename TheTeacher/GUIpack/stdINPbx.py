import tkinter as tk

class Mes():
    global inp
    global que
    global ent
    global sub
    global root
    
    def __init__(self,q):
        self.root = tk.Tk()
        self.root.config(bg = "#262626")
        self.inp = tk.StringVar()
        self.root.title("Input window")
        
        self.que = tk.Label(self.root,text = q,fg = "#6a1aa6",bg = "#262626",font = ("Comic Sans MS",14,"bold"))
        self.que.pack()
        
        self.ent = tk.Entry(self.root,textvariable=self.inp,fg = "#6a1aa6",bg = "#262626",font = ("Comic Sans MS",18,"bold"))
        self.ent.pack()
        
        self.sub = tk.Button(self.root,text= "submit",fg = "#6a1aa6",command = self.root.destroy,bg = "#262626",font = ("Comic Sans MS",14,"bold"))
        self.sub.pack()
    
    def start(self):
        self.root.mainloop()
        return self.inp.get()
    