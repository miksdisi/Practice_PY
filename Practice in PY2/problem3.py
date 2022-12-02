import operator
dic = {1: 1, 3: 3, 5: 5, 7: 7, 9: 3, 11: 1, 8: 8, 4: 4}
# print(dic)
# d = dict(input('Enter your dictionary'))

result = dict(sorted(dic.items(), key=operator.itemgetter(1)))
print(result)