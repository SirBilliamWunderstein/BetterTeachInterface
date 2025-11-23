import tkinter as tk
import pickle

class TheFlash(tk.Canvas):
    global flashL
    global fr
    global floc
    
    def __init__(self,floc,root):
        
        binfil = open("./BinDump/" + floc + ".dat","rb")
        self.flashL(pickle.load(binfil))
        binfil.close()
        
        self.floc = floc
        
        self.fr = tk.Frame(root, width = 100,height = 200,borderwidth = 2,bg = "#262626",highlightbackground="#6a1aa6", highlightcolor="#6a1aa6",relief = tk.FLAT)
        self.super.__init__(self.fr,width = 85,height = 185,bg = "#262626",fg = "#6a1aa6",font = ("Comic Sans",12,"bold"))
        
        self.create_text((0,0),text = self.floc)
        
        self.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)
        
        self.bind("<Button-1>", self.clicke)
    
    
    def clicke(self,event):
        pass
    
    def destoy(self):
        self.fr.destroy()
        self.destroy()
        