import random as r
import matplotlib.pyplot as plt

def roll_dice_sum(dices):
    total = 0
    for i in range(dices):
        digit = r.randint(1,6)
        total += digit

    return total


def simulate_dice_sum(num_dice, num_trials):
    total_sum = []
    for i in range(num_trials):
        total_sum.append(roll_dice_sum(num_dice))
    
    return total_sum

def simulate_dice_sum_hist(num_dice, num_trials):
    
    max_sum = num_dice * 6
    
    hist = [0] * (max_sum + 1)

    for _ in range(num_trials):
        dice_sum2 = sum(r.randint(1,6) for _ in range(num_dice))
        hist[dice_sum2] += 1

    for k in range(len(hist)):
        hist[k] /= num_trials

    return hist


    
nbr_of_dice = int(input('How many dice do you want to throw: '))
nbr_attempt = int(input('How many attempts? '))



y = simulate_dice_sum_hist(nbr_of_dice, nbr_attempt)
x = [i for i in range(len(y))]
plt.bar(x, y, tick_label = x)
plt.show()


