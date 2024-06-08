from pathlib import Path
import json

path = Path('favorite_number.json')
number = input('What is favorite number?')
contents = json.dumps(int(number))
path.write_text(contents)

contents = path.read_text()
num = json.loads(contents)
print(f'I know your favorite number! It is {num}')