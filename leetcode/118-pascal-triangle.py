def generate(numRows: int):
    arr = [[1]]

    if numRows == 1:
        return arr

    for i in range(1, numRows):
        sub_arr = []
        for j in range(0, i + 1):
            val = 0
            if j == 0 or j == i:
                val = 1
            else:
                val = arr[i - 1][j - 1] + arr[i - 1][j]

            sub_arr.append(val)
        arr.append(sub_arr)

    return arr


print(generate(7))
