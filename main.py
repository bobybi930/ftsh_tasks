f = open("demofile.txt", "r")
o = f.readlines()
for i in range(0, len(o), 2):
    d = o[i]
    n = int(d.split()[0])
    k = int(d.split()[1])
    l = [1, 1]
    for j in range(n - 2):
        l.append(l[len(l) - 2] * k + l[len(l) - 1])
    print(l[len(l) - 1])
