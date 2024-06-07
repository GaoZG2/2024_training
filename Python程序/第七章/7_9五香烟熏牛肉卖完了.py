sandwich_orders = ['s1',  'pastrami', 's2',  'pastrami', 's7',  'pastrami', 's5']
print('pastrami is sold out!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sanwiches = []
for sandwich in sandwich_orders:
    finished_sanwiches.append(sandwich)
    print(f'I made your {sandwich} sandwich.')
print('All sandwichs are finished: ', finished_sanwiches)