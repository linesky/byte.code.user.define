import os

files=input("file il to decompile? ")
pfiles=files
ill=files.find(".")
if ill>-1:
    pfiles=files[:ill]
os.system("ildasm "+files + " /out="+pfiles+".tmp")

f1=open(pfiles+".tmp","r")
txts=f1.read()
f1.close()

list1=txts.split("\n")
txts=""
onon=False
for n in list1:
    spacess=n.strip()!=""
    
    if n.find(".class")>-1:
        t=""
        ill=n.find(".")
        if ill>-1:
            t=n[:ill]
        
        ill=n.find("<")
        tt=""
        if ill>-1:
            tt=n[ill+1:]
        ill=n.find(">")
        if ill>-1:
            tt=tt[:ill]
        n=t+"class"+tt 
    if n.find(".method")>-1:
        t=""
        ill=n.find(".")
        if ill>-1:
            t=n[:ill]

        ill=n.find("<")
        tt=""
        if ill>-1:
            tt=n[ill+1:]
        ill=tt.find(">")
        if ill>-1:
            tt=tt[:ill]
        n=t+"int "+tt 

        
    if n.find(".entrypoint")>-1:
        t=""
        ill=n.find(".")
        if ill>-1:
            t=n[:ill]
        n=t+"entrypoint:"
    if n.find("call ")>-1:
        t=""
        ill=n.find("call")
        if ill>-1:
            t=n[:ill]
        tt=""
        ill=n.find("::")
        if ill>-1:
            tt=n[ill+2:]
        n=t+"call "+tt
    pointss=True
    if n.find(".custom")>-1:
        pointss=False
    if n.find(" nop")>-1:
        pointss=False
 
    if n.find("extends")>-1:
        pointss=False
    if n.find("instance")>-1:
        pointss=False
    if n.find(".")==0:
        pointss=False
    ill=n.find("IL_")
    if ill>-1:
        n=n[:ill]+n[ill+9:]
    ill=n.find("//")
    if ill>-1:
        n=n[:ill]
    if onon and spacess and pointss:
        txts=txts+n+"\n"
    if n.find(" "+files)>-1:
        onon=True


f1=open(pfiles+".il","w")
f1.write(txts)
f1.close()