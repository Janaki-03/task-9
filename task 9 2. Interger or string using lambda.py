my_list = [1, 'hello', 42, 'world']

check_type = lambda x: isinstance(x, (int, str))

result = all(map(check_type, my_list))

if result:
    print("All elements in the list are integers or strings.")
else:
    print("Not all elements in the list are integers or strings.")
    