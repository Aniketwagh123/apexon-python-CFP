import random


def get_probablities(number_of_flips: int):
    '''
    Calculate percentage of Heads and Tails on coin flips.
    Input  : (int) number_of_flips : how mwny times coin get fliped.
    Returns: (float, float) probablities of head and tails.
    '''
    heads_count: int = 0
    tails_count: int = 0

    for _ in range(number_of_flips):
        if (random.random() < 0.5):
            tails_count += 1
        else:
            heads_count += 1

    return (tails_count/number_of_flips)*100, (heads_count/number_of_flips)*100


if __name__ == "__main__":
    number_of_flips = input()

    # Inpute validation
    if number_of_flips.isdigit() and int(number_of_flips) > 0:
        number_of_flips = int(number_of_flips)
        tails_probablity, head_probablity = get_probablities(number_of_flips)
        # print( {get_probablities.__doc__})
        print(
            f'Tails Probablity: {tails_probablity}% \nHead Probablity: {head_probablity}%')
    else:
        print(f'Error: invalid number {number_of_flips}')
