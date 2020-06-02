import re
handle = open ('regularexpression.txt')
numlist = list()
for line in handle:
    extract = re.findall('[0-9]+',line)
    for num in extract:
        num = int(num)
        numlist.append(num)
        total = sum(numlist)
        print(total)
