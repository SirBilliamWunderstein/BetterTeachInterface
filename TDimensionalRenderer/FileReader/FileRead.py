sep = 31
tsep = 63
xsep = 15


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
    while i < len(Pointer):
        if Pointer[i] == sep.to_bytes(1,"big"):
            see = Pointer[:i]
            
            i += 1
            Pointer = Pointer[i:]
            i = 0
        i += 1


def xyzer(se):
    title = b""
    xyz = b""
    for i in range(len(se)):
        if se[i] == tsep.to_bytes(1, "big"):
            title += se[:i]
            i += 1
            xyz += se[i:]
            break
    

def numcon(by):
    by = by[::-1]
    for i in len():
        
    