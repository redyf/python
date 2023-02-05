import time

print("Welcome to pomodoro, the most loved studying technique!")

question = input("Would you like to start? ")
if question in ["yes", "y", "sim", "s"]:
    timer = input("Great! What's the timer? ")
    print(f"Starting pomodoro for {timer} minutes...")
    timer = float(timer) * 60
    start_time = time.time()
    end_time = start_time + timer
    while time.time() < end_time:
        time_left = end_time - time.time()
        print(f"Time left: {int(time_left)} seconds", end="\r")
        # \r faz o texto sobrepor a si mesmo na mesma linha para dar o efeito de cooldown
        time.sleep(1)
    print("Time is up!")

print("Your session has ended, would you like to start a new pomodoro?")
