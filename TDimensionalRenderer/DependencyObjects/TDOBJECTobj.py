import DependencyObjects as dodo

class objection():
    global P
    global Frel
    
    def __init__(self,Point,Faceinf):
        self.P = Point
        self.Frel = {}
        
        for i in list(Faceinf.keys()):
            self.Frel[i] = dodo.FaceM(self.P[Faceinf[i][0]],self.P[Faceinf[i][1]],self.P[Faceinf[i][2]],Faceinf[i][3])
    
    def copy_cat(self,CC):
        CC.P = self.P
        CC.Frel = self.Frel