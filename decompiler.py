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
    pointss=True
    if not(n.find(".class")>-1 or n.find(".method")>-1 or n.find(" .entrypoint")>-1):
         pointss=(n.find(".")!=0)
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