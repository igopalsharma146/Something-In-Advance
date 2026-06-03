class Gcd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_gcd(self):
        while self.b:
            self.a, self.b = self.b, self.a % self.b
        return self.a
x=Gcd(48, 18)
print(x.calculate_gcd())

class Lcm:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_lcm(self):
        gcd = Gcd(self.a, self.b).calculate_gcd()
        return (self.a * self.b) // gcd
y=Lcm(48, 18)
print(y.calculate_lcm())