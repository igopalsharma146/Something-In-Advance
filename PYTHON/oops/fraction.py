class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        # return Fraction(new_numerator, new_denominator)
        # hum yaha par simplyfy kar sakte hain, taki humare result me numerator aur denominator me common factor na ho. iske liye hum gcd (greatest common divisor) function ka use kar sakte hain.
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        common_divisor = gcd(new_numerator, new_denominator)
        new_numerator //= common_divisor
        new_denominator //= common_divisor
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        # return Fraction(new_numerator, new_denominator)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        common_divisor = gcd(new_numerator, new_denominator)
        new_numerator //= common_divisor
        new_denominator //= common_divisor
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        # return Fraction(new_numerator, new_denominator)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        common_divisor = gcd(new_numerator, new_denominator)
        new_numerator //= common_divisor
        new_denominator //= common_divisor
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        # return Fraction(new_numerator, new_denominator)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        common_divisor = gcd(new_numerator, new_denominator)
        new_numerator //= common_divisor
        new_denominator //= common_divisor
        return Fraction(new_numerator, new_denominator)
x=Fraction(1, 2)
y=Fraction(3, 4)
print("x:", x)
print("y:", y)
# jab hum kisi object ko print karte hain to wo uske __str__ method ko call karta hai, aur uska return value print karta hai. isliye humne __str__ method ko define kiya hai taki jab hum Fraction object ko print kare to wo numerator/denominator format me print ho.

print("x + y:", x + y)
# jab hum x + y karte hain to wo x ke __add__ method ko call karta hai aur y ko as an argument pass karta hai. isliye humne __add__ method ko define kiya hai taki jab hum Fraction object ko add kare to wo numerator/denominator format me return ho.

print("x - y:", x - y)
# jab hum x - y karte hain to wo x ke __sub__ method ko call karta hai aur y ko as an argument pass karta hai. isliye humne __sub__ method ko define kiya hai taki jab hum Fraction object ko subtract kare to wo numerator/denominator format me return ho.

print("x * y:", x * y)
# jab hum x * y karte hain to wo x ke __mul__ method ko call karta hai aur y ko as an argument pass karta hai. isliye humne __mul__ method ko define kiya hai taki jab hum Fraction object ko multiply kare to wo numerator/denominator format me return ho.

print("x / y:", x / y)
# jab hum x / y karte hain to wo x ke __truediv__ method ko call karta hai aur y ko as an argument pass karta hai. isliye humne __truediv__ method ko define kiya hai taki jab hum Fraction object ko divide kare to wo numerator/denominator format me return ho.



#agar hame ese or bhi method define karne h to hum easily kar sakte hain, jaise ki __eq__ method ko define karne se hum Fraction object ko compare kar sakte hain, ya __lt__ method ko define karne se hum Fraction object ko less than operator ke sath compare kar sakte hain. is tarah se hum apne class me jitne bhi method chahte hain define kar sakte hain, aur unhe use kar sakte hain.
#agar hame ye sab method dekhne h to hum dir() function ka use kar sakte hain, jo ki ek object ke sabhi attributes aur methods ko list me return karta hai. is tarah se hum apne class ke sabhi method ko dekh sakte hain, aur unhe use kar sakte hain.

print(dir(x))

# inhe ham magic methods kehte hain, kyunki ye methods python ke built-in methods hote hain, aur inhe hum apne class me define kar sakte hain taki jab hum apne class ke object ke sath kisi operator ka use kare to wo automatically call ho jaye. is tarah se hum apne class ke object ke sath operator overloading kar sakte hain, aur apne class ke object ke sath kisi bhi operator ka use kar sakte hain.