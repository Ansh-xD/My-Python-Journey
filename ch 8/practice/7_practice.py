"""
def rem(l, word):
    for item in l:
        l.remove(word)
        return l
    

l = ["Harry", "Rohan", "Ansh", "an"]

print(rem(l, "an"))"""




def rem(l, word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n

l = ["Harry", "Rohan", "Ansh", "an"]

print(rem(l, "an"))