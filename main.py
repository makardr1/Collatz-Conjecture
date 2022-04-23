# The simplest unsolved problem - Collatz conjecture

# Collatz conjecture - the coolest math trick of all time
def function():
    x = int(input())
    counter = 0
    while x != 1:
        if x % 2 != 0:
            x = x * 3 + 1
            counter += 1
        elif x % 2 == 0:
            x = x / 2
            counter += 1
    print("Number of steps =", counter)

function()