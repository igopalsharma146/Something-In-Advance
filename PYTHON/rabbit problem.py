# rabbit problem
def rabbit_problem(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return rabbit_problem(n - 1) + rabbit_problem(n - 2)
n = int(input("Enter the number of months: "))
print("Number of rabbit pairs after", n, "months:", rabbit_problem(n))


# [1,2,3] => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print("\nGenerating subsets for [1, 2, 3]:")
def generate_subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    backtrack(0, [])
    return result
nums = [1, 2, 3]
print("Subsets:", generate_subsets(nums))