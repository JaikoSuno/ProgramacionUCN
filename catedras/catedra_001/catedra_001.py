






x = int(input("Ingrese en valor de x: "))
n = int(input("Ingrese el valor de n: "))
p = n
while p > 0:
    p = p - 7
j = 2
c = 1
if p > 0:
    for i in range(n):
        j = j * i
    print(j)
else:
    if p == 0 and n < 10:

        p = True
        while j > 0:
            j = j - c
            if p:
                c = c + 1
            p = not p
        print(p)
    else:
        z = int(n/2)
        if z > 3:
            c *= x
            for i in range(n):
                c += 1
                print(c)
        else:
            c *= x
            for i in range(n, 1, -1):
                c += 1
                print(c)
