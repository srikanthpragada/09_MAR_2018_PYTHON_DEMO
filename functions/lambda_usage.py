def iseven(n):
    return n % 2 == 0


nums = [10, 11, 20, 25, 30]
enums = filter(iseven, nums)
onums = filter(lambda n: n % 2 == 1, nums)

for n in onums:
    print(n)
