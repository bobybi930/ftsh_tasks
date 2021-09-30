f = open("demofile.txt", "r")
o = f.readlines()
dict = dict([])
for i in range(0, len(o), 3):
    s = ''.join({o[i + 1], o[i + 2]}).strip()
    dict[o[i][1:].strip()] = (s.count('G') + s.count('C')) / len(s)
dict = {k: v for k, v in reversed(sorted(dict.items(), key=lambda item: item[1]))}
print(list(dict.items())[0][0])
print(list(dict.items())[0][1] * 100)
