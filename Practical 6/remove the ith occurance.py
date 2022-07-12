def returnword(list1, word1, N):
   count = 0

   for i in range(0, len(list1)):
      if (list1[i] == word1):
         count = count + 1

      if(count == N):
         del(list1[i])
         return True
   return False

list1 = ['Eleven', 'twelve', 'thirteen', 'Javlin', 'lika','twelve']
print("The list is:",list1)
word1 = 'twelve'
N = 2

flag_val = returnword(list1, word1, N)

if (flag_val == True):
   print("The updated list is: ",list1)
else:
   print("List is not updated")