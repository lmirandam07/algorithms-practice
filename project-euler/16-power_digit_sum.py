def power_digit_sum(base, exp):
    return sum([int(d) for d in str(base**exp)])

print(power_digit_sum(2,1000))