lis = ['gzg', 'jjb', 'ztl', 'fyk', 'ztm']
for l in lis:
    print(f'{l.title()}, I sincerely invite you to join the party.')
print('Find a larger dining table!')
lis.insert(0, 'wst')
lis.insert(len(lis) // 2, 'dqy')
lis.append('cls')
for l in lis:
    print(f'{l.title()}, I sincerely invite you to join the party.')
print('Sorry, only two guests can be invited because the newly purchased table cannot be delivered in time.')
while(len(lis) > 2):
    guest = lis.pop()
    print(f"{guest}, I'm sorry to inform you that I won't be albe to invite you.")
for guest in lis:
    print(f"{guest}, you are still on the invite list.")
while(len(lis) > 0):
    del lis[-1]
print(lis)