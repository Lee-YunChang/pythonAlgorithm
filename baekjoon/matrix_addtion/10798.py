

word_list = []
length = []
for _ in range(5):
    word = input()
    word_list.append(word)
    length.append(len(word))

result = ''
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            result += word_list[j][i]


print(result)


