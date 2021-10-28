import sys

print('\nWelcome to your BMI calculator!!\n'
    'Please insert units expressed in centimeters, meters, and kilograms.')

def main():
    """Calculates your Body Mass Index (BMI) and classify according to the result."""
    while True:
        bmi = calculate_BMI()
        if bmi < 18.5:
            print(f'\nYour BMI is: {bmi:.2f} and is considered Underweight.')
        elif bmi < 25:
            print(f'\nYour BMI is: {bmi:.2f} and is considered Normal weight.')
        elif bmi < 30:
            print(f'\nYour BMI is: {bmi:.2f} and is considered Overweight.')
        else:
            print(f'\nYour BMI is: {bmi:.2f} and is considered Obese.')
        new_calculation()

def calculate_BMI():
    user_weight = int(input('\ninsert your weight:\n> '))
    user_height = float(input('\ninsert your height:\n> '))
    return user_weight / user_height ** 2

def new_calculation():
    """Handles new BMI calculation option."""
    while True:
        option = input('\nDo you want calculate your BMI again? (yes or no): ')
        if option not in ['yes', 'no']:
            print('invalid option!')
            continue
        else:
            break
    if option == 'yes':
        return main()
    else:
        print('Goodbye!')
        sys.exit()

if __name__ == '__main__':
     main()
