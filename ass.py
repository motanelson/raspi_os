import os
print("\033c\033[43;30m\nget me file name to show")
a=input()
print("\nget me function name to show")
b=input()
c="copy %1 \"C:\\temp\"".replace("%1",a)
os.system(c)
os.chdir("C:\\Program Files (x86)\\Microsoft SDKs\\Windows\\v10.0A\\bin\\NETFX 4.8.1 Tools")
c="ildasm.exe %1 /out=c:/temp/myfile.il".replace("%1",a)
os.system(c)
f1=open("c:/temp/myfile.il","r")
d=f1.read()
f1.close()
e=d.split("\n")
i=False
for h in e:
    h=h.strip()
    print(h)