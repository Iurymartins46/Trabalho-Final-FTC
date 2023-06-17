def generate_transition_matrix(filename):
    # Abrir o arquivo para leitura
    with open(filename, 'r') as file:
        # Ler o conteúdo do arquivo
        content = file.read()

    # Separar as linhas do conteúdo
    lines = content.split('\n')

    # Extrair os estados do conteúdo
    states = set()
    for line in lines:
        if line:
            transition = line.split('->')
            if len(transition) != 2:
                continue  # Ignorar linhas no formato incorreto
            from_state = transition[0].strip()
            to_state = transition[1].split('|')[0].strip()
            states.add(from_state)
            states.add(to_state)

    # Ordenar os estados em ordem alfabética
    states = sorted(states)

    # Mapear os estados para números inteiros
    state_map = {state: i for i, state in enumerate(states)}

    # Inicializar a matriz de transição com -1
    matrix_size = len(states)
    transition_matrix = [[-1] * matrix_size for _ in range(matrix_size)]

    # Preencher a matriz com as transições
    for line in lines:
        if line:
            transition = line.split('->')
            if len(transition) != 2:
                continue  # Ignorar linhas no formato incorreto
            from_state = transition[0].strip()
            to_state = transition[1].split('|')[0].strip()
            value = int(transition[1].split('|')[1].strip())
            from_state_index = state_map[from_state]
            to_state_index = state_map[to_state]
            transition_matrix[from_state_index][to_state_index] = value

    # Copiar a última linha da matriz para a primeira posição da nova matriz
    last_row = transition_matrix.pop()
    transition_matrix.insert(0, last_row)

    return transition_matrix

# Exemplo de uso
transition_matrix = generate_transition_matrix('PLAYER01.txt')

# Imprimir a matriz de transição
for row in transition_matrix:
    print(row)
    
#A matriz de transições representa as possíveis transições entre os estados do sistema,-1 caso não exista a transição de um estado para o outro.
