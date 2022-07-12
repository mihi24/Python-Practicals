m=list(map(int,input("Enter a list: ").split()))
l_m=len(m)
print("Array elements at even positions are: ")
for i in range(1,l_m,2):
    print(m[i],end=' ')
