# Name: Isaac Francisco Marte
# Class: SDEV 300

# imported modules used by the functions within program
import math
import string
import secrets
from datetime import date


# function when called calculates volume of circular cylinder with values entered
def volume_of_cylinder():

    # catches any value error raised by invalid inputs by user that are non numeric
    try:
        # Application Title
        print('__________ Welcome To The Volume of Circular Cylinder Calculator__________')

        # Message to user to enter height of circular cylinder
        print('Enter height of circular cylinder')
        height = float(input())  # height variable for value entered by user

        # Message to user to enter radius of circular cylinder
        print('Enter the Radius of circular cylinder')
        radius = float(input())  # radius variable for value entered by user

        # Volume of Circular Cylinder = (πr2) × Height
        cylinder_volume = (math.pi * radius**2) * height

        # Formatted final output with values from user once all values are entered
        print('_______Volume of Circular Cylinder_______')
        print(f'Height: {height}')
        print(f'Radius: {radius}')
        print('Volume of Circular Cylinder: ' + '{:.{}f}'.format(cylinder_volume, 3) + '\n')

    except ValueError:
        print('Invalid Input! All inputs must be numeric\n')
        volume_of_cylinder()  # recalls the function after message


# when function is called the user enters the value for a triangle to get side c
def law_of_cosines():
    print('__________ Law of Cosines Application __________')
    print('Enter Side A/first of the triangle')
    side_a = float(input())  # side_a variable holds first side value entered

    print('Enter Side B/Second of the Triangle')
    side_b = float(input())  # side_b variable holds second side value entered

    print('Enter the Angle of Side C')
    angle = float(input())  # side_c variable holds angle value entered

    # sets side c variable to match formula c2 = a2 + b2 − 2abcos(C)
    side_c = math.sqrt(side_a**2 + side_b**2 - 2 * (side_a * side_b *
                                                    math.cos(angle * math.pi / 180)))

    # Formatted final output for user once all values are received
    print('')
    print(f'Angle: {angle} \n')
    print(f'Side A: {side_a}')
    print(f'Side B: {side_b}')
    print('Side C: ' + '{:.{}f}'.format(side_c, 3) + '\n')


# When function is called the number of days left until 7/4/2025 is printed to user
def days_until_independence_day_2025():
    # Variable set to current date of user, using date module's today function
    current_date = date.today()
    # Variable set to July,4,2025
    july_4_2025 = date(2025, 7, 4)
    # Subtracts the current date from 07/25 to calculate days
    days_left = (july_4_2025 - current_date).days

    # Formatted output with current time, expected time, and days remaining between both
    print('_____ How Many Days Until Independence Day 2025? _____')
    print(f'From: {current_date.strftime("%B, %d, %Y")}')
    print(f'To: {july_4_2025.strftime("%B, %d, %Y")}')
    print(f'Days Left: {days_left}\n')


# Takes a user input for numerator, denominator, and decimal place and calculates percentage
def calculate_and_format_percentage():

    # catches any type error or division by zero based on input from user using try & except
    try:

        # Application Title
        print('__________Welcome to The Percentage Calculator & Formatter__________\n')

        # Requests user to enter the numerator/actual value/part
        print('Enter the numerator of your percentage')
        numerator = float(input())  # stores input value as numerator variable

        # Requests user to enter the denominator/total value/whole
        print('Enter the Denominator of your percentage')
        denominator = float(input())  # stores input value as denominator variable

        # Requests user to enter the decimal places they desire for the final output
        print('Enter the number of decimal places your percentage should have')
        decimal_place = int(input())  # stores the input value as the decimal place variable

        # Percentage variable is value of numerator/ denominator entered times 100
        percentage = (numerator / denominator) * 100

        # Formatted final output which is set, based on decimal place
        print('Yield: ' + '{:.{}f}%'.format(percentage, decimal_place))
        print('')

    # sets types of errors that will be handled such as division by zero or type error
    except TypeError:
        # Message printed to user when type error exception is caught
        print('Input Entered must be numeric\n')

    except ZeroDivisionError:
        # Message printed to user when user tries to divide by zero
        print('Division By Zero is Not Permitted\n')


