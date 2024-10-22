import datetime
import holidays

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')


def main():
    '''Lookup a calendar date.'''
    print('Text-Based Calendar Lookup.\n')

    while True:
        try:
            year = int(input('Enter the year (e.g. 2010): '))
            month = int(input('Enter the month (1-12): '))

            # Validate the month and year
            if not (1 <= month <= 12):
                raise ValueError('Month must be between 1 and 12.')
            if year < 1:
                raise ValueError('Year must be a positive integer')

            print(generate_calendar(year, month))

        except ValueError as e:
            print(f'Error: {e}\n')
        except Exception as e:
            print(f'Unexpected error: {e}\n')

        again = input('Press Enter to generate another calendar. '
                      'Enter (q)uit to exit: ').strip().lower()
        if again not in ('q', 'quit'):
            print()
            continue
        else:
            print('Exiting program...Bye!')
            break


def generate_calendar(year, month):
    '''Generates a text-based calendar for a given month and year.'''
    # Get holidays for the given year and month
    za_holidays = holidays.ZA(years=year)
    holiday_dates = {date: name for date, name in za_holidays.items()
                     if date.month == month}

    calendar_text = ''
    # Calendar title
    calendar_text += f' {MONTHS[month - 1]} {year}'.center(79) + '\n'
    # Calendar days of the week
    calendar_text += '...Sunday.....Monday....Tuesday...Wednesday...' \
        'Thursday....Friday....Saturday..\n'

    week_separator = ('+----------' * 7) + '+\n'  # Separator for weeks
    blank_row = ('|          ' * 7) + '|\n'  # Blank rows

    # Starting date for the first week
    try:
        current_date = datetime.date(year, month, 1)
    except ValueError as e:
        return f'Error: {e}'

    # Adjust to start at the beginning of the week (Sunday)
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:  # Generate calendar for each week
        calendar_text += week_separator
        day_row = ''
        for i in range(7):
            day_label = str(current_date.day).rjust(3)
            if current_date in holiday_dates:  # Mark holidays
                day_label = str(current_date.day).rjust(2) + '*'

            day_row += '|' + day_label + (' ' * 7)
            current_date += datetime.timedelta(days=1)
        day_row += '|\n'

        calendar_text += day_row
        for _ in range(3):
            calendar_text += blank_row

        if current_date.month != month:
            break

    calendar_text += week_separator

    # Add holiday names at the bottom
    if holiday_dates:
        calendar_text += f'\nHolidays {MONTHS[month - 1]}:\n'
        for date, name in sorted(holiday_dates.items()):
            calendar_text += f'{date.day:2d} {MONTHS[date.month - 1]}: '\
                f'{name}\n'

    return calendar_text


if __name__ == '__main__':
    main()
