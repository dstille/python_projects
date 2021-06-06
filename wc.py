import sys
text = open(sys.argv[1]).read().lower()
w_list = text.replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace(";", "").replace(":", "").split(" ")

dict = {}
for word in w_list:
   if word in dict.keys():
      dict[word] += 1
   else:
      dict[word] = 1

min = len(dict)
max = 0
least = ""
most = ""
for word in dict:
   if dict[word] < min:
      min = dict[word]
      least = word
   if dict[word] > max:
      max = dict[word]
      most = word

lines = len(text.split("\n"))
unique = len(dict)
words = len(w_list)
chars = len(text)
print(f"lines:{lines}, unique:{unique}, words:{words}, chars:{chars}")
print(f"Most frequent word:{most} ({max} times), Less frequent word:{least} ({min} times).")


