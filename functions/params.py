def line(length=10, char='-'):
    for i in range(1, length):
        print(char, end='')


line(20, '.')  # Positional parameter
print()
line(length=30)  # Keyword parameter
print()
line(char='*', length=50)  # Keyword parameter
print()
line()

print(10,20,sep='-', end='*')