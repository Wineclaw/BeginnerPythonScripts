def day_finder(day_num): # keep this to return day of week
    if day_num == 0:
          print("The day is Sunday")
    elif day_num == 1:
          print("The day is Monday")
    elif day_num == 2:
          print("The day is Tuesday")
    elif day_num == 3:
          print("The day is Wednesday")
    elif day_num == 4:
         print("The day is Thursday")
    elif day_num == 5:
         print("The day is Friday")
    elif day_num == 6:
        print("The day is Saturday")
    elif day_num >6:
        print("Number", day_num," is too high. Enter a number lower than 7")
# defs day_finder


day_left = int(input("What day are you leaving?"))
# ask for day number leaving, day_left

z = int(input("How many days will you be gone?"))
# ask for length of stay, stay_l

d = (day_left + z) % 7
# Since there are 7 days in a week, then this should leave the number you need
# to count ahead to arrive at the day of the week needed

day_finder(d)
