# Text-Based Calendar Display

## Description 

This program generates a text-based calendar for a given year and month. It prompts the user to enter a valid year and month, and then generates a calendar for that month and year. The calendar is displayed in the terminal window.

## How it Works

- The program uses the `datetime` module to handle dates and time. It defines two constant tuples, `MONTHS` and `DAYS`, to store the names of the months and days of the week, respectively.

### `calendar_display_1.py`

- The `main()` function prompts the user to enter a year and month, and then calls the `generate_calendar()` function with the specified `year` and `month` as arguments. The resulting calendar is then printed to the console.

- The `generate_calendar()` function takes in a year and month and returns a string representation of the corresponding calendar.
    - The function first generates a title for the calendar by concatenating the month and year, and then adds a row of days of the week (Sunday, Monday, Tuesday, etc.). The function then creates a separator for each week, a blank row for each day, and starts at the first day of the specified month. It then iterates over each week of the month, adding the day of the month to the appropriate day of the week. After each week, it adds three blank rows and continues until the last day of the month is reached. Finally, the function returns the entire string representation of the calendar.

### `calendar_display_2.py`

- The calendar program is a simple command-line calendar display application that prompts the user to either display a yearly or monthly calendar using the `calendar` module.

- The `main()` function prompts the user to select an option for displaying the calendar. If the user chooses to display the yearly calendar, the program prints the yearly calendar for that year using the `calendar.calendar()` function. If the user chooses to display the year and month, the program prints the monthly calendar for that year and month using the `calendar.month()` function.

## Program Input & Output

When you run `calendar_display_1.py`, the output will look like this:

```

Text-based Calendar Maker.
    
Enter a Calendar Year:
> 2020
Enter a Calendar Month:
> 2
                                  February 2020
...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..
+----------+----------+----------+----------+----------+----------+----------+
|26        |27        |28        |29        |30        |31        | 1        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 2        | 3        | 4        | 5        | 6        | 7        | 8        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 9        |10        |11        |12        |13        |14        |15        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|16        |17        |18        |19        |20        |21        |22        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|23        |24        |25        |26        |27        |28        |29        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
```

When you run `calendar_display_2.py`, the output will look like this:

```

Text-based Calendar Maker - Version 2.

Select option to display:
Enter 1 to show year only.
Enter 2 to show year and month.
> 1
Yearly Calendar Display.
Enter the Calendar Year to Display.
> 2022
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

```