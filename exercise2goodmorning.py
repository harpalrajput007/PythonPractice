# from datetime import datetime
import time

# now = datetime.now()
time = time.strftime("%H:%M:%S")

print(time)

if "04:00:00" <= time <= "11:59:00":
    print("Good morning!")
elif "12:00:00" <= time <= "15:59:00":
    print("Good afternoon!")
elif "16:00:00" <= time <= "20:59:00":
    print("Good evening!")
else:
    print("Good night!")