# function which allows user to generate a high, med, low, or numeric security password
def generate_secured_password():

    # runs a loop for function menu until a selection is made from the options
    while True:
        # Application Title
        print('__________Welcome to The Secured Password Generator__________\n')

        # message to user to enter the length of the password to generate
        print('Enter the length of Characters you would like to have for your new password')
        password_length = int(input())  # stores the password length entered
        print('')

        # if conditional checks the length of the password is b/w 4 to 64 before menu is presented
        if 4 <= password_length <= 64:
            # print statements which act as menu, allow user to enter complexity of password
            print('1. High Complexity Password ' + '(Includes Alphabetical Letters(Lower & Upper),' 
                                                   ' Numbers, and Special Characters)\n')
            print('2. Med Complexity Password ' + '(Includes Alphabetical Letters(Lower & Upper),' 
                                                  ' and Numbers)\n')
            print('3. Low Complexity Password ' + '(Includes Alphabetical Letters(Lower) Characters,' 
                                                  ' and Numbers)\n')
            print('4. All Numbers' + '(Includes Only Numbers)\n')
            print('9. Exit Application')
            selection = int(input())  # selection variable for user input as integer

            """ Within each conditional there is a password strength variable that uses the string
            module ASCII function to select the characters from upper to lower case letters, 
            numbers, and special characters """

            # if user enters #1 a High complexity password is generated with length given
            if selection == 1:
                password_strength = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(secrets.choice(password_strength) for i in range(password_length))
                print(password + '\n')
                main_menu()

            # else if user enters #2 a Med complexity password is generated with length given
            elif selection == 2:
                password_strength = string.ascii_letters + string.digits
                password = ''.join(secrets.choice(password_strength) for i in range(password_length))
                print(password + '\n')
                main_menu()

            # else if user enters #3 a Low complexity password is generated with length given
            elif selection == 3:
                password_strength = string.ascii_lowercase + string.digits
                password = ''.join(secrets.choice(password_strength) for i in range(password_length))
                print(password + '\n')
                main_menu()

            # else if user enters #4 Numeric password is generated with length given
            elif selection == 4:
                password_strength = string.digits
                password = ''.join(secrets.choice(password_strength) for i in range(password_length))
                print(password + '\n')
                main_menu()

            # else if user enters #9 a high complexity password is generated
            elif selection == 9:
                break

            # else if a invalid input is entered a message is displayed and function is recalled
            else:
                print('Invalid Input, \tTry Again!' + '\n')
                generate_secured_password()

        # if password length is not b/w 4 to 64 the menu is skipped and function is recalled
        else:
            print('Password must be between 4 to 64 characters long, Try Again!' + '\n')
            generate_secured_password()


# Function which acts as the menu pane to the user when app is running
def main_menu():

    # runs main menu until a selection is made from the options displayed below
    while True:
        print('__________ Welcome to The Deliverables Application __________\n')
        print('(Enter the number next to the application you would like to initiate'
              ' from 1-5, or 9 to exit program)')
        print('1. Generate Secure Password ')
        print('2. Calculate and Format a Percentage')
        print('3. How many days from today until July 4, 2025?')
        print('4. Use the Law of Cosines to calculate the leg of a triangle. ')
        print('5. Calculate the volume of a Right Circular Cylinder ')
        print('9. Exit Program')
        selection = int(input())  # selection variable given by user input as integer
        print('')  # line space/ whitespace

        # if user enters #1 the generate secured password function is called
        if selection == 1:
            generate_secured_password()

        # else if user enters #2 the calculate and format a percentage function is called
        elif selection == 2:
            calculate_and_format_percentage()

        # else if user enters #3 the days until independence day 2025 is called
        elif selection == 3:
            days_until_independence_day_2025()

        # else if user enters #4 the law of cosines function is called
        elif selection == 4:
            law_of_cosines()

        # else if user enters #5 volume of cylinder function is called
        elif selection == 5:
            volume_of_cylinder()

        # if #9 is entered the program will completely terminate
        elif selection == 9:
            print('Thank you for visiting Deliverables Application. '
                  'Come back and see us soon! ')
            break

        # Any input not within selection will result in this message displayed to user
        else:
            print('Invalid Input', '\ttry again!')


# Initiates the main function when program is first run
if __name__ == '__main__':
    main_menu()
