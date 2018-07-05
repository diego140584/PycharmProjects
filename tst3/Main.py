ab = [1, 3, 1, 2, 3, 5]
nw = []
count = 0
for x in ab:
    if x in ab[count+1:]:
        count+=1
        continue
    elif count == len(ab) - 1:
        if x in
    else:
        nw.append(x)
        count +=2
print(nw)
