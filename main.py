numb = []
for x in range(1,1000):
    if x % 3 == 0 and x % 5 == 0:
        numb.append(x)
        print(numb)
        print(sum(numb))
