#Ascending and descending 
h = list(map(int,input("Enter array number:").split()))
print("Array elments in ascending")
h.sort()
print(*h)
h.sort(reverse=True)
print("Array in Desending")
print(*h)