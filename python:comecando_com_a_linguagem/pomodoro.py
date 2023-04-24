from tqdm import tqdm
import time

print("Welcome to pomodoro, the most loved studying technique!")

question = input("Would you like to start? ")
if question in ["yes", "y", "sim", "s"]:
    timer = input("Great! What's the timer? ")
    print("Invalid input. Please enter a number.")
    print(f"Starting pomodoro for {timer} minutes...")
    timer = float(timer) * 60
    minutes = timer
    start_time = time.time()
    end_time = start_time + timer
    with tqdm(
        total=timer,
        unit="s",
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}]",
    ) as pbar:
        while time.time() < end_time:
            time_left = end_time - time.time()
            pbar.update(1)
            pbar.set_description(
                f"Time left: {int(time_left / 60)} min {int(time_left % 60)} sec"
            )
            time.sleep(1)
    print("Time is up!")

print("Your session has ended, would you like to start a new pomodoro?")
