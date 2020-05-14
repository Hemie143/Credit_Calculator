from math import log, ceil
import argparse
import sys


def diff(P, n, interest):
    i = interest / 12 / 100
    over = P
    for m in range(n):
        d = ceil(P / n + i * (P - P * m / n))
        over -= d
        print(f'Month {m + 1}: paid out {d}')
    print(f'Overpayment = {-over}')


def annuity(payment, principal, periods, interest):
    if not payment:
        nominal_rate = interest / 100 / 12
        annuity = ceil(principal * (nominal_rate * pow(1 + nominal_rate, periods)) / (pow(1 + nominal_rate, periods) - 1))
        over = annuity * periods - principal
        print(f'Your annuity payment = {ceil(annuity)}!')
        print(f'Overpayment = {over}')
    elif not principal:
        nominal_rate = interest / 100 / 12
        principal = payment / (nominal_rate * pow(1 + nominal_rate, periods)) * (pow(1 + nominal_rate, periods) - 1)
        over = payment * periods - principal
        print(f'Your credit principal = {principal}!')
        print(f'Overpayment = {over}')
    elif not periods:
        nominal_rate = interest / 100 / 12
        periods = log(payment / (payment - nominal_rate * principal), 1 + nominal_rate)
        periods = ceil(periods)
        over = payment * periods - principal
        if periods > 11:
            months = periods % 12
            if months:
                print(f'You need {periods // 12} years and {periods % 12} months to repay this credit!')
            else:
                print(f'You need {periods // 12} years to repay this credit!')
        else:
            print(f'You need {periods} months to repay this credit!')
        print(f'Overpayment = {over}')
    elif not interest:
        incorrect()


def incorrect():
    print('Incorrect parameters')
    exit()

if __name__ == '__main__':
    if len(sys.argv) != 5:
        incorrect()
    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--payment', type=int, default=0)
    parser.add_argument('--principal', type=int, default=0)
    parser.add_argument('--periods', type=int, default=0)
    parser.add_argument('--interest', type=float, default=0)
    args = parser.parse_args()

    if args.type == 'annuity':
        annuity(args.payment, args.principal, args.periods, args.interest)
    elif args.type == 'diff':
        if args.payment:
            incorrect()
        diff(args.principal, args.periods, args.interest)
    else:
        incorrect()

