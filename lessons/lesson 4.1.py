# filter (func, iter)

def squere(x):
    return x ** 2

def cube(x):
    return x ** 3

nums = [5, 2, 7 ,1, 6, 9, 0, 4, 2, 8, 4]

# 1 вариант
#for i in range(len(nums)):
#    nums[i] = squere(nums[i])

# 2 вариант
#nums = [squere(el) for el in nums]

# 3 вариант
nums = list(map(cube, nums))
print(nums)

