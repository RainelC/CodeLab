# A narcissistic number, also known as an Armstrong number, is a number that is the sum of its own digits
# each raised to the power of the number of digits

def narcissistic( value ):
    digits = []
    x = value
    while x > 0:
        digits.append(x % 10)
        x = x // 10
    digits.reverse()
    result = sum([x**len(digits) for x in digits])
    return False if result != value else True

print(narcissistic(153))