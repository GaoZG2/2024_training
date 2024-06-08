import random

lis = [random.randint(0, 100) for _ in range(10)] + [chr(random.randint(65, 90)) for _ in range(5)]

selected_elements = random.sample(lis, 4)
print(selected_elements)
