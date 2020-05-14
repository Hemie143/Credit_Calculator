import string
line = input()
for c in line:
    if c in 'aeiou':
        print('vowel')
    elif c in string.ascii_lowercase:
        print('consonant')
    else:
        break
