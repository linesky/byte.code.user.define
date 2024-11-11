tabs=" "*4
codes=""
files=input("file to convert to tab ford?")
f1=open(files,"r")
codes=f1.read()
f1.close()
codess=codes.split("\n")
codes=""

for n in codess:
    codes=codes + tabs +n+"\n"

f1=open(files+".out","w")
f1.write(codes)
f1.close()