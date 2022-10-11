number_list = [2, 33, 54, 2.43]
print(number_list)

some_list = [12,  34.56, 'jjee']
print(some_list)
print(len(number_list))
print(len(some_list))
print(some_list[1:2])

some_list[2] = 'hi'
print(some_list)
# print(some_list + number_list)

some_list.append('I am ...')
print(some_list)

some_list.insert(2, 'You are ...')
print(some_list)

new_list = ['a', 't', 'l', 'b']

# removing
some_list.pop(3)
print(some_list)



deleted_item = some_list.pop()
print(some_list)
print(deleted_item)

some_list.remove(12)
print(some_list)

new_one_list = new_list.copy()
print(new_one_list)

new_list.sort()
print(new_list)

new_list.reverse()
print(new_list)

new_one_list.append(some_list)
print(new_one_list)

