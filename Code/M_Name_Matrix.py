class NameMatrix:
    # Basic Information
    p_names = [[0]]
    name = "Name"

    # Loop to create a line of names.
    while len(name) > 0:
        name = str(input("Type a player name em press RETURN or simply press RETURN: "))
        if not len(name) == 0:
            p_names[0].append(name)
            p_names.append([name])

    # Loop to create Name Matrix.
    for x in range(1, len(p_names[0])):
        for y in range(1, len(p_names[0])):
            p_names[x].append(0)
