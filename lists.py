our_list = [27, 46, -5, 17, 9]
print(f'\nour_list = {our_list}')

print(f'\ntype(our_list) = {type(our_list)}')

jackson = ['A', 'B', 'C', 1, 2, 3, 'Do', 'Rey', 'Me', True, False]
print (f'\njackson[3], jackson[-2] = {jackson[3]}, {jackson[-2]}')

jack = jackson[3:6]
print (f'\njack = jackson[3:6], therefore jack = {jack}')

new_list = [1,23, 56, [-2,-675, -4], ['a', 'g']]
print (f'\nnew_list = {new_list}')

print ('\nHere\'s a slice from new_list. I will extract the second item of each inner list:')
print(f'Inner list item from new_list[3][1]: {new_list[3][1]}')
print(f'Inner list item from new_list[4][1]: {new_list[4][1]}')