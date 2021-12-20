from time import sleep


def options():
    opt = int(input(f'\t[1] ataque ( 1 DE DANO)\n'
                    f'\t[2] defesa (2 DE DEF)\n'
                    f'\t[3] item ( USE A ITEM)\n'
                    f'\t[4] RUN (Escape from the fight)\n \t: '))
    return opt


def hud(damage, x=10, y=10):
    hp = ''
    mp = ''
    lhp = ''
    for i in range(0, x - damage):
        hp = hp + '█'
    if damage > 0:
        for i in range(0, damage):
            lhp = lhp + '█'
            lp = len(lhp)
    for i in range(0, y):
        mp = mp + '█'
    print(f'HP: \033[32m{hp}\033[31m{lhp} \n\033[mMP: \033[36m{mp}\033[m')
    if damage == 10:
        return lp

def bloco(msg):
    tam = len(msg)
    print(f"\t\033[31m{'-' * (tam + 4)}")
    print(f"\t\033[4;31m{msg.center(tam+4)}\033[m")
    print(f"\t\033[31m{'-' * (tam + 4)}\033[m")


def linha():  # Line
    print('-=' * 30)


def cabecalho():  # Cabeçaalho
    print('-=' * 30)
    print('WELCOME PLAYER'.center(60))
    print('-=' * 30)


def criapersonagem():  # Creating a character
    print(f'Classes disponiveis')
    print('1 - Warrior')
    print('2 - Archer')
    print('3 - Wizzard')
    print('4 - Feral')
    classe = input('Qual classe você deseja escolher ?: \n')
    if classe == '1':
        classe = 'Warrior'
    elif classe == '2':
        classe = 'Archer'
    elif classe == '3':
        classe = 'Wizzard'
    elif classe == '4':
        classe = 'Feral'
    else:
        print('Class invalid')
    return classe


def path():  # Define trilha a seguir
    while True:
        print(f'TRILHAS DISPONIVEIS ')
        print('1 - Noble')
        print('2 - Mercenary')
        print('3 - Farmer')
        print('4 -  Descrição das trilhas')
        esc = input('')
        if esc == '1':
            tril = 'Noble'
            break
        elif esc == '2':
            tril = 'Mercenary'
            break
        elif esc == '3':
            tril = 'Farmar'
            break
        elif esc == '4':
            linha()
            print('\tNobre - Começara no castelo como o filho do Rei Lothric\n'
                  '\te da Rainha Gwnyver, Tera boa montaria, tropas e dinheiro\n'
                  '\tconfortavel para as suas espedições e trades\n'
                  '\t(habilidade espadas e arcos)\n')
            linha()
            print('\tMercenario - Começa com o seu bando de Mercenarios\n'
                  '\t você terá um grande conhecimento do mapa e será \nfurtivo'
                  '\tterá companheiros para ajudar em algumas lutas\n.'
                  '\t(habilidade furtiva)\n')
            linha()
            print('\tCamponês - Começara com grande afeto com os animais, será\n '
                  '\tdesbravador e com vontade de crescimento seu igual!\n'
                  '\t(Habilidade little rookie)\n')
    return tril


def introduction():
    introduc = f'No começo havia a chama primordial. Ela era a fonte de todas a vida.' \
                 f'a partir dela\n surgiu os Deuses, as criaturas Mágicas e os Humanos. ' \
                 f'Eras atrás os mundos eram separados,\n entretanto agora após o mal ser' \
                 f' libertado pelo feiticeiro Ocellot, os mundos foram\n unificados como um só ' \
                 f'(O dos monstros e das criaturas magicas). \n\tUm guerreiro precisa ajudar o mundo ' \
                 f'a ser como antes e salvar tudo ...'
    print(introduc)

def beginning(x, name):
    if x == 'Noble':
        # Dialogos do começo do caminho nobre
        print(f'\t\tvocê abre os olhos, foi acordado no')
        print(f'\t\tmeio da noite com o barulho de muitas pessoas correndo')
        print(f'\t\tvocê fica curioso e pensa...')
        print(f"\t{name}:'O que será que está acontecendo?'")
        print(f" \tvocê vai para sala para saber do que  ")
        print(f' \ttrata-se este tumulto.')
        print(f'\t{name}: PAI! por que toda essa balburdia, o que está acontecendo?')
        print(f'\t♚Rei Lothric: "Meu filho sente-se... preciso lhe falar sobre Ocellot.')
        print(f'\tO feiticeiro maligino conseguiu o que queria, e agora os 2 mundos ')
        print(f'\tforam unificados. Olhe pela janela e você entenderá"')
        print(f'\t\tVocê olha pela janela e vê criaturas magicas em todos')
        print(f'\t\tos lugares lutando com os habitantes do reino ')
        print(f'\t\te com espanto diz.')
        print(f'\t{name} MAS O QUE! pelos deuses! ')
        print(f'\tPai os monstros estão matando nossos aldeões!')
        print(f'♚Rei Lothric: por favor meu filho {name} salve nosso povo.',)
        print('\t\tVocê corre para aldeia e encontra um Lobo negro atacando uma criança')

        bloco('Decisão')
        dec = int(input('\t[1] Lutar \n'
                        '\t[2] Correr \n'
                        '\tDecisão: '))
        return dec
