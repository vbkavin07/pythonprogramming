N=int(input(""))
Q=int(input(""))
for count in range(N,Q+1):
    if count > 1:
        for i in range(2,count):
            if(count%i)==0:
                break
	else:
	    print(count)
