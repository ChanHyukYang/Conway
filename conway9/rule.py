def rule(val,lis):
   accum = 0
   for i in lis:
      accum = accum + i
   if val == 1:
      if accum == 2 or accum == 3:
         return 1
      else:
         return 0
   if val ==0:
      if accum == 3:
         return 1
      else:
         return 0

