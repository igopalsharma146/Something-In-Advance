def mera_khud_ka_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            print(item)
        except StopIteration:
            break
l = [1, 2, 3, 4, 5]
m=(1, 2, 3, 4, 5)
n={'a':1,'b':2,'c':3,'d':4,'e':5}
o='Hello'
mera_khud_ka_for_loop(l)
mera_khud_ka_for_loop(m)
mera_khud_ka_for_loop(n)
mera_khud_ka_for_loop(o)