from math import sqrt

def create_dict_singles(words):
     singles = {}
     for i in words:
         singles[i] = singles[i] + 1 if i in singles else 1
     return singles

def create_dict_pairs(words):
    pairs = {}
    for i in range(len(words) - 1):
        if (words[i], words[i + 1]) in pairs:
            pairs[(words[i], words[i + 1])] += 1
        else:
            pairs[(words[i], words[i + 1])] = 1
    return pairs

def p(wj, wi, dict):
    return count_multi((wi, wj), dict) / count(wi, dict)

def count(wi, dict):
    return dict[wi] if wi in dict else 0

def count_multi(w_list, dict):
    if isinstance(w_list, str): w_list[1] = [w_list[1]]
    sum = 0
    for word in w_list[1]:
        if (w_list[0], word) in dict: sum += dict[(w_list[0], word)]
    return sum
    #return sum([dict[(w_list[0], word)] for word in w_list[1] if (w_list[0], word) in dict])

def similarity(S1, S2, words):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in words:
        sum1 += count3(i, S1) * count3(i, S2)
        sum2 += count3(i, S1) ** 2
        sum3 += count3(i, S2) ** 2
    return sum1 / (sum2 * sum3) ** .5

def similarity_2(S1, S2, words):
   return sum([count3(i, S1) * count3(i, S2) for i in words]) /  \
          sqrt(sum([count3(i, S1)**2 for i in words]) *     \
               sum([count3(i, S2)**2 for i in words]))

def similarity_3(S1, S2, V):
    return sum([count(word, S1) * count(word, S2) for word in V]) / \
           sqrt(sum([count(word, S1) ** 2 for word in V]) * \
                sum([count(word, S2) ** 2 for word in V]))




def count3(word, document):
    count = 0
    for w in document.split():
        if w == word: count += 1
    return count




if __name__ == '__main__':
    temp = open("eatinghealthy.txt").read().lower()
    words = temp.split()
    sentences = temp.split(".")
    singles = create_dict_singles(words)
    pairs = create_dict_pairs(words)
    dict = singles | pairs
    food = ["eggs", "meat", "dairy", "vegetables", "nutrients", "food", "foods"]
    print(food)
    print(p(food, "eat", dict))
    print(similarity("The cat sat on the hat in the hall", "The hat sat on a cat outside the hall", singles))
    S1 = create_dict_singles("The cat sat on the hat in the hall".split())
    S2 = create_dict_singles("The hat sat on a cat outside the hall".split())
    print(similarity_3(S1, S2, singles))
    print(similarity_3(S1, S1, singles))