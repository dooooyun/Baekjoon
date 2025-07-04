text = input()
count = [0] * 26
i = 0
k = 0
l = 0
num = 0

while i < len(text):
    count[ord(text[i].lower()) - ord('a')] += 1
    i += 1

max_count = count[0]
max_index = 0

while (k <= 25):
    if(max_count < count[k]):
        max_count = count[k]
        max_index = k
    k += 1

while l<=25:
    if(max_count == count[l]):
        num += 1
    l+=1

if num != 1 :
    print('?')
else :
    print(chr(max_index+65))
