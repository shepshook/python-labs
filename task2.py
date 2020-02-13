text = input()
dic = {}

words = text.split()
for word in words:
    if dic.get(word) is None:
        dic[word] = 1
    else:
        dic[word] += 1

sorted_words = [k for k, _ in sorted(dic.items(), key=lambda item: item[1], reverse=True)]

for i in range(min(len(sorted_words), 10)):
    print(sorted_words[i], end=" ")
