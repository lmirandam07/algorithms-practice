def sum_square_diff(max_num):
    sum_squares = sum(num**2 for num in range(max_num+1))
    square_of_sum = sum(list(range(max_num+1)))**2

    return square_of_sum - sum_squares


print(sum_square_diff(100))