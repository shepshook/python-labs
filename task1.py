text = input()
dic = {}

words = text.split()
for word in words:
    if dic.get(word) is None:
        dic[word] = 1
    else:
        dic[word] += 1

print(dic)
