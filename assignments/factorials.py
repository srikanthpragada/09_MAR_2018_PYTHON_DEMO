facts = []

for n in range(1, 11):
    # factorial of n
    fact = 1
    for i in range(2, n + 1):
        fact *= i

    facts.append(fact)

# print factorials
for i, f in enumerate(facts):
    print("%2d %d" % (i+1,f))



