import re
handle=open('extra.txt')
count=0
summ=0
for line in handle:
    f=re.findall('[0-9]+',line)
    print(f)
    for num in f:
        count+=1
        summ=summ+int(num)
print(summ)
print(count)
