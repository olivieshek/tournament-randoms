deposit = 1000
percent = 2
month = 0
a = 0
b = 0
while True:
    profit = deposit * percent // 100
    deposit += profit
    month += 1
    if profit >= 30:
        print(f'Profit is {profit}, month - {month}')
        a = 1
    if deposit > 1200:
        print(f'Deposit balance is {deposit}, month - {month}')
        b = 1
    if a and b:
        exit