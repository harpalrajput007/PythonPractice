from datetime import datetime

now = datetime.now()
time = now.strftime("%H:%M:%S")

print(time)

if "04:00:00" <= time <= "11:59:00":
    print("Good morning!")
elif "12:00:00" <= time <= "15:59:00":
    print("Good afternoon!")
elif "16:00:00" <= time <= "20:59:00":
    print("Good evening!")
else:
    print("Good night!")