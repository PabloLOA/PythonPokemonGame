import readchar
import os
import random
from random import randint

## Variables del Mapa
POS_X = 0
POS_Y = 1
pos_ini = [12, 12]
end_game = False
number_of_potions = 3

#Configuración de la vida propia inicial
Starter_Own_HP = 90
HP_2= Starter_Own_HP
input_options = ["0", "1", "2"]

#Variable que indica la longitud de la barra de salud
HP_bar_length = 20

# Lista de Pokemon. [0] Para el nombre, [1] para la vida.
Enemy_Pokemon_List = [["Pikachu", 75], ["Ratata", 55], ["Pidgey", 50], ["Drowzee", 90]]

# Lista de ataques. [0] Para el nombre, [1] para el daño del ataque.
Pikachu_Attack_List = [["Placaje", 5], ["Rayo", 20], ["Bola Voltio", 10], ["Onda Trueno",15]]
Ratata_Attack_List = [["Placaje", 5], ["Ataque Rápido", 10], ["Mordisco", 15], ["Triturar",25]]
Pidgey_Attack_List = [["Placaje", 5], ["Ataque Arena", 7], ["Ataque Ala", 10], ["Vendaval",20]]
Drowzee_Attack_List = [["Destructor", 5], ["Psicorrayo", 10], ["Psiquico", 12], ["Psicorrayo",17]]
#Lista de Ataques Propios
Squirtle_Attack_List = [["Placaje", 5], ["Pistola Agua", 25], ["Burbuja", 9]]

#Definición de las funciones
def RandomEnemy():
    random = randint(0,3)
    enemy = Enemy_Pokemon_List[random]
    return enemy
def CALC_Enemy_HP() :
    Enemy_HP = int((HP_1 / enemy_StarterHP) * HP_bar_length)
    return Enemy_HP
def CALC_Own_HP() :
    Own_HP = int((HP_2 / Starter_Own_HP) * HP_bar_length)
    return  Own_HP
def ShowEnemyHP():
    print("Vida {}   [{}{}] {}/{}".format(enemyPokemon,"#" * Enemy_HP, " " * (HP_bar_length - Enemy_HP), HP_1, enemy_StarterHP))
def ShowOwnHP():
    print("Vida Squirtle   [{}{}] {}/{}".format("#" * Own_HP, " " * (HP_bar_length - Own_HP), HP_2, Starter_Own_HP))
def Enemy_attack(attack_1,HP_2):
    print(enemyPokemon + " usó " + attack_List[attack_1][0])
    HP_2 = HP_2 - attack_List[attack_1][1]
    return HP_2
def checkHP(HP_1, HP_2):
    if HP_1 < 0:
        HP_1 = 0
    if HP_2 < 0:
        HP_2 = 0
    return HP_1, HP_2
def Own_attack(HP_1):
    print("turno Squirtle")
    attack_2 = None
    while attack_2 not in input_options:
        attack_2 = input("Qué ataque quieres? Placaje [0], Pistola Agua [1], Burbuja [2] ")
    attack_2 = int(attack_2)
    print("Squirtle usó " + Squirtle_Attack_List[attack_2][0])
    HP_1 = HP_1 - Squirtle_Attack_List[attack_2][1]
    input()
    return HP_1
def print_HP(Enemy_HP, HP_bar_length, HP_1, enemy_StarterHP, Own_HP, Starter_Own_HP):
    print("Vida {}   [{}{}] {}/{}".format(enemyPokemon, "#" * Enemy_HP, " " * (HP_bar_length - Enemy_HP), HP_1, enemy_StarterHP))
    print("Vida Squirtle   [{}{}] {}/{}".format("#" * Own_HP, " " * (HP_bar_length - Own_HP), HP_2, Starter_Own_HP))
    input("enter para continuar... \n\n")
    os.system('cls' if os.name == 'nt' else 'clear')
def winner(HP_1, HP_2):
    if HP_1 > HP_2:
        print("{} gana.".format(enemyPokemon))
    else:
        print("Squirtle gana.")

obstacle_definition = """\
#########################################
#                ########################
                 ######        ##########
##########       #####   ################
###              ####      ####     #####
##     ###   ########                ####
#      ###          #    #             ##
####   ##########   #    ################
####                     ###       ######
###################  ########       #####
###################  #######     ##     #
##########            #####      ##     #
###          #######   ####     ###     #
###      ##########    ###     #        #
##        #########                 #####
###         ###############      ########
####                             ########
#######                          ########
#########################################\
"""

obstacle_definition =[list(row) for row in obstacle_definition.split("\n")]
canvas_width = len(obstacle_definition[0])
canvas_height = len(obstacle_definition)

object_num = 4
map_objects = []

def create_obj():
    while object_num > len(map_objects):
        obj=[random.randint(0, canvas_width - 1), random.randint(0, canvas_height - 1)]
        if obj not in map_objects and obj != pos_ini and obstacle_definition[obj[POS_Y]][obj[POS_X]] != "#":
            map_objects.append(obj)

