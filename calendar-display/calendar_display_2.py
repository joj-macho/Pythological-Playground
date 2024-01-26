import calendar

def main():
    '''Main function for displaying a calendar based on user input.'''
    print('\nText-based Calendar Maker - Version 2.\n')

    while True:
        response = input(
            'Select option to display:\nEnter 1 to show year only.\nEnter 2 to show year and month.\n> ')
        if response in ('1', '2'):
            response = int(response)
            break
        else:
            print('Enter A Valid Integer Option!!')

    if response == 1:
        print('Yearly Calendar Display.')
        year_input = int(input('Enter the Calendar Year to Display.\n> '))
        print(calendar.calendar(year_input))

    elif response == 2:
        print('Monthly Calendar Display.')
        year_input = int(input('Enter the Calendar Year to Display.\n> '))
        month_input = int(input('Enter the Calendar Month (1-12) to Display.\n> '))
        print(calendar.month(year_input, month_input))

if __name__ == '__main__':
    main()
