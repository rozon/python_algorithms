# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
# these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def multiples(num1, num2, limit):
    sum = 0
    for x in range(limit):
        if x % num1 == 0 or x % num2 == 0:
            sum += x
    return sum


print(multiples(3, 5, 1000))  # 233168
