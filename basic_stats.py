def l_sqr(num_list):
   return [i**2 for i in num_list]

def avg(num_list):
   return sum(num_list) * 1.0/len(num_list)

def var(X):
   return sum([(x - avg(X))**2 for x in X]) * 1.0/len(X)



