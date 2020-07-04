def collatz(starts, control, nums_seq):
    nums_seq[starts] = 0
    while control > 1:
        if control % 2 == 0:
            control = int(control/2)
        else:
            control = int(3*control + 1)
        nums_seq[starts] += 1
        # Using memoization to check if a value was already saved
        if control in nums_seq:
            nums_seq[starts] += nums_seq[control]
            return




def longest_collatz(max_num):
    # Storing the long of the sequence for every number
    nums_seq = {}
    for i in range(1, max_num+1):
        collatz(i, i, nums_seq)

    return max(nums_seq, key=nums_seq.get)


print(longest_collatz(999999))

