current_users = ['admin', 'Gzg', 'jjb', 'ztl', 'fyk']
new_users = ['zwq', 'wst', 'gzg', 'dqy', 'jjb']
for nUser in new_users:
    if nUser.lower() in [value.lower() for value in current_users]:
        print('Please enter a different username.')
    else:
        print('This username is not in use.')
    