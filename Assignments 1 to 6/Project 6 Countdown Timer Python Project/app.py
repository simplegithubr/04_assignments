
import time

def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"{mins:02d}:{secs:02d}")
        time.sleep(1)
    print("00:00")
    print("Time's up! ⏰")
try:
   total_seconds = int(input("Enter time in seconds: "))
   countdown_timer(total_seconds)
except ValueError:
   print("Invalid input! Please enter a valid number.")
if __name__ == "__main__":
    countdown_timer()  


   