num = int(input("Enter the number "))
sum=0;
temp= num
while temp>0:
    digit=temp%10
    sum+=digit *digit*digit;
    temp//=10
if num==sum:
    print(num,"is an amstrong number")
else :
    print(num,"is not an Armstrong number")