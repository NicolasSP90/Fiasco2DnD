from random import randrange
from M_Name_Matrix import NameMatrix
from M_Groups_Sub import Group1, Group2, Group3, Group4, Group5, Group6, Group7, Group8


# Basic Information
groups = 8
p_int_count = 0
matrix_l = 1
matrix_c = 2
matrix_loop = 0
matrix_lcount = 1
matrix_ccount = 2

# Name Matrix
NameMatrix()
p_matrix = NameMatrix.p_names
players = len(p_matrix)-1

# Number of Interactions and Players Relations
groupint = int(input("Inform Group Interaction.\n1-Circle\n2-Universal\n"))
if groupint == 1:
    p_int = int(players)
elif groupint == 2:
    p_int = int(players * (players - 1) / 2)
else:
    p_int = 0
    print("Problem trying to identify the Group Interaction. Restart and Try Again.")
    exit()

# Random Numbers - Groups and Subgroups
while int(p_int_count) < p_int:
    intplayer = []
    rolltitle = int(randrange(1, groups+1))
    rollsub = int(randrange(1, groups+1))
    if rolltitle == int(1):
        Group1()
        intplayer.append(Group1.title)
        intplayer.append(Group1.subtitles[rollsub-1][0])
    elif rolltitle == int(2):
        Group2()
        intplayer.append(Group2.title)
        intplayer.append(Group2.subtitles[rollsub - 1][0])
    elif rolltitle == int(3):
        Group3()
        intplayer.append(Group3.title)
        intplayer.append(Group3.subtitles[rollsub - 1][0])
    elif rolltitle == int(4):
        Group4()
        intplayer.append(Group4.title)
        intplayer.append(Group4.subtitles[rollsub - 1][0])
    elif rolltitle == int(5):
        Group5()
        intplayer.append(Group5.title)
        intplayer.append(Group5.subtitles[rollsub - 1][0])
    elif rolltitle == int(6):
        Group6()
        intplayer.append(Group6.title)
        intplayer.append(Group6.subtitles[rollsub - 1][0])
    elif rolltitle == int(7):
        Group7()
        intplayer.append(Group7.title)
        intplayer.append(Group7.subtitles[rollsub - 1][0])
    elif rolltitle == int(8):
        Group8()
        intplayer.append(Group8.title)
        intplayer.append(Group8.subtitles[rollsub - 1][0])
    else:
        print("Problem trying to identify the Groups and Subgroups. Restart and Try Again.")
        exit()

    # Circular Name Matrix
    if groupint == 1:
        if matrix_ccount == players + 1:
            # noinspection PyTypeChecker
            p_matrix[1][players] = intplayer
            # noinspection PyTypeChecker
            p_matrix[players][1] = intplayer
        else:
            p_matrix[matrix_lcount][matrix_ccount] = intplayer
            p_matrix[matrix_ccount][matrix_lcount] = intplayer
        p_int_count += 1
        matrix_ccount += 1
        matrix_lcount += 1

    # Universal Name Matrix
    elif groupint == 2:
        p_matrix[matrix_lcount][matrix_ccount] = intplayer
        p_matrix[matrix_ccount][matrix_lcount] = intplayer
        p_int_count += 1
        matrix_ccount += 1
        if matrix_ccount == players + 1:
            matrix_loop += 1
            matrix_ccount = matrix_c + matrix_loop
            matrix_lcount = matrix_l + matrix_loop
    else:
        print("Problem to create the Name Matrix. Restart and Try Again.")
        exit()

for x in range(1, players+1):
    print("\nPlayer " + p_matrix[x][0] + " is related to the following Players:")
    for y in range(1, players+1):
        if p_matrix[x][y] != 0:
            print(p_matrix[0][y] + " (" + p_matrix[x][y][0] + ") " + p_matrix[x][y][1])
