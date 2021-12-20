from Historia.util import tools, enemies


# variaveis
Character = dict()
weapon = list()
inventory = list()
vida_atual = 0
# cabeçalho
tools.cabecalho()

# cria personagem

while True:
    name = input('Type a nick name: ')
    if name.isalpha():
        break
    else:
        print('Error! invalid name')
Character['Name'] = name
while True:
    sex = str(input('Sex [M/F] ')).strip().upper()
    if sex in 'MF':
        break
    else:
        print('Error! please enter a valid sex')
Character['Sex'] = sex
# choice a class

tools.linha()
classe = tools.criapersonagem()
Character['Classe'] = classe
# choice a start path

tools.linha()
trilha = tools.path()
Character['Trilha'] = trilha

# introduction
tools.linha()
tools.introduction()

# beginning

tools.linha()
dec = tools.beginning(trilha, name)

#  battle
tools.bloco('--- BATTLE! ---')
damage = 0
enemy_life = 10
hp = 10
edamage = 0
while True:
    if hp == 0 or enemy_life == 0:
        break
    tools.linha()
    lp = tools.hud(edamage)
    tools.linha()
    opt = tools.options()
    tools.linha()
    if opt == 1:  # Attack give 1 damage
        damage = damage + 1
        edamage = edamage + enemies.dwolf(damage)
    if opt == 2:  # Defense block 1 damage
        block = enemies.dwolf(damage, opt=2)
        print(block)
        print(hp)
