# Opposite Day practice program

today_is_opposite_day = True

if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

# If it is opposite day, toggle say_it_is_opposite_day
if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day

# Now say what day it is
if say_it_is_opposite_day == True:
    print('Today is opposite day.')
else:
    print('Today is not opposite day.')