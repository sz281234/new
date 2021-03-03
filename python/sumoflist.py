def sum(num):
 if len(num) == 1:
   return num[0]
 else:
   return num[0] + sum(num[1:])

print(sum([2,3]))
