import random
import sys
import time

cooficents = [0.1,0.1,0.2,0.2,0.1,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.1,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.5,0.5,0.5,0.5,0.5,0.7,0.7,0.7,0.7,0.7,2,2,2,3,3,4,4,5,5,10]

balance = float(input('\033[41mсколько депнешь: \033[0m'))

while True:
    print('\033[1mваш баланс:\033[0m', round(balance))
    time.sleep(1)
    stavka = float(input('\033[1mваша ставка:\033[0m '))
    if stavka > balance:
        print('\033[41mнедостаточно средств\033[0m')
        time.sleep(1)
    elif balance < stavka:
        print('\033[41mне может быть отрицательным\033[0m')
        time.sleep(1)
    else:
        skoka = balance - stavka
        coof = random.choice(cooficents)
        if coof < 1:
            print('\033[41mнеудача!\033[0m')
        elif 10 > coof > 1:
            print('\033[42mУдача\033[0m')
        if coof == 10:
            print('\033[42m\033[1mДЖЕКПОТ!\033[0m')
        time.sleep(1)
        proitog = stavka * coof
        balance = (balance - stavka) + proitog
        if balance < 1:
            print('\033[41mты всё проебал\033[0m')
            sys.exit()