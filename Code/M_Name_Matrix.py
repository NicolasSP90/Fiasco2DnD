class NameMatrix:
    # informações iniciais
    p_names = [[0]]
    name = "Name"

    # loop para criação da primeira linha da matriz com nomes.
    while len(name) > 0:
        name = str(input("Insira o nome do Player/Personagem ou pressione ENTER: "))
        if not len(name) == 0:
            p_names[0].append(name)
            p_names.append([name])

    # loop para transformar a lista em matriz.
    for x in range(1, len(p_names[0])):
        for y in range(1, len(p_names[0])):
            p_names[x].append(0)