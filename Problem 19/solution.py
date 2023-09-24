"""
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import time
start_time = time.time()

counter = 0

dow = 2 # Start with 01/01/1901, a Tuesday (treat Sunday as the 0th day of the week)

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(25): # 25 sets of 4 years (3 normal years + 1 leap year)
    for j in range(3): # The 3 normal years
        for num in days_in_month:
            dow = (dow + num) % 7 # See what day of the week the 1st of each month is
            if dow == 0: # If it's a Sunday, add 1 to the counter
                counter += 1
        
    for num in days_in_month_leap: # Same logic as above, but for leap years
        dow = (dow + num) % 7
        if dow == 0:
            counter += 1

print(counter)

end_time = time.time()

print(f"This solution took {(end_time - start_time):.6f}s to run")