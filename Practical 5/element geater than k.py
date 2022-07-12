li=[4,5,7,4,4,3,5,4,2,3]
print("The list is : "+str(li))

K=3
res = []
for i in li:

    frequency = li.count(i)
    if frequency>K and i not in res:
        res.append(i)

        print("The required elements is : "+str(res))