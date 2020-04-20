


def missingNumber(nums):
    sum, total = 0, 0
    for i in range(len(nums)):
        sum += nums[i]
        total += i + 1
    return - total + sum

# inputdata = [1,2,3,5,6,7,8]
#
# res = missingNumber(inputdata)
# print(res)


def missingNumber2(nums):
    start, end = 0, len(nums) - 1
    for i in range(1, len(nums)):

        mid = start + (end - start) // 2
        print("i", i, mid, start, end)
        if start <= end and mid >= 0 and nums[mid] - nums[mid - 1] == nums[mid + 1] - nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return (nums[start + 1] + nums[start]) // 2

inputdata = [1,2,3,4,5,7,8]

res = missingNumber2(inputdata)
print(res)