import json
st1 = {1: "One", 2: "two", 3: "three"}
st2 = {4: "four", 5: "five", 6: "six"}
ls = [st1, st2]
with open("tst.txt", 'w')as tst:
    json.dump(ls, tst)

with open("tst.txt", 'r')as tst:
    print(tst.read())


