_a=int(raw_input())
_b=int(raw_input())
list=[]
sum=0
for i in range(0,_a):
	a=int(raw_input())
	list.append(a)
for j in range(0,_b):
	sum=sum+list[j]
print(sum)
