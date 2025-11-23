global flsep
global xsep
global tsep
global sep
global hexy

hexy = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
sep = 31
tsep = 63
xsep = 93
flsep = 79

def File_create(fn):
    f = fn + ".pdd"
    
    fin = open(f,"rb")
    
    read = fin.read()
    #print(read)
    
    global Pointer
    global Facer
    for i in read:
        if i == 127:
            q = read.index(i.to_bytes(1,"big"))
            Pointer = read[:q]
            q += 1
            Facer = read[q:]
    
    PoiL = {}
    i = 0
    Pointer = Pointer.split(sep.to_bytes(1, "big"))
    
    for i in Pointer:
        q = xyzer(i)
        PoiL[q[0]] = q[1]
    
    #print(PoiL)
    
    FaceL = FaceMan(Facer)
    
    return [FaceL,PoiL]

def xyzer(se):
    title = b""
    xyz = b""
    for i in range(len(se)):
        if se[i] == tsep:
            title += se[:i]
            i += 1
            xyz += se[i:]
            break
    
    j = 0
    XYZ =  []
    #print(xyz)
    xyz = xyz.split(xsep.to_bytes(1, "big")) 
    ##print(xyz)
    for i in xyz:
        #print(i)
        XYZ.append(numcon(i))
    
    title = numcon(title)
    LL = [title,XYZ]
    return LL
    
def FaceMan(Fe):
    Fe = Fe.split(sep.to_bytes(1, "big"))
    FeCl = {}
    for i in Fe:
        #print(i)
        i = i.split(tsep.to_bytes(1, "big"))
        i[1] = i[1].split(xsep.to_bytes(1, "big"))
        hex = "#"
        #print(i)
        for j in i[1][3]:
            hex += hexy[j]
        xyzh = [numcon(i[1][0]),numcon(i[1][1]),numcon(i[1][2]),hex]
        FeCl[numcon(i[0])] = xyzh
    
    return FeCl
        

def numcon(by):
    flp = b""
    neg = False
    if by[0] == 97:
        neg = True
        by = by[1:]
    for i in range(len(by)):
        if by[i] == flsep:
            i += 1
            flp += by[i:]
            i -= 1
            by = by[:i]
            break
    num  = 0.0
    dec = 0.0
    #print("by:" , by)
    by = by[::-1]
    #print("bydash:" , by)
    for i in range(len(by)):
        num += int(by[i])*(10**i)
    
    if flp:
        flp = flp[::-1]
        for i in range(len(flp)):
            dec += int(by[i])/(10^i)
    
    nem = num + dec
    if neg:
        nem = nem*-1
    
    return nem
        
lem = File_create("tesfil")
print(lem)
    