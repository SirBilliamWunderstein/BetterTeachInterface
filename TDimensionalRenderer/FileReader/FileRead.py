def File_create(fn):
    f = fn + ".pdd"
    
    fin = open(f,"rb")
    
    read = fin.read()
    
    global Pointer
    global Facer
    for i in read:
        if i == 127:
            q = read.index(i.to_bytes())
            Pointer = read[:q]
            q += 1
            Facer = read[q:]
    
    