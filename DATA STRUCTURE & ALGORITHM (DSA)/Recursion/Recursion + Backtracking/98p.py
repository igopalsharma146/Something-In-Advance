# Generate parentheses
# def parentheses(index,total,result):
#     if index >= len(brackets):
#         if total==0:
#             result.append("".join(brackets))
#             return
#     if total>len(brackets)//2:
#         return
#     elif total<0:
#         return
#     brackets[index]="("
#     sum=total+1
#     parentheses(index,sum,result)
#     brackets[index]=")"
#     sum=total-1
#     parentheses(index+1,sum,result)
# n=3
# brackets=[""] * n*2
# parentheses(0,0,[])

# Generate Parentheses using Balance

def parentheses(index, balance, result):
    if index == len(brackets):
        if balance == 0:
            result.append("".join(brackets))
        return

    if balance < 0:
        return

    if balance > len(brackets) - index:
        return

    brackets[index] = "("
    parentheses(index + 1, balance + 1, result)

    brackets[index] = ")"
    parentheses(index + 1, balance - 1, result)

n = 3
brackets = [""] * (2 * n)
result = []
parentheses(0, 0, result)
print(result)