lis = ['gzg', 'jjb', 'ztl', 'fyk', 'ztm']
for l in lis:
    print(f'{l.title()}, I sincerely invite you to join the party.')
print('Find a larger dining table!')
lis.insert(0, 'wst')
lis.insert(len(lis) // 2, 'dqy')
lis.append('cls')
for l in lis:
    print(f'{l.title()}, I sincerely invite you to join the party.')