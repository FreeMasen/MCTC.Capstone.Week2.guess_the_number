import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'
error_text = 'Error, please enter in a whole number!'

def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    while True:
        try:
            return int(input('Guess the secret number? '))
        except ValueError as e:
            print(error_text)

def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)
    print('I am going to pick a random number and then you need to guess it')
    print('I will let you know if your guess is too high or too low')
    guess_counter = 0
    while True:
        guess_counter += 1
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result + 'it took %s guesses' % guess_counter)

        if result == correct:
            break


if __name__ == '__main__':
    main()
