f = open("demofile.txt", "r")
o = f.readlines()
for i in range(0, len(o)):
    d = o[i]
    n = int(d.split()[0])
    k = 1
    m = int(d.split()[1])
    l = [1, 1]
    for j in range(2, n):
        if j < m:
            l.append(l[- 2] * k + l[- 1])
        elif j == m or l[-1] == m + 1:
            l.append(l[- 2] * k + l[- 1] - 1)
        else:
            l.append(l[- 2] * k + l[- 1] - l[- m - 1])
    print(l[len(l) - 1])
