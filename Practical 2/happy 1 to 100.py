def check_happy_num(my_num):
   remaining = sum_val = 0
   while(my_num > 0):
      remaining = my_num%10
      sum_val = sum_val + (remaining*remaining)
      my_num = my_num//10
   return sum_val
print("The list of happy numbers between 1 and 100 are : ")
for i in range(1, 101):
   my_result = i
   while(my_result != 1 and my_result != 4):
      my_result = check_happy_num(my_result)
   if(my_result == 1):
      print(i)