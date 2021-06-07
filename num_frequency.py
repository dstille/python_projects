import sys
num_dict = {} 
for num in sys.argv[1:]:
   if int(num) in num_dict.keys():
      num_dict[int(num)] += 1
   else:
      num_dict[int(num)] = 1
count = len(num_dict) - 1
for i in num_dict:
   print(f"{i}:{num_dict[i]}", end = ", " if count > 0 else "")
   count -= 1