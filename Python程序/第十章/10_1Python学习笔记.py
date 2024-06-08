from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

print(contents)

lines = contents.splitlines()
lis = []
for line in lines:
    lis.append(line)
print(lis)