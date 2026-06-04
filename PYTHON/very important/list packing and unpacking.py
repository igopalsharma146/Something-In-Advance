# list packing and unpacking
# List packing is the process of creating a list by combining multiple values into a single list.
# List unpacking is the process of extracting values from a list and assigning them to individual variables.
# List packing
packed_list = [1, 2, 3, 4, 5]
print("Packed list:", packed_list)

# List unpacking
a, b, c, d, e = packed_list
print("Unpacked values:", a, b, c, d, e)

# List unpacking with * operator
a, *b, c = packed_list
print("Unpacked values with * operator:", a, b, c)

# List unpacking with * operator and ignoring values
a, *_, c = packed_list
print("Unpacked values with * operator and ignoring values:", a, c)

