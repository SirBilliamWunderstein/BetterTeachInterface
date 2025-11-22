global flsep
global xsep
global tsep
global sep
sep = 31
tsep = 63
xsep = 15
flsep = 79

def File_create(fn):
    f = fn + ".pdd"
    
    fin = open(f,"rb")
    
    read = fin.read()
    
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
    xyz = xyz.split(xsep.to_bytes(1, "big")) 
    for i in xyz:
        XYZ.append(numcon(i))
    
    title = numcon(title)
    LL = [title,xyz]
    return LL
    
def FaceMan(Fe):
    Fe = Fe.split(sep.to_bytes(1, "big"))
    FeCl = {}
    for i in Fe:
        i = i.split(tsep.to_bytes(1, "big"))
        L = []
        L.append(numcon(i[0]))
        i[1] = i[1].split(xsep.to_bytes(1, "big"))
        

def numcon(by):
    flp = b""
    for i in range(len(by)):
        if by[i] == flsep:
            i += 1
            flp += by[i:]
            i -= 1
            by = by[:1]
            break
    num  = 0.0
    dec = 0.0
    by = by[::-1]
    for i in range(len(by)):
        num += int(by[i])*(10^i)
    
    if flp:
        flp = flp[::-1]
        for i in range(len(flp)):
            dec += int(by[i])/(10^i)
    
    nem = num + dec
    return nem
        
    