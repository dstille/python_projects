import sys
num_dict = {} 
for num in sys.argv[1:]:
   if int(num) in num_dict.keys():
      num_dict[int(num)] += 1
   else:
      num_dict[int(num)] = 1
print(num_dict)