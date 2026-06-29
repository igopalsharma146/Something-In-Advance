# Program: Generate Parentheses
n = int(input("Enter number of pairs of parentheses: "))


# Brute Force Approach (Generate All Binary Strings)

def is_valid(s):
    count = 0
    for ch in s:
        if ch == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False
    return count == 0


print("\nBrute Force Approach")
result = []
def generate(curr):
    if len(curr) == 2 * n:
        if is_valid(curr):
            result.append(curr)
        return

    generate(curr + "(")
    generate(curr + ")")

generate("")

for ans in result:
    print(ans)
print("Total Valid Parentheses:", len(result))

print("Time Complexity: O(2^(2N) * N)")
print("Space Complexity: O(2^(2N) * N)")


# Better Approach
print("\nBetter Approach")
print("Not Applicable")

print("Time Complexity: N/A")
print("Space Complexity: N/A")


# Optimal Approach (Backtracking)
print("\nOptimal Approach")
result = []
def solve(open_count, close_count, curr):
    if len(curr) == 2 * n:
        result.append(curr)
        return

    # Add Opening Bracket
    if open_count < n:
        solve(open_count + 1,close_count,curr + "(")

    # Add Closing Bracket
    if close_count < open_count:
        solve(open_count,close_count + 1,curr + ")")

solve(0, 0, "")
for ans in result:
    print(ans)

print("Total Valid Parentheses:", len(result))
print("Time Complexity: O(4^N / √N)")
print("Space Complexity: O(N)")


        #             ""
        #           /
        #         (
        #       /   \
        #     ((     ()
        #      |      |
        #    (()     ()(
        #      |      |
        #   (())    ()()