import sys, re

def get_text(fname):
    return open(fname).read().lower()

def get_words(text):    
    return re.split('[\W\d]', text)

def get_counts(words):
    d = {}
    for w in words:
        d[w] = d[w] + 1 if w in d else 1
    return d

def get_dict():
    text = get_text('eatinghealthy.txt') 
    words = get_words(text)       
    d = get_counts(words)
    if '' in d: 
        del d['']
    return d   

if __name__ == '__main__':
    d = get_dict()     