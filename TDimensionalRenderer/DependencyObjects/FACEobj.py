from GenMathClass import Mclass

met = Mclass()
class FaceM():
    global A
    global B
    global C
    global AB
    global BC
    global CA
    global cent
    global centIn
    global planeQ
    global col
    
    def init(self,pA,pB,pC,col):
        self.A = pA
        self.B = pB
        self.C = pC
        self.col = col
        
        self.AB = self.Lin_r(self.A, self.B)
        self.BC = self.Lin_r(self.B, self.C)
        self.CA = self.Lin_r(self.C, self.A)
        
        self.cent = [((self.A[0]+self.B[0]+self.C[0])/3),((self.A[1]+self.B[1]+self.C[1])/3),((self.A[2]+self.B[2]+self.C[2])/3)]
        self.centIn = self.In(self.cent)
        
        self.Plane()
        
    def In(self,P):
        l1 = P[1]-(P[0]*self.AB[0]) - self.AB[1]
        l2 = P[1]-(P[0]*self.BC[0]) - self.BC[1]
        l3 = P[1]-(P[0]*self.CA[0]) - self.CA[1]
        L = []
        if l1 > 0:
            L.append(0)
        elif l1 == 0:
            L.append(2)
        else:
            L.append(1)
            
        if l2 > 0:
            L.append(0)
        elif l2 == 0:
            L.append(2)
        else:
            L.append(1)
        
        if l3 > 0:
            L.append(0)
        elif l3 == 0:
            L.append(2)
        else:
            L.append(1)
        
        return L
    
    def get_In(self,P):
        Ch = self.In(P)
        if Ch == self.centIn():
            return 0
        else:
            for i in Ch:
                if i == 2:
                    r = 2 + Ch.index(i)
                    return r
            return 1
            
    def Plane(self):
        AB = met.V_sub(self.B, self.A)
        AC = met.V_sub(self.C, self.A)
        L = met.cross_p(AB,AC)
        d = (L[0]*self.A[0] + L[1]*self.A[1] + L[2]*self.A[2])*(-1)
        L.append(d)
        self.planeQ = L
    
    def Lin_r(self,a,b):
        tan = (b[1] - a[1])/(b[0] - a[0])
        c =  a[1] - (tan*a[0])
        L = [tan,c]
        return L 
        
        