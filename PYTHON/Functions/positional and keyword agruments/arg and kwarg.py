print("taking infinite no. of keyword argument :")
print("\n\n **kwarg :")
def keyword_arg(**kwarg):
    print(type(kwarg))
    print(kwarg)
keyword_arg(a=1,b=2,c=30,d="go")

print("\n taking infinite no. of positional argument :")
def arg(*arg):
    print(type(arg))
    print(arg)
arg(1,2,"gopal","hello",[1,2,3])