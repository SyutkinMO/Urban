immutable_var = (1, 2.98, 'Potato', ['word', 8, True], True,'Table, False')
print(immutable_var)
print(type(immutable_var))
immutable_var[3][0:2]= [1]
print(immutable_var)

mutable_list = [1, 0, True, 'medicine']
print(mutable_list)
mutable_list[0] = 3, 4.12
print(mutable_list)
mutable_list.remove((3, 4.12))
print(mutable_list)
mutable_list.insert(1, False)
print(mutable_list)
print(0 in mutable_list)
mutable_list[0]=880
print(mutable_list)
print(mutable_list[::-1])