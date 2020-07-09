data = '         '
print('---------')
print('| ' + data[0] + ' ' + data[1] + ' ' + data[2] + ' |')
print('| ' + data[3] + ' ' + data[4] + ' ' + data[5] + ' |')
print('| ' + data[6] + ' ' + data[7] + ' ' + data[8] + ' |')
print('---------')


while True:
    # loop to enter as X
    t = 0
    while t == 0:  # Run till valid coordintes are not entered
        i = 3  # y cord starts from 3
        m = 0
        x, y = input('Enter the coordinates: ').split()
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if x not in range(1, 4) or y not in range(1, 4):
                print('Coordinates should be from 1 to 3!')
            else:
                while 1 <= i <= 3:  # loop working a/c to cartesian-coord., i=y and j=x
                    j = 1  # x cord starts from 1
                    while 1 <= j <= 3:
                        if i == y and j == x:  # at x,y cord.
                            s = [z for z in data]  # form a list of data elements bcoz string can't be assigned
                            if s[m] == 'X' or s[m] == 'O':  # m is the index of list, data[m] and s[m] are same
                                print("This cell is occupied! Choose another one!")
                            else:
                                s[m] = 'X'  # assignment to list
                                data = ''.join(s)
                                print('---------')
                                print('| ' + data[0] + ' ' + data[1] + ' ' + data[2] + ' |')
                                print('| ' + data[3] + ' ' + data[4] + ' ' + data[5] + ' |')
                                print('| ' + data[6] + ' ' + data[7] + ' ' + data[8] + ' |')
                                print('---------')
                                t = 1  # terminate main loop
                        j += 1  # increase x cord by 1
                        m += 1
                    i -= 1  # decrease y coord by 1 after every j/x loop

        else:
            print('You should enter numbers!')

    # check status of game
    no_of_o = 0
    no_of_x = 0
    no_of_blanks = 0
    x_win = 0
    o_win = 0
    for i in data:
        if i == 'O':  # count no of O
            no_of_o += 1
        elif i == 'X':  # count no of X
            no_of_x += 1
        elif i == ' ':  # count no of blanks
            no_of_blanks += 1

    if (data[0] == 'X' and data[1] == 'X' and data[2] == 'X') or (
            data[3] == 'X' and data[4] == 'X' and data[5] == 'X') or (
            data[6] == 'X' and data[7] == 'X' and data[8] == 'X') or (
            data[0] == 'X' and data[3] == 'X' and data[6] == 'X') or (
            data[1] == 'X' and data[4] == 'X' and data[7] == 'X') or (
            data[2] == 'X' and data[5] == 'X' and data[8] == 'X') or (
            data[0] == 'X' and data[4] == 'X' and data[8] == 'X') or (
            data[2] == 'X' and data[4] == 'X' and data[6] == 'X'):
        x_win = 1  # if 3 X's in a line

    if (data[0] == 'O' and data[1] == 'O' and data[2] == 'O') or (
            data[3] == 'O' and data[4] == 'O' and data[5] == 'O') or (
            data[6] == 'O' and data[7] == 'O' and data[8] == 'O') or (
            data[0] == 'O' and data[3] == 'O' and data[6] == 'O') or (
            data[1] == 'O' and data[4] == 'O' and data[7] == 'O') or (
            data[2] == 'O' and data[5] == 'O' and data[8] == 'O') or (
            data[0] == 'O' and data[4] == 'O' and data[8] == 'O') or (
            data[2] == 'O' and data[4] == 'O' and data[6] == 'O'):
        o_win = 1  # if 3 O's in a line

    if (x_win == 1 and o_win == 1) or (abs(no_of_x - no_of_o) >= 2):
        print('Impossible')
        break
    elif x_win == 1:
        print('X wins')
        break
    elif o_win == 1:
        print('O wins')
        break
    elif no_of_blanks > 0:
        pass
    else:
        print('Draw')
        break

    # loop to enter as O
    t = 0
    while t == 0:  # Run till valid coordintes are not entered
        i = 3  # y cord starts from 3
        m = 0
        x, y = input('Enter the coordinates: ').split()
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if x not in range(1, 4) or y not in range(1, 4):
                print('Coordinates should be from 1 to 3!')
            else:
                while 1 <= i <= 3:  # loop working a/c to cartesian-coord., i=y and j=x
                    j = 1  # x cord starts from 1
                    while 1 <= j <= 3:
                        if i == y and j == x:  # at x,y cord.
                            s = [z for z in data]  # form a list of data elements bcoz string can't be assigned
                            if s[m] == 'X' or s[m] == 'O':  # m is the index of list, data[m] and s[m] are same
                                print("This cell is occupied! Choose another one!")
                            else:
                                s[m] = 'O'  # assignment to list
                                data = ''.join(s)
                                print('---------')
                                print('| ' + data[0] + ' ' + data[1] + ' ' + data[2] + ' |')
                                print('| ' + data[3] + ' ' + data[4] + ' ' + data[5] + ' |')
                                print('| ' + data[6] + ' ' + data[7] + ' ' + data[8] + ' |')
                                print('---------')
                                t = 1  # terminate main loop
                        j += 1  # increase x cord by 1
                        m += 1
                    i -= 1  # decrease y coord by 1 after every j(x) loop

        else:
            print('You should enter numbers!')

    # check status of game
    no_of_o = 0
    no_of_x = 0
    no_of_blanks = 0
    x_win = 0
    o_win = 0
    for i in data:
        if i == 'O':  # count no of O
            no_of_o += 1
        elif i == 'X':  # count no of X
            no_of_x += 1
        elif i == ' ':  # count no of blanks
            no_of_blanks += 1

    if (data[0] == 'X' and data[1] == 'X' and data[2] == 'X') or (
            data[3] == 'X' and data[4] == 'X' and data[5] == 'X') or (
            data[6] == 'X' and data[7] == 'X' and data[8] == 'X') or (
            data[0] == 'X' and data[3] == 'X' and data[6] == 'X') or (
            data[1] == 'X' and data[4] == 'X' and data[7] == 'X') or (
            data[2] == 'X' and data[5] == 'X' and data[8] == 'X') or (
            data[0] == 'X' and data[4] == 'X' and data[8] == 'X') or (
            data[2] == 'X' and data[4] == 'X' and data[6] == 'X'):
        x_win = 1  # if 3 X's in a line

    if (data[0] == 'O' and data[1] == 'O' and data[2] == 'O') or (
            data[3] == 'O' and data[4] == 'O' and data[5] == 'O') or (
            data[6] == 'O' and data[7] == 'O' and data[8] == 'O') or (
            data[0] == 'O' and data[3] == 'O' and data[6] == 'O') or (
            data[1] == 'O' and data[4] == 'O' and data[7] == 'O') or (
            data[2] == 'O' and data[5] == 'O' and data[8] == 'O') or (
            data[0] == 'O' and data[4] == 'O' and data[8] == 'O') or (
            data[2] == 'O' and data[4] == 'O' and data[6] == 'O'):
        o_win = 1  # if 3 O's in a line

    if (x_win == 1 and o_win == 1) or (abs(no_of_x - no_of_o) >= 2):
        print('Impossible')
        break
    elif x_win == 1:
        print('X wins')
        break
    elif o_win == 1:
        print('O wins')
        break
    elif no_of_blanks > 0:
        pass
    else:
        print('Draw')
        break

