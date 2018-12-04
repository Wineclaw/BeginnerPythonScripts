# Seconds to Hours/Minutes/Seconds
#
# Asks for seconds, then outputs how many hours, minutes and seconds
# that number of seconds make.
#
# By: Wineclaw, December 4 2018

total_secs = int(input("How many seconds do you have?"))
hours = total_secs // 3600
secs_remaining = total_secs % 3600
minutes = secs_remaining // 60
secs = secs_remaining % 60

print("Hours =", hours,
"Minutes =", minutes,
"Seconds =", secs)