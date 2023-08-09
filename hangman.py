import random

words = ("king", "butcher", "executioner", "assasin", "murderer", "rural", "urban", "city", "town", "farm")
answer = words[random.randint(0, len(words) - 1)]
# print(answer)

chances = 5 # increase or decrease chances if wanted

x = '_' * len(answer)
print(f'Answer is a {len(answer)} letter word: {x}')

while True:
    while True:
        index = float(input('which underscore do you want to guess for?: '))
        index = int(index)
        if index > 0 and index <= len(answer):
            break

    while True:
        letter = input('Guess the letter: ').lower()
        if len(letter) == 1:
            print()
            break
    
    x = list(x)
    x[index - 1] = letter
    string = ''
    for i in x:
        string += i

    print(f'Answer is a {len(answer)} letter word: {string}')

    if string[index - 1] == answer[index - 1]:
        print('------ Correct! ------')
        print(f'You have {chances} guess/s remaining.')
        print()
    else:
        chances -= 1
        print('------ Wrong! ------')
        print(f'You have {chances} guess/s remaining.')
        print()

    if string == answer:
        print('You Win!')
        break
    elif chances == 0:
        print(f"You lose! the word was '{answer}' not '{string}'")
        break