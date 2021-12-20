from random import choice


def dwolf(damage=0, opt=0, x=10):
    if opt == 2:
        opt = 1

    hp = ''
    lhp = ''
    # VIDA DO LOBO E LUTA
    for i in range(0, x - damage):
        hp = hp + '█'
    if damage > 0:
        for v in range(0, damage):
            lhp = lhp + '█'

    print(f"HP: \033[34m{hp}\033[m\033[31m{lhp}\033[m")

    WR = 'Wind Roar'  # give 1 damage point
    FC = "Fear's Claw"  # give 2 damage point
    power = [WR, FC]
    used = choice(power)
    if used == WR:
        print(f'Wolf used {WR}')
        used = 1
    else:
        print(f'Wolf used {FC}')
        used = 2
    if opt == 2:
        used = opt - used

    return used
