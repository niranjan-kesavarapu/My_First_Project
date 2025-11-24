List=list(map(int,input("Enter the elements for list: ").split()))
unique=[]
for i in List:
    if i not in unique:
        unique.append(i)
print(unique)