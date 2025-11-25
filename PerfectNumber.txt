n=int(input("Enter a number: "))
l=[]
sum=0
i=1
while i<n:
    if n%i==0:
        l.append(i)
    i=i+1
for i in l:
    sum=sum+i
if sum==n:
    print("Perfect Number")
else:
    print("Not a perfect number")