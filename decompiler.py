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
for n in list1:
    ill=n.find("//")
    if ill>-1:
        n=n[:ill]
    txts=txts+n+"\n"



f1=open(pfiles+".il","w")
f1.write(txts)
f1.close()