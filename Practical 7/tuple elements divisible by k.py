TP=((1,2,3),(3,42,68),(23,56,89))
res=[]
k=2
for i in TP:
    for ele in i:
        if ele%k==0:
            res.append(ele)
print("Number divisible by k--",res)