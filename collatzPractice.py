def collatz(number):
    if number % 2 == 0:         # defines even number
        return number // 2
    elif number % 2 == 1:       # defines odd number
        return 3 * number + 1


print('Enter a number:')
try:
    userInput = int(input())
    newVal = collatz(userInput)
    print(newVal)

    while collatz(newVal) != 1:
        newVal = collatz(newVal)
        print(newVal)

    newVal = collatz(newVal)
    print(newVal)

except ValueError:
    print('You must enter an integer number')