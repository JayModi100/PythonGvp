# Word shuffle using string manipulation

import random

string  = "Hii, Hello I ma Jay How Wans Going What you doing"

words = string.split(" ")
list = []
for i in range(len(words)):
    while True:
        x = random.randint(0,len(words)-1)
        if x not in list:
            list.append(x)
            break
    print(words[x],end=" ")



