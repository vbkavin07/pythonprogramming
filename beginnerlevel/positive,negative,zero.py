a=input()
i=0
if isinstance(a,str):
    print("string is not allowed")
else:
    i=int(a)
    if (i==0):
        print("zero")
    elif (i>0):
        print("positive")
    else:
        print("negative")
