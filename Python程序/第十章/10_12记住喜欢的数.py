from pathlib import Path
import json

path = Path('favorite_number.json')
if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f'Your favorite number is {number}!')
else:
    number = input('Please input your favorite number: ')
    contents = json.dumps(int(number))
    path.write_text(contents)