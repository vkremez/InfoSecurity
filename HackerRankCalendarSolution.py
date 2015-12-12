# Enter your code here. Read input from STDIN. Print output to STDOUT
# author = vkremez
# Solution: HackerRank
# String Splicing + Calendar/Datetime Module

import calendar
import datetime
N = raw_input()
N_month = int(N[0:2]) 
N_day = int(N[3:5])
N_year = int(N[6:10])
my_date = datetime.datetime(N_year, N_month,N_day)
day_of_week = str(calendar.day_name[my_date.weekday()].upper())
print(day_of_week)
