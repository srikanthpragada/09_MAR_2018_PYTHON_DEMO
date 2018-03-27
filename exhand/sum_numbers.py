import sys

sum = 0
i = 1
errors = 0
while i <= 5:
    try:
        n = int(input("Enter a number :"))
        sum += n
        i += 1
    except ValueError:
        print("Sorry! Invalid Number.")
        errors += 1
        if errors == 2:
            print("2 invalid inputs given. Quitting...")
            break
else:
    avg = sum / 5
    print(avg)


print("The End!")