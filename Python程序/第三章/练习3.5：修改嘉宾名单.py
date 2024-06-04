lis = ['gzg', 'jjb', 'ztl', 'fyk', 'ztm']
for l in lis:
    print(f'{l.title()}, I sincerely invite you to join the party.')
print('fyk')
lis[lis.index('fyk')] = 'lll'
for l in lis:
    print(f'{l.title()}, I sincerely invite you to join the party.')