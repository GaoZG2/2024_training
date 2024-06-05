users = ['admin', 'gzg', 'jjb', 'ztl', 'fyk']
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')
else:
    print('The list is empty.')