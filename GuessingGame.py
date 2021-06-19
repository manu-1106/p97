import random
print('Number guessing game')
number=random.randint(1,9)
chances=0
print('guess a number(between 1 and 9):')
while chances<5:
    guess=int(input('enter your number'))
    if guess==number:
        print('CONGRATULATIONS YOU WIN!')
        break
    elif guess<number:
        print('your guess was too low guess a number higher than',guess)
    else :
        print('your guess was too high try a number lower than',guess)
    chances+=1
if not chances<5:
    print('YOU LOSE!the number is ',number)
     