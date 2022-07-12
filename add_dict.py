from collections import Counter

def add_dict(d1,d2):

    new_dict = Counter(d1) + Counter(d2)
    
    return print(new_dict)

add_dict({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})