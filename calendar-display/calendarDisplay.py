import datetime

# Calendar day and month constant
MONTHS = ('Janaury', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

def main():
    '''This is the main function. It prompts the user to enter a year and a month, then generates and displays a text-based calendar.'''


    print('''
Text-based Calendar Maker.
    ''')

    # prompt user for month and year to display
    while True:
        response = input('Enter a Calendar Year:\n> ')
        # year must be decimal, > 0, and contain 4 digits??
        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break
        else:
            print('Enter a valid Calendar Year!')
            continue
    
    while True:
        response = input('Enter a Calendar Month:\n> ')
        if not response.isdecimal():
            continue
        month = int(response)
        if 1 <= month <= 12:
            break
        print('Please enter a valid number representing Calendar Month')

    # Generate Text Calendar and show it
    display_calendar = generate_calendar(year, month)
    print(display_calendar)

def generate_calendar(year, month):
    '''This function takes in the year and month and returns a printable text calendar.'''
    
    calendar_text = ''
    # Calendar Title
    calendar_text += (' '*34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    # Calendar days of the week
    calendar_text += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    # Seperate weeks with horizontal rule
    separate_weeks = ('+----------' * 7) + '+\n'
    # blank Rows
    blank_row = ('|          ' * 7) + '|\n'
    # date
    current_date = datetime.date(year, month, 1)
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)
    # for each week of the month
    while True:
        calendar_text += separate_weeks
        day_row = ''
        for i in range(7):
            day_label = str(current_date.day).rjust(2)
            day_row += '|' + day_label + (' '*8)
            current_date += datetime.timedelta(days=1)
        day_row += '|\n'

        calendar_text += day_row
        for i in range(3):
            calendar_text += blank_row

        if current_date.month != month:
            break

    calendar_text += separate_weeks
    return calendar_text

if __name__ == '__main__':
    main()
