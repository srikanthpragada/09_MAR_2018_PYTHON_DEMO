def sum(*nums):
    total = 0
    for n in nums:
        total += n

    return total


print(sum(10, 20))
print(sum(10, 20, 39, 21, 2, 2))


def wish(*names, message="Hi", footer='End'):
    for n in names:
        print(message, n)
    
    print(footer)


wish('Steve', 'Joe', 'Jeff', message="Hello", footer='The End')