def initialize_maze():
    create_obj()
    print("+" + "-" * (3 * canvas_width) + "+")
    for coord_y in range(canvas_height):
        print("|", end="")
        for coord_x in range(canvas_width):
            char_to_draw =" "
            for map_object in map_objects:
                if coord_y == map_object[POS_Y] and coord_x == map_object[POS_X]:
                    char_to_draw ="$"
            if coord_y == pos_ini[POS_Y] and coord_x == pos_ini[POS_X]:
                char_to_draw ="@"
            if obstacle_definition[coord_y][coord_x] == "#":
                char_to_draw = "#"
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (3 * canvas_width) + "+")
    print("Salud de Squirtle: " + str(HP_2))
    print("Pociones Restantes: " + str(number_of_potions)+ "\n")

create_obj()
initialize_maze()
while not end_game:

    print("¿Dónde te quieres mover? [WASD] ([Q] para salir, [P] Para usar una Max Pocion)")
    direction = readchar.readchar()
    direction = direction.upper()
    new_position = None

    if direction == "W":
        new_position = [pos_ini[POS_X], (pos_ini[POS_Y] - 1) %canvas_height]

    elif direction == "S":
        new_position = [pos_ini[POS_X], (pos_ini[POS_Y] + 1) % canvas_height]

    elif direction == "D":
        new_position = [(pos_ini[POS_X] + 1) % canvas_width, pos_ini[POS_Y]]

    elif direction == "A":
        new_position = [(pos_ini[POS_X] - 1) % canvas_width, pos_ini[POS_Y]]

    elif direction == "P":
        if number_of_potions >0:
            print("Max Pocion!")
            HP_2 = Starter_Own_HP
            number_of_potions -=1

    elif direction == "Q":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("ADIOS!")
        break
    if new_position :
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            pos_ini = new_position

    os.system('cls' if os.name == 'nt' else 'clear')
    print("+" + "-" * (3 * canvas_width) + "+")
    for coord_y in range(canvas_height):
        print("|", end="")
        for coord_x in range(canvas_width):
            char_to_draw =" "
            object_in_cell = None

            for map_object in map_objects:
                if coord_y == map_object[POS_Y] and coord_x == map_object[POS_X]:
                    char_to_draw ="$"
                    object_in_cell = map_object

            if coord_y == pos_ini[POS_Y] and coord_x == pos_ini[POS_X]:
                char_to_draw = "@"

                if object_in_cell:

                    enemy = RandomEnemy()
                    enemyPokemon = enemy[0]
                    enemy_StarterHP = enemy[1]
                    HP_1 = enemy_StarterHP

                    # Configuración del set de movimientos enemigo
                    if enemyPokemon == "Pikachu":
                        attack_List = Pikachu_Attack_List
                    elif enemyPokemon == "Ratata":
                        attack_List = Ratata_Attack_List
                    elif enemyPokemon == "Pidgey":
                        attack_List = Pidgey_Attack_List
                    elif enemyPokemon == "Drowzee":
                        attack_List = Drowzee_Attack_List

                    print("\n\n El combate contra {} está a punto de comenzar! \n".format(enemyPokemon))

                    # Combate Pokemon. Sería interesante hacer una función de esto
                    while HP_1 > 0 and HP_2 > 0:
                        print("Turno Enemigo \n")
                        attack_1 = randint(0, 3)
                        HP_2 = Enemy_attack(attack_1, HP_2)

                        Enemy_HP = CALC_Enemy_HP()
                        Own_HP = CALC_Own_HP()

                        HP_1 = checkHP(HP_1, HP_2)[0]
                        HP_2 = checkHP(HP_1, HP_2)[1]

                        ShowEnemyHP()
                        ShowOwnHP()

                        input("ENTER para continuar... \n\n")
                        os.system('clear')

                        if HP_2 <= 0:
                            print(" {} ha ganado! ".format(enemyPokemon))
                            exit()

                        HP_1 = Own_attack(HP_1)
                        os.system('clear')
                        Enemy_HP = CALC_Enemy_HP()
                        Own_HP = CALC_Own_HP()

                        HP_1 = checkHP(HP_1, HP_2)[0]
                        HP_2 = checkHP(HP_1, HP_2)[1]

                        print_HP(Enemy_HP, HP_bar_length, HP_1, enemy_StarterHP, Own_HP, Starter_Own_HP)

                    winner(HP_1, HP_2)
                    map_objects.remove(object_in_cell)
                    if len(map_objects) == 0:
                        end_game = True


            if obstacle_definition[coord_y][coord_x] == "#":
                char_to_draw = "#"
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (3 * canvas_width) + "+")
    print("Salud de Squirtle: " + str(HP_2))
    print("Pociones Restantes: " + str(number_of_potions) + "\n")
    print(len(map_objects))

    if end_game:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("HAS GANADO!")