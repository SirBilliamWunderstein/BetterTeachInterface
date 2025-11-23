import DependencyObjects as dodo
import FileReader as fr
import tkinter as tk

class Window(tk.Tk):
    global disp_F
    global can
    global OBJ
    
    def __init__(self,fh):
        super().__init__()
        self.config(bg = "#262626")
        
        objI = fr.File_create(fh)
        self.OBJ = dodo.objection(objI[1],objI[0])
        
        self.disp_F = tk.Label(self,width = 1080,height = 600,bg = "#262626")
        
        self.can = tk.PhotoImage(width = 600,height=600)
        
        self.disp_F.config(image = self.can)
        
        self.disp_F.pack()
        
        self.load_img()
    
    def load_img(self):
        for i in range(601):
            ii = i - 300
            for j in range(601):
                j = j
                jj = 300 - j
                ret = {}
                blank = ""
                for faces in self.OBJ.Frel.keys():
                    re = self.OBJ.Frel[faces].get_In([ii,jj])
                    #print(re)
                    if re == 1:
                        blank += "l"
                    elif re == 0:
                        zz = self.OBJ.Frel[faces].get_Z([ii,jj])
                        ret[zz] = [self.OBJ.Frel[faces],re]
                        #if ii in range(-25,25) and jj in range(-25,25):
                            #print(ret)
                    
                if blank == "l"*len(self.OBJ.Frel):
                    self.can.put("green",(i,j))
                    #print("blank")
                else:
                    #print("dun")
                    #print(ret.keys())
                    Q = list(ret.keys())
                    if ret.keys():
                        if ret[max(Q)][1] == 0:
                            #if ii in range(-25,25) and jj in range(-25,25):
                                ##print("q",max(Q))
                            self.can.put(ret[max(Q)][0].col,(i,j))
                            #self.can.put("green",(i,j))
                        else:
                            self.can.put("#000000",(i,j))
        
        for i in range(600):
            self.can.put("#000000",(i,300))
        
        for i in range(600):
            self.can.put("#000000",(300,i))
                    
                
                
                
                
                
'''if i == j:
                    self.can.put("#262626",(i+540,j+300))
                else:
                    self.can.put("purple",(i+540,j+300))'''

objI = fr.File_create("./tesfil")
obj = dodo.objection(objI[1],objI[0])
print(obj.Frel)
print(obj.P)
roo = Window("./tesfil")
roo.mainloop()