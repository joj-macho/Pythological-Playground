import calendar


def main():
    '''Main function for displaying a calendar based on user input.'''

    print('\nText-based Calendar Maker - Version 2.\n')

    # Prompt user to choose between yearly or monthly calendar
    while True:
        response = input(
            'Select option to display:\nEnter 1 to show year only.\nEnter 2 to show year and month.\n> ')
        if response in ['1', '2']:
            opt = int(response)
            break
        else:
            print('Enter A Valid Integer Option!!')

    if opt == 1:
        print('Yearly Calendar Display.')
        year_input = int(input('Enter the Calendar Year to Display.\n> '))
        # Print the entire calendar for the given year
        print(calendar.calendar(year_input))

    elif opt == 2:
        print('Monthly Calendar Display.')
        year_input = int(input('Enter the Calendar Year to Display.\n> '))
        month_input = int(input('Enter the Calendar Month (1-12) to Display.\n> '))
        # Print the calendar for the given month and year
        print(calendar.month(year_input, month_input))


if __name__ == '__main__':
    main()
