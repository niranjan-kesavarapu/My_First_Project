n=int(input("Enter a number: "))
temp=n
temp1=n
arm=0
count=0
while n>0:
    r=n%10
    count=count+1
    n=n//10
while temp>0:
    r=temp%10
    arm=arm+r**count
    temp=temp//10
if arm==temp1:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")

