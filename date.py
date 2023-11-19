import argparse
from datetime import datetime, timedelta
import os
from pathlib import Path
import sys

def current_date():
    today = datetime.now()
    print(f"Today's date is: {today.strftime('%Y-%m-%d')}")

def current_day():
    today= datetime.now()
    print(f"Current day: {today.strftime('%A')}")

def leap_year():
    year = datetime.now().year
    if(year %4 ==0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

def difference(date1):
    try:
        date1 = datetime.strptime(date1, '%Y-%m-%d')
        today = datetime.now()
        difference =  date1 - today
        print(f"Difference between {date1.strftime('%Y-%m-%d')} and today: {difference.days} days")
    except Exception as e:
        print(f"{e}{date1}invalid date. Please enter a valid date")
        sys.exit(1)

def main():

    parser = argparse.ArgumentParser(description="Performing date command line Integration utilities from file or from the standard input(STDIN)")
    # parser.add_argument("input_file", nargs='?',type = argparse.FileType("r"),default= sys.stdin, help = "Read input from satndard input(stdin)")
    parser.add_argument('-c','--current_date',help='Print current date', action ='store_true')
    parser.add_argument('-t','--current_day',help='Print current date', action ='store_true')
    parser.add_argument('-l', '--leap_year',help ='print leap year', action ='store_true')
    parser.add_argument('-d','--date_difference', help ='print difference between dates')

    arguments=  parser.parse_args()
    # print(arguments)
    
    if arguments.current_date:
        current_date()

    if arguments.current_day:
        current_day()    

    if arguments.leap_year:
        leap_year()

    if arguments.date_difference:
        difference(arguments.date_difference)
    
if __name__ == "__main__":
    main()