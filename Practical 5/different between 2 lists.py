lis1 = list(map(int,input("Enter array number:").split()))
lis2 = list(map(int,input("Enter array number:").split()))
difference = list(set(lis1) - set(lis2))
print(difference)