import random

def dice_sum():
    sum1 = 0
    sum2 = 0
    roll = 0
    # goal = 0
    
    goal = int(input('Desired dice sum: '))
    while goal < 2 or goal > 12:
        print('Not valid. Value must be between 2 and 12.')
        goal = int(input('Desired dice sum:'))
        
    while roll != goal:
        sum1 = random.randint(1, 6)
        sum2 = random.randint(1, 6)
        roll = sum1 + sum2
        print("{} and {} = {}".format(sum1, sum2, roll))
        
    
        
dice_sum()
        