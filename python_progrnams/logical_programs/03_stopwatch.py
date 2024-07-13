import time
if __name__ == "__main__":
    while True:
        input("Press Enter to start StopWatch")
        start_time = time.time()
        input("Press Enter to stop StopWatch")
        print(f'elaps time = {(time.time()- start_time):.2f} seconds')
        break