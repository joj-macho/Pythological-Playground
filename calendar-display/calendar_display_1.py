import datetime

# List of month and day names
MONTHS = ('Janaury', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

def main():
    '''Main function for generating and displaying a text-based calendar.'''


    print('\nText-based Calendar Maker.\n')

    # Prompt user for year and month
    while True:
        response = input('Enter a Calendar Year:\n> ')
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

    # Generate and display the text calendar
    display_calendar = generate_calendar(year, month)
    print(display_calendar)

def generate_calendar(year, month):
    '''Generate a printable text calendar based on year and month.'''
    
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

    # Adjust current_date to start with Sunday of the week
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    # For each week of the month...
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
