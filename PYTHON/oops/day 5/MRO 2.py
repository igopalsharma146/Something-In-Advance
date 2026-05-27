#MRO
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        val = super().m1()+30
        return val
class C(B):
    def m1(self):
        val=self.m1()+20
        # yaha per recursion ho rahi hai, kyuki self obj1 hi h jo C class ka hai, to wo phir se C class ke m1 method ko call karega, aur ye process infinite loop me chala jayega. 
        return val
obj1= C()
print(obj1.m1())  # Output: 70