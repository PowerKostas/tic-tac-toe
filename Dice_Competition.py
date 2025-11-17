import random

def dice(player_1,player_2):
    min=1
    max=6
    roll_1=0
    roll_2=0
    while roll_1==roll_2:
        print('\nRolling for '+player_1+'...')
        print('\n'+player_1+' got a...')
        roll_1=random.randint(min,max)
        if roll_1==6:
            print(' _____')
            print('|●   ●|')
            print('|●   ●|')
            print('|●   ●|')
            print(' ‾‾‾‾‾')
        elif roll_1==5:
            print(' _____')
            print('|●   ●|')
            print('|  ●  |')
            print('|●   ●|')
            print(' ‾‾‾‾‾')
        elif roll_1==4:
            print(' _____')
            print('|●   ●|')
            print('|     |')
            print('|●   ●|')
            print(' ‾‾‾‾‾')
        elif roll_1==3:
            print(' _____')
            print('|●    |')
            print('|  ●  |') 
            print('|    ●|')
            print(' ‾‾‾‾‾')
        elif roll_1==2:
            print(' _____')
            print('|    ●|')
            print('|     |') 
            print('|●    |')
            print(' ‾‾‾‾‾')
        elif roll_1==1:
            print(' _____')
            print('|     |')
            print('|  ●  |') 
            print('|     |')
            print(' ‾‾‾‾‾')
        print('\nRolling for '+player_2+'...')
        print('\n'+player_2+' got a...')
        roll_2=random.randint(min,max)
        if roll_2==6:
            print(' _____')
            print('|●   ●|')
            print('|●   ●|')
            print('|●   ●|')
            print(' ‾‾‾‾‾')
        elif roll_2==5:
            print(' _____')
            print('|●   ●|')
            print('|  ●  |')
            print('|●   ●|')
            print(' ‾‾‾‾‾')
        elif roll_2==4:
            print(' _____')
            print('|●   ●|')
            print('|     |')
            print('|●   ●|')
            print(' ‾‾‾‾‾')
        elif roll_2==3:
            print(' _____')
            print('|●    |')
            print('|  ●  |') 
            print('|    ●|')
            print(' ‾‾‾‾‾')
        elif roll_2==2:
            print(' _____')
            print('|    ●|')
            print('|     |') 
            print('|●    |')
            print(' ‾‾‾‾‾')
        elif roll_2==1:
            print(' _____')
            print('|     |')
            print('|  ●  |') 
            print('|     |')
            print(' ‾‾‾‾‾')
        if roll_1==roll_2:
            print('\nRolling again...')
    return roll_1,roll_2