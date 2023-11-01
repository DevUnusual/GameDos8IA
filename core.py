import numpy as np

#d - down r - right u - up l - left
movs = {(0,0):["R", "D"], (0,1):["R", "D", "L"], (0,2):["D", "L"], (1,0):["R", "D", "U"], (1,1):["R", "D", "U", "L"], (1,2):["D", "U", "L"], (2,0):["R", "U"], (2,1):["R", "U", "L"], (2,2):["U", "L"]}

# Matriz de estado inicial
stateInicial = np.array(((1, 2, 3), (4, 5, 6), (7, -1, 8)))

# Matriz de estado final
FINAL = np.array(((1, 2, 3), (4, 5, 6), (7, 8, -1)))

def distance_to_position(position, number):
    """Calcula a distância de um número até a posição final"""
    # Posição final do número
    final_position = np.where(FINAL == number)
    # Distância entre a posição atual e a posição final
    return abs(position[0] - final_position[0]) + abs(position[1] - final_position[1])

def distance_to_final(state):
    """Calcula a distância de um estado até o estado final"""
    # Distância total
    distance = 0
    # Percorre o estado
    for i in range(3):
        for j in range(3):
            # Se o número for diferente de -1
            if state[i][j] != -1:
                # Calcula a distância do número até a posição final
                distance += distance_to_position((i, j), state[i][j])
    # Retorna a distância
    return distance

def blank_space(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == -1:
                return (i, j)
            
def possible_moviments(pos):
    return movs[pos]

def action_move(state, direction, blank):
    if direction == "R":
        state[blank[0]][blank[1]] = state[blank[0]][blank[1]+1]
        state[blank[0]][blank[1]+1] = -1
    elif direction == "L":
        state[blank[0]][blank[1]] = state[blank[0]][blank[1]-1]
        state[blank[0]][blank[1]-1] = -1
    elif direction == "U":
        state[blank[0]][blank[1]] = state[blank[0]-1][blank[1]]
        state[blank[0]-1][blank[1]] = -1
    elif direction == "D":
        state[blank[0]][blank[1]] = state[blank[0]+1][blank[1]]
        state[blank[0]+1][blank[1]] = -1
    return state
        
def explore_possibilitys(state : np.array):
    blank = blank_space(state)
    possible = possible_moviments(blank)
    ways = []
    for i in possible:
        result = action_move(state.copy(), i, blank)
        if np.array_equal(result, FINAL):
            print(result)
            print("FIM")
            return state
        value = distance_to_final(result)
        print(result)
        print(value)
        ways.append((value, result))
    return ways
    ##salvar os estados e refazer as possibilidades em cada um ate chegar na resposta.

print(distance_to_position((1, 1), 1))
print(distance_to_final(stateInicial))
print(blank_space(stateInicial))
print(possible_moviments(blank_space(stateInicial)))
print(stateInicial)
horizonte = explore_possibilitys(stateInicial)
print(horizonte)


def game():
    state = stateInicial
    while True:
        print(state)
        blank = blank_space(state)
        possible = possible_moviments(blank)
        print(possible)
        mov = input("Digite o movimento: ")
        if mov not in possible:
            print("Movimento inválido")
        else:
            state = action_move(state, mov, blank)
        if np.array_equal(state, FINAL):
            print("FIM")
            break
#game()