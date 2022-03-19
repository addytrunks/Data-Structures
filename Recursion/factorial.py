# Iterative O(n)

def findFactorialIterative(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
    return fact

# Recursive O(n)
def findFactorialRecursive(number):
    if number == 0:
        return 1
    if number <=2:
        return number
    return number * findFactorialRecursive(number-1)

    # number = 5
    # 5* fact(4) -> 5* 4* fact(3) ->5* 4* 3* fact(2) -> 3*2

