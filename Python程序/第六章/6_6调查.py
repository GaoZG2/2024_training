favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
lists = ['sarah', 'gzg']
for l in lists:
    if l in favorite_languages.keys():
        print(f'{l}, Thanks for accepting our survey!')
    else:
        print(f'{l}, We hope you will accept our survry!')