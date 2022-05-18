import re

d = {}

def find_parentheses(s: str):
    left_indexes = []
    sums = []
    simple_parentheses = []
    complex_parentheses = []
    for i in range(len(s)):
        if s[i] == "(": left_indexes += [i]
        if s[i] == ")":
            substr = s[left_indexes.pop(-1): i + 1]
            if "(" in substr[1:]:
                complex_parentheses += [substr]
            elif substr[1:4] == 'SUM':
                sums += [substr]    
            else:
                simple_parentheses += [substr]
    return sums + simple_parentheses + complex_parentheses

def find_left_arg(s):
    for i in range(len(s)):
        substr = s[i:]
        if substr in d:
            return substr
    return s        
    
def find_right_arg(s):
    for i in range(len(s), -1, -1):
        substr = s[:i]
        if substr in d: 
            return substr
    return s    

def find_3fields(s):
    print(s)
    return re.split(r"[,\)]", s)[1:4]

def evaluate(op, args):
     if op == "SUM":
         begin, end, term = args
         return f"SUM,{begin},{end},{term}", summation(begin, end, term)
     lftarg, rghtarg = args
     if op != '=': print(lftarg, rghtarg, d[lftarg], d[rghtarg])    
     if op == "^": return lftarg + op + rghtarg, d[lftarg]**d[rghtarg]
     if op == "*": return lftarg + op + rghtarg, d[lftarg]*d[rghtarg]
     if op == "/": return lftarg + op + rghtarg, d[lftarg]/d[rghtarg]
     if op == "+": return lftarg + op + rghtarg, d[lftarg]+d[rghtarg]
     if op == "-": return lftarg + op + rghtarg, d[lftarg]-d[rghtarg]
     if op == "=": return lftarg, d[rghtarg]

def find_nums(s):
    nums = re.findall('\d+', s)
    if nums:
        for num in nums:
            d[num] = int(num)

def prep(s):
    find_nums(s) 
    return find_parentheses(s) + [s]           

def parse(s):
    evaluated = s    
    exps_to_eval = prep(s)
    for exp in exps_to_eval:
        operators = find_ops(exp)
        for op, sides in operators.items():
            for left, right in sides:
                if op == "SUM":
                    args = find_3fields(right)  
                else:    
                    args = [find_left_arg(left)] + [find_right_arg(right)]
                evaluated, value = evaluate(op, args) 
                if f'({evaluated})'== exp: evaluated = f'({evaluated})'
                d[evaluated] = value
    return d[evaluated], evaluated

def find_ops(s):
    d = {}
    for i in range(len(s)):
        for op in ['SUM', '^', '*', '/', '+', '-', '=']:
            substr = s[i: i + len(op)]
            if substr == op:
                sides = (s[:i], s[i + len(op):])
                d[op] = d[op] + [sides] if op in d else [sides]           
    return d       

def summation(orig, end, term):
    start, curr = parse(orig)
    sum = 0
    for idx in range(start, d[end] + 1):
        d[curr] = idx
        sum += parse(term)[0]  
    return sum

def resolve(s):
    parse(s)
    return d[s]    



if __name__ == "__main__":
    exp = '(SUM,i=1,10,2*i)'
    print(resolve(exp))

    
    


