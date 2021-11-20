# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
from datetime import date


def current_date():
    today = date.today()
    print("Today's date:", today)

    d = today - date(day=20, month=11, year=2021)
    print(f"\nthis is: {d.days} days")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("You started at: 2021-11-20")
    current_date()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
