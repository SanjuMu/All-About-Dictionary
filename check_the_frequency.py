test_dict= {'Coding': 2, 'is': 2, 'best': 2, 'for': 2, 'Coding':1}


print("The original dictionary:" + str(test_dict))

K= 2

res = 0
for key in test_dict:
    if test_dict[key]==K:
        res = res+1

print("The Frequency of K is: "+str(res))