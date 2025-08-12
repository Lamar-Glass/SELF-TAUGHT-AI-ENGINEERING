# I will be building a count down timer from what i learned earlier.

import time

my_time = int(input("Enter the time in seconds: "))
message = str(input("Enter your name or anything you want to see during 'time is up': "))

print("NOTE: hold CTRL + C to cancel the timer.")

for x in reversed(range(0, my_time)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

# You can use this other way of reverse count down
#for x in (range(my_time, 0, -1)):
#    print(x)
#    time.sleep(1)


print(f"TIME IS UP! {message}")