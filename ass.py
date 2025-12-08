import os
print("\033c\033[43;30m\nget me file name to show")
a=input()
print("\nget me function name to show")
b=input()
c="\"C:\\Program Files (x86)\\Microsoft SDKs\\Windows\\v10.0A\\bin\\NETFX 4.8.1 Tools\\"\\ildasm.exe /tok /byt %1 /out=myfile.il".replace("%1",a)
os.system(c)
f1=open("myfile.il","r")
d=f1.read()
f1.close()
e=d.split("\n")
i=False
for h in e:
    h=h.strip()
    if i:
        
        o=h.find(">:")
        if o>-1:
            i=False
    if i:
        print(h)
    j=h.find(">:")
    if j>-1:
        l=h.find(b)
        if l>-1:
            j=h.find("<")
            i=True
            print(h[j+1:])
     
        
