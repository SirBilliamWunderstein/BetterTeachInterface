import DependencyObjects as dodo
import math
from GenMathClass import Mclass

gmc = Mclass()

class objection():
    global P
    global Faceinf
    global Frel
    
    def __init__(self,Point,Faceinf):
        self.Faceinf = Faceinf
        self.P = Point
        self.Frel = {}
        
        for i in list(Faceinf.keys()):
            print("dodo:",self.P[Faceinf[i][0]],self.P[Faceinf[i][1]],self.P[Faceinf[i][2]],Faceinf[i][3])
            self.Frel[i] = dodo.FaceMaster(self.P[Faceinf[i][0]],self.P[Faceinf[i][1]],self.P[Faceinf[i][2]],Faceinf[i][3])
    
    def copy_cat(self,CC):
        CC.P = self.P
        CC.Frel = self.Frel
    
    def rotate(self,lrud = 0):
        index = []
        R = []
        if lrud == 0:
            index.append(0)
            index.append(2)
            R.append(math.cos(math.radians(15)))
            R.append(math.sin(math.radians(15)))
        elif lrud == 1:
            index.append(0)
            index.append(2)
            R.append(math.cos(math.radians(15)))
            R.append(-math.sin(math.radians(15)))
        elif lrud == 2:
            index.append(2)
            index.append(1)
            R.append(math.cos(math.radians(15)))
            R.append(math.sin(-math.radians(15)))
        elif lrud == 3:
            index.append(2)
            index.append(1)
            R.append(math.cos(math.radians(15)))
            R.append(math.sin(math.radians(15)))
        
        for i in P.keys():
            A = [P[i][index[0]],P[i][index[1]]]
            ret = gmc.complex_M(A, R)
            P[i][index[0]] = ret[0]
            P[i][index[1]] = ret[1]
        
        self.FaceReload()
    
    def FaceReload(self):
        del self.Frel
        self.Frel = {}
        for i in list(Faceinf.keys()):
            self.Frel[i] = dodo.FaceMaster(self.P[Faceinf[i][0]],self.P[Faceinf[i][1]],self.P[Faceinf[i][2]],Faceinf[i][3])
        
            