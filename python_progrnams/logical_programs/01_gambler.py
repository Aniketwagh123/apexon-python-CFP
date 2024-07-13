import random


def gamble(stake: int, goal: int, number_of_times: int):
    balence = stake
    win_count = 0
    bets_count = 0
    fair = 1
    while not balence<=0 and not balence >= goal:
        bets_count += fair
        is_win: bool = random.choice([True, False])
        if is_win:
            win_count += 1
            balence += fair
        else:
            balence -= fair
    win_percentage = (win_count/bets_count)*100
    return win_count, win_percentage


if __name__ == "__main__":
    try:
        stake: int = int(input("Enter the stake: "))
        goal: int = int(input("Enter the goal: "))
        number_of_times: int = int(input("Enter the number of time: "))
    except (ValueError):
        print("enter propper intiger values.")
        exit(1)

    
    win_avg = -1
    win_avg_percentage = -1

    for i in range(number_of_times):
        win_count, win_percentage = gamble(stake, goal, number_of_times)
        print(f'for try:{i+1} win_count = {win_count} and win_percentage = {win_percentage}')

        if win_avg == -1:
            win_avg = win_count
            win_avg_percentage = win_percentage
        else:
            win_avg = (win_avg + win_count)/2
            win_avg_percentage = (win_avg_percentage + win_percentage)/2

    print(f'Aavrage of all {number_of_times} times: win avrage count = {win_avg} and win avrage percentage = {win_avg_percentage}')
