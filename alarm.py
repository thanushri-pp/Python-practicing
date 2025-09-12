import time

print("⏰ Welcome to the Bruh Alarm Clock ⏰")

alarm_time = input("Set alarm time in HH:MM (24hr format): ")

print(f"Alarm set for {alarm_time}, bruh. Don’t oversleep 😴")

while True:
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
        print("WAKE UP BRUH 💀💀💀")
        break
    time.sleep(30)  # check every 30 seconds
