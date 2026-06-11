# 1. Head Recursion

# Jab recursive call function ke beginning me ho aur uske baad kuch work ho, to use Head Recursion kehte hain.

def fun(n):
    if n == 0:
        return

    fun(n - 1)   # Recursive call pehle
    print(n)     # Kaam baad me

fun(5)


# 2. Tail Recursion

# Jab recursive call last statement ho aur uske baad koi work na ho, to use Tail Recursion kehte hain.
print("\n TAIL Recursion :")
def fun(n):
    if n == 0:
        return

    print(n)     # Kaam pehle
    fun(n - 1)   # Recursive call last me

fun(5)