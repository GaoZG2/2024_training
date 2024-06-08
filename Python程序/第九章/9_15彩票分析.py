import random

lis = [random.randint(0, 100) for _ in range(10)] + [chr(random.randint(65, 90)) for _ in range(5)]

my_ticket = [20, 31, 43, 88]

numbers = 0
while True:
    selected_elements = random.sample(lis, 4)
    numbers += 1
    flag = True
    if len(set(selected_elements)) != 4:
        continue
    for ele in selected_elements:
        if ele not in my_ticket:
            flag = False
            break
    if flag:
        print(f'Hit the jackpot after {numbers} cycles')
        break