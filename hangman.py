from random import choice

words = ['python', 'java', 'kotlin', 'javascript']
alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
guess = choice(words)
hide_word = '-' * (len(guess))
attempts = 8
letters = []
gameState = 'play'

print('H A N G M A N')
gameState = input('Type "play" to play the game, "exit" to quit: ')
while gameState == 'play':
        while attempts > 0:
            print('\n' + hide_word)
            letter = input('Input a letter: ')
            #if letter in guess:
            letters.append(letter)
            i = 0
            while i < len(guess):
                if len(letter) > 1:
                    print('You should input a single letter')
                    #attempts -= 1
                    if attempts < 1:
                        print('You are hanged!')
                    break
                elif letter not in alphabet:
                    print('It is not an ASCII lowercase letter')
                    #attempts -= 1
                    if attempts < 1:
                        print('You are hanged!')
                    break
                elif letters.count(letter) > 1:
                    print('You already typed this letter')
                    #attempts -= 1
                    if attempts < 1:
                        print('You are hanged!')
                    break
                elif letter not in guess:
                    print('No such letter in the word')
                    attempts -= 1
                    if attempts < 1:
                        print('You are hanged!')
                    break
                elif letter == guess[i]:
                    temp = list(hide_word)
                    temp[i] = letter
                    hide_word = ''.join(temp)
                i += 1
            if hide_word.isalpha():
                print('You guessed the word!\nYou survived!')
                break
            #reset game
        if input('\nType "play" to play the game, "exit" to quit: ') == 'play':
            guess = choice(words)
            hide_word = '-' * (len(guess))
            attempts = 8
            letters = []
        else:
            break
