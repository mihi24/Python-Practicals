#Mihir Manoj Jawale
#program to find harshad number
# 156 then 1+5+6=12 && 156 is divide by 12

print("Enter the number: ")
n=int(input())
sum=0
temp=n
while(n>0):
    sum+=(n%10)
    n=n//10      
if(temp%sum ==0):
    print(temp,"is a Harshad Number")
else:
    print(temp,"is  not a Harshad Number")


