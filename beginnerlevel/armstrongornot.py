n=int(input(""))
if(n<100000):
    a=list(map(int,str(n)))
    b=list(map(lambda x:x**3,a))
    if(sum(b)==n):
    	print("yes")
    else:
            print("no")
else:
	print("invalid number")
