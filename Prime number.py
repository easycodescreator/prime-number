def prime(text="Enter your number: "):
    # first function take a number from user
    a = int(input(text))
    # create a empty list
    d = []
    # create loops for find divisors
    for i in range(2, a):
        # check if (a) has divisor or not.
        if a % i == 0:
            d.append(i)
    # if d is empty number is prime
    # else number is not prime
    if d == []:
        print(f"The number ({a}) is prime.")
    else:
        print(f"The number ({a}) is not prime.")
    return d


print(prime())
