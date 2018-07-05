ab = [1, 2, 1, 3, 2, 5]
>> > count = 1
>> > abc = []
>> > for x in ab:
    if x in ab[1:]:
        abc.append(x)
        count += 3
    else
