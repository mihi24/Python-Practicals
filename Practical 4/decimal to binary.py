def DecimalToBinary(num):
   if num > 1:
      DecimalToBinary(num // 2)
   print(num % 2, end = '')
# main
if __name__ == '__main__':
   dec_val = 35
   DecimalToBinary(dec_val)