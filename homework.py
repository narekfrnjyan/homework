n=input("input language")
file=open("text.txt",encoding="utf-8")
s=file.readlines()
if n=="hy":
    print(s[0])
elif n=="ru":
    print(s[1])
elif n=="en":
    print(s[2])
else :
    print("please input correct language")