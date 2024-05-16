n = int(input())
texts = []
for i in range(n):
    texts.append(str(input()))

cnt = 0
for text in texts:
    words = []
    tmp_char = None
    char_cnt = 0
    for char in text:
        if (tmp_char != char or tmp_char is None) and char not in words:
            words.append(char)
            tmp_char = char
            char_cnt += 1
            if len(text) == char_cnt:
                cnt += 1
                break
        elif tmp_char == char:
            char_cnt += 1
            if len(text) == char_cnt:
                cnt += 1
                break
            continue
        elif tmp_char != char and char in words:
            char_cnt += 1
            break

print(cnt)
