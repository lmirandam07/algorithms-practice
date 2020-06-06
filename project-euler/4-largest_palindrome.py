def largest_palindrome(max_digit):
    max_num = (10**max_digit) - 1
    min_num = 10**(max_digit-1)
    palindrome = 0

    for i in range(max_num, min_num-1, -1):

        for k in  range(i, min_num-1, -1):
            product = (k * i)
            if str(product) == str(product)[::-1] and product > palindrome:
                palindrome = product
    return palindrome

print(largest_palindrome(3))