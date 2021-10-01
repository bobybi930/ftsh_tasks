f = open("demofile.txt", "r")
o = f.readlines()
dict = dict([])
t = ""
s = ""
for i in range(0, len(o)):
    if o[i][0] == '>':
        if not i == 0:
            dict[t] = (s.count('G') + s.count('C')) / len(s)
        t = o[i][1:].strip()
        s = ""
    else:
        s = ''.join({s, o[i].strip()}).strip()
dict[t] = (s.count('G') + s.count('C')) / len(s)
dict = {k: v for k, v in reversed(sorted(dict.items(), key=lambda item: item[1]))}
print(list(dict.items())[0][0])
print(list(dict.items())[0][1] * 100)
