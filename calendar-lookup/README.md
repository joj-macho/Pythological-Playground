# Calendar Lookup

## Description 

The Calendar Lookup program generates a text-based calendar for a specific year and month, and marks holidays (if any) on the calendar. 

## How it Works

- Enter the year and month.
- The program will create a text-based calendar for the specified month and year.
- The program retrieves holidays for the specified year using the `holidays` library and filters them to include only those in the specified month.

Intall the `holidays` library with `python3 -m pip install holidays`

## Running the Program

```bash
# Navigate to the project directory
cd calendar-lookup/

# Run the main script
python3 calendar_lookup.py
```

## Program Input & Output

When you run `calendar_lookup.py`, the output will look like this:

```
Text-Based Calendar Lookup.

Enter the year (e.g. 2010): 2010
Enter the month (1-12): 12
                                  December 2010                                
...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..
+----------+----------+----------+----------+----------+----------+----------+
| 28       | 29       | 30       |  1       |  2       |  3       |  4       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|  5       |  6       |  7       |  8       |  9       | 10       | 11       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 12       | 13       | 14       | 15       |16*       | 17       | 18       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 19       | 20       | 21       | 22       | 23       | 24       |25*       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|26*       |27*       | 28       | 29       | 30       | 31       |  1       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+

Holidays December:
16 December: Day of Reconciliation
25 December: Christmas Day
26 December: Day of Goodwill
27 December: Day of Goodwill (observed)

Enter (q)uit to exit. Press Enter to generate another calendar: 

Enter the year (e.g. 2010): 2010
Enter the month (1-12): 5
                                    May 2010                                   
...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..
+----------+----------+----------+----------+----------+----------+----------+
| 25       | 26       | 27       | 28       | 29       | 30       | 1*       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|  2       |  3       |  4       |  5       |  6       |  7       |  8       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|  9       | 10       | 11       | 12       | 13       | 14       | 15       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 16       | 17       | 18       | 19       | 20       | 21       | 22       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 23       | 24       | 25       | 26       | 27       | 28       | 29       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 30       | 31       |  1       |  2       |  3       |  4       |  5       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+

Holidays May:
 1 May: Workers' Day

Enter (q)uit to exit. Press Enter to generate another calendar: 

Enter the year (e.g. 2010): 2010
Enter the month (1-12): 12
                                  December 2010                                
...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..
+----------+----------+----------+----------+----------+----------+----------+
| 28       | 29       | 30       |  1       |  2       |  3       |  4       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|  5       |  6       |  7       |  8       |  9       | 10       | 11       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 12       | 13       | 14       | 15       |16*       | 17       | 18       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 19       | 20       | 21       | 22       | 23       | 24       |25*       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|26*       |27*       | 28       | 29       | 30       | 31       |  1       |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+

Holidays December:
16 December: Day of Reconciliation
25 December: Christmas Day
26 December: Day of Goodwill
27 December: Day of Goodwill (observed)

Enter (q)uit to exit. Press Enter to generate another calendar: q
Exiting program...Bye!
```