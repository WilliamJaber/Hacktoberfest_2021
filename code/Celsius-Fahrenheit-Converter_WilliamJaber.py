import sys

print('\nWelcome to your Celsius and Fahrenheit Converter.')

def main():
    """Converter of Celsius to Fahrenheit and viceversa"""
    while True:
        converter_type = input('\nDo you want to convert Celsius or Fahrenheit? Insert (C or F):\n> ')
        if converter_type.lower() not in ['c', 'f']:
            print('invalid Input')
            new_conversion()
        if converter_type[0].lower() == 'c':
            celsius_to_fahrenheit()
            new_conversion()
        else:
            fahrenheit_to_celsius()
            new_conversion()

def celsius_to_fahrenheit():
    temp_degree = int(input('\nInsert temperature:\n> '))
    result_in_F = (temp_degree * 9/5) + 32
    print(f'\n{temp_degree}°C equals to {result_in_F:.2f}°F')

def fahrenheit_to_celsius():
    temp_degree = int(input('\nInsert temperature:\n> '))
    result_in_C = (temp_degree - 32) * 5/9
    print(f'\n{temp_degree}°F equals to {result_in_C:.2f}°C')

def new_conversion():
    """Handles new conversion option."""
    while True:
        option = input('\nDo you want make a new conversion? (yes or no): ')
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
