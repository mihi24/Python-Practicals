
print("Enter a number: ")
n=int(input())
temp=n
sum=0
ln=len(str(n))
n=int(n)
while(n>0):
    p=n%10
    sum = sum +(p**ln)
    ln=ln-1
    n=n//10
if(sum == temp):
    print(temp,"is a Disarium number")
else:
    print(temp,"is not a Disarium number")