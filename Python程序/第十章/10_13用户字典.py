from pathlib import Path
import json

path = Path('user_info.json')
if path.exists():
    contents = path.read_text()
    user_info = json.loads(contents)
    print(f"I know your following information: {[value for value in user_info.keys()]}")
else:
    username = input("What is your name? ")
    place = input("Where do you live? ")
    school = input("Which school do you study in? ")
    dic = {}
    dic['username'] = username
    dic['place'] = place
    dic['school'] = school
    contents = json.dumps(dic)
    path.write_text(contents)
    print(f"{username}, all your information has been recorded!")