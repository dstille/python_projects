import re

def find_parentheses(s: str):
    left_indexes = []
    simple_parentheses = []
    complex_parentheses = []
    for i in range(len(s)):
        if s[i] == "(": left_indexes += [i]
        if s[i] == ")":
            if "(" in s[left_indexes[-1] + 1:]:
                complex_parentheses += [s[left_indexes.pop(-1): i + 1]]
            else:
                simple_parentheses += [s[left_indexes.pop(-1): i + 1]]
    return simple_parentheses + complex_parentheses

def find_left_arg(op_index, str_in):
    for i in range(op_index):
        if str_in[i: op_index] in d: return str_in[i: op_index]
    return str_in[:op_index]    

def find_right_arg(op_index, s):
    for i in range(len(s), op_index, -1):
        if s[op_index + 1: i] in d: return s[op_index + 1: i]
    return s[op_index + 1:]    

def find_3fields(op_index, s):
    return re.split("[,\)]", s[op_index:])[:3]

def evaluate(op, args):
     if op == "SUM": return "SUM," + args[0] + "," + args[1] + "," + args[2], summation(args[0], args[1], args[2])
     elif op == "^": return args[0] + op + args[1], d[args[0]]**d[args[1]]
     elif op == "*": return args[0] + op + args[1], d[args[0]]*d[args[1]]
     elif op == "/": return args[0] + op + args[1], d[args[0]]/d[args[1]]
     elif op == "+": return args[0] + op + args[1], d[args[0]]+d[args[1]]
     elif op == "-": return args[0] + op + args[1], d[args[0]]-d[args[1]]
     elif op == "=": return args[0], d[args[1]]

def find_nums(s):
    skip = -1
    for i in range(len(s)):
        if s[i] in "0123456789" and i > skip:
             for j in range(i, len(s)):
                 if j == len(s) -1 or s[j+1] not in "0123456789":
                     d[s[i:j+1]] = int(s[i:j+1])
                     skip = j
                     break

def eval_term(str_in):
    find_nums(str_in)
    evaluated = str_in
    exps_to_eval = find_parentheses(str_in) + [str_in]
    operators = ["SUM", "^", "*", "/", "+", "-", "="]
    for exp in exps_to_eval:
        for op in operators:
            for i in range(len(exp)):
                args = []
                if exp[i: i + len(op)] == op:
                    if op == "SUM":
                        args += find_3fields(i + len(op) + 1, str_in)    
                    else:    
                        args += [find_left_arg(i, exp)]
                        args += [find_right_arg(i + len(op) - 1, exp)]
                    #print("args", args)
                    evaluated, value = evaluate(op, args) 
                    if "(" + evaluated + ")"== exp: evaluated = "(" + evaluated + ")"
                    d[evaluated] = value

            #print(d)
    return d[evaluated], evaluated    

def summation(orig, end, term):
   # print("end: ", end)
    start, curr = eval_term(orig)
   # print("start: ", start)
    sum = 0
    for i in range(start, d[end] + 1):
        d[curr] = i
       # print(i, curr)
        sum += eval_term(term)[0]
    return sum



if __name__ == "__main__":
    d = {}
    #exp6 = "(SUM,i=1,100,i+1)^2"
    #print(find_3fields(5,exp6))
    exp = "1-SUM,i=5,10,i^2"
    eval_term(exp)
    print(d[exp])
    exp2 = "SUM,i=0,5,SUM,j=i,3,j"
    eval_term(exp2)
    print(d)
    print(d[exp2])
    exp3 = "SUM,i=1,100,i+1"
    d = {}
    eval_term(exp3)
    print(d)
    print(d[exp3])
    eval_term('i=4')
    exp4 = '5*i^2+6'
    eval_term(exp4)
    print(d[exp4])
    #exp5 = "SUM,i=1,100,i+1*SUM,i=1,100,i+1"
    #eval_term(exp5)
    #print(d[exp5])
    exp6 = "(SUM,i=1,100,i+1)^2"
    #print(find_3fields(exp6))
    eval_term(exp6)
    print(d[exp6])

    
    


