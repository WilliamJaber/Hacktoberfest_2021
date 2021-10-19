from random import randint
import sys

print('\nHELLO')
def main():
    ''' Structure of possible answers, a standard Magic 8 Ball has 20 possible answers,
    including 10 affirmative answers, 5 non-committal answers and 5 negative answers. '''

    while True:
        random_number = randint(1, 20)
        user_question = input('Please, make your question:\n> ')

        answers = {
            1: 'It is certain.',
            2: 'It is decidedly so.',
            3: 'Without a doubt.',
            4: 'Yes definitely.',
            5: 'You may rely on it.',
            6: 'As I see it, yes.',
            7: 'Most likely.',
            8: 'Outlook good.',
            9: 'Yes.',
            10: 'Signs point to yes.',
            11: 'Reply hazy, try again.',
            12: 'Ask again later.',
            13: 'Better not tell you now.',
            14: 'Cannot predict now.',
            15: 'Concentrate and ask again.',
            16: "Don't count on it.",
            17: 'My reply is no.',
            18: 'My sources say no.',
            19: 'Outlook not so good.',
            20: 'Very doubtful.'
}

        if len(user_question) < 3:
            play_again()

        print(answers[random_number])
        play_again()

def play_again():
    """Handles play again option"""
    while True:
        option = input('\nWould you like to ask again?! (yes or no): ')
        if option not in ['yes', 'no']:
            print('invalid option!')
            continue
        else:
            break
    if option == 'yes':
        return main()
    else:
        print('Thanks for playing - Goodbye!')
        sys.exit()


if __name__ == '__main__':
     main()
