import random

def generatePayoff():
    payoff = 1
    coin = random.randint(0,1)
    while coin == 1:
        payoff *= 2
        coin = random.randint(0,1)
    return payoff

def playNTimes(n):
    i = 0
    total = 0
    max_val = 0
    while i < n:
        b = generatePayoff()
        if b > max_val:
            max_val = b
        total += b
        i += 1
    print('Maximum payoff {}'.format(max_val))
    return total / n

a = input('How many times would you like to play?:\n')
result = playNTimes(int(a))
print('The expected payoff is {}'.format(result))