import math

class Mclass():
    def __init__(self):
        pass
    
    def cross_p(self,A,B):
        a = (A[1]*B[2]) - (A[2]*B[1])
        b = (A[0]*B[2]) - (A[2]*B[0])
        c = (A[0]*B[1]) - (A[1]*B[0])
        L = [a,b,c]
        return L

    def V_sub(self,A,B):
        L = [A[0]-B[0],A[1]-B[1],A[2]-B[2]]
        return L
    
    def complex_M(self,a,b):
        x = a[0]*b[0] - a[1]*b[1]
        y = a[0]*b[1] + a[1]*b[0]
        L = [x,y]
        return L