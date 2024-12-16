import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end='\r')  # \r moves the cursor back to the beginning of the line
        time.sleep(1)
        seconds -= 1
    print("Time's up!")  # Corrected the print statement

seconds = int(input('Enter the time in seconds: '))
countdown_timer(seconds)
