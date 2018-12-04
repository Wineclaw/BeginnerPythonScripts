# What time does the alarm go off?
#
# Find out when an alarm will go off, based on hours and 24HR format.
#
# By: Wineclaw
# December 4, 2018

# Asks for time now in 24HR format & number of hours to wait; breaks on float
time_now = int(input("What time is it now, in hours?"))
time_wait = int(input("How many full hours to wait?"))*100

# Finds out if any days have passed
days_past = (time_now + time_wait) // 2400

# The time when the alarm will go off, in 24HR format
alarm_time = ((time_now + time_wait) % 2400)

# Prints summary
print("The alarm will go off at",
    alarm_time, "hours,",
    days_past, "days from now.")