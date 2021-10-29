# The Perfect Guess
import random
bot = random.randint(1, 100)
# print(bot)
a = None
counter = 0

while a != bot:
    a = int(input('Enter A Number : '))
    if a > bot:
        print('Guess Lower')
        counter += 1
    else:
        print('Guess Higher')
        counter += 1

if counter == 1:
    print(f'Congratulations The Number Was {a}, It took you 1 guess')
else:
    print(f'Yes The Number Was {a}, It took you {counter} guesses')

with open('highscore.txt', 'rt', encoding='Utf8') as f:
    f = f.read()
if f == '':
    with open('highscore.txt', 'wt', encoding='Utf8') as f:
        f.write(str(counter))
        print('Congratulations This Is A New Highscore')
elif int(f) > int(counter):
    with open('highscore.txt', 'wt', encoding='Utf8') as f:
        f.write(str(counter))
        print('Congratulations This Is A New Highscore')
