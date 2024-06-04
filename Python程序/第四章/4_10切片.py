lis = [value ** 3 for value in range(1, 11)]
print('The first three items in the list are:', lis[:3])
print('Three items from the middle of the list are:', lis[len(lis) // 2 - 1: len(lis) // 2 + 2])
print('The last three items in the list are:', lis[-3 :])