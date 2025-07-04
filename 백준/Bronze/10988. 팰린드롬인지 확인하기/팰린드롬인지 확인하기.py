text = input()
length = len(text)
mid = len(text)//2

if(length%2 == 0):
    left = text[:mid]
    right = text[mid:]
    if(left == right[::-1]):
        print(1)
    else:
        print(0)
else:
    left = text[:mid]
    right = text[mid+1:]
    if(left == right[::-1]):
        print(1)
    else:
        print(0)