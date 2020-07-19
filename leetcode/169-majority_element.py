def majorityElement(nums) -> int:
    if len(nums) == 1: return nums[0]

    def counting_func(n, c):
        if len(n) <= 1:
            if n[0] not in c:
                c.append(n[0])
                return
            else: return

        mid = len(n) // 2
        counting_func(n[:mid], c)
        counting_func(n[mid:], c)

        return c

    counts = counting_func(nums,[])
    return [n for n in counts if nums.count(n) > len(nums)//2][0]

print(majorityElement([2,2,1,1,1,2,2]))
