from Imports import funciones

Exit = False
flg_0 = True
flg_1 = False
flg_2 = False
flg_3 = False
flg_4 = False
flg_10 = False
flg_11 = False
flg_juego = False
# Strigs de los menús
head_menu = "\n" + " " * 45 + "1)Login\n" + " " * 45 + "2)Create User\n" + " " * 45 + "3)Replay Adventure\n" + \
            " " * 45 + "4)Reports\n" + " " * 45 + "5)Exit"
head_loged_menu = "\n" + " " * 45 + "1)Logout\n" + " " * 45 + "2)Play\n" + " " * 45 + "3)Replay Adventure\n" + \
                  " " * 45 + "4)Reports\n" + " " * 45 + "5)Exit"
head_report_menu = "\n" + " " * 45 + "1)Most used answer\n" + " " * 45 + "2)Player with more games played\n" + \
                   " " * 45 + "3)Games played by user\n" + " " * 45 + "4)Back"

menu_input = " " * 45 + "Option -> "
while True:
    if not flg_0 and Exit:
        break
    # Menú 0, es decir el general
    while flg_0:
        funciones.getMainHeader()
        opc = funciones.getOpt(head_menu, menu_input, [1, 2, 3, 4, 5])
        if opc == 1:
            flg_1 = True
            flg_0 = False

        elif opc == 2:
            flg_2 = True
            flg_0 = False

        elif opc == 3:
            flg_3 = True
            break

        elif opc == 4:
            flg_4 = True
            break

        elif opc == 5:
            print("\nThank you for using playing this game, hope you come back soon")
            flg_0 = False
            Exit = True

    while flg_1:
        print("Username:")
        username = input()
        print("Password:")
        password = input()
        if funciones.checkUserbdd(username, password) == 1:
            print("Hi {}, lets play!".format(username))
            flg_11 = True
            flg_1 = False
        else:
            if funciones.checkUserbdd(username, password) == 0:
                print("There's no username registered as '{}'".format(username))
                input("Press enter to continue")
                print()

            elif funciones.checkUserbdd(username, password) == -1:
                print("Incorrect Password")
                input("Press enter to continue")
                print()
        flg_0 = True
        flg_1 = False

    while flg_11:
        pos_menu = 0
        adventures = funciones.get_adventures_with_chars()
        adventures_keys = list(adventures.keys())
        while True:
            dic_show = {}
            for i in adventures_keys[pos_menu:pos_menu + 4]:
                dic_show[i] = adventures[i]
            stringAdventures = funciones.getFormatedAdventures(dic_show)
            opc = funciones.getOpt(stringAdventures, "What adventure do you want to play?(0 Go back)",
                                   adventures_keys, exceptions=[0, "+", "-"])
            if opc == "+":
                if pos_menu + 4 > len(adventures_keys) - 4:
                    if pos_menu + 4 == len(adventures_keys):
                        pos_menu = 0
                        print()
                    else:
                        pos_menu = len(adventures_keys) - 4
                        print()
                else:
                    pos_menu += 4
                    print()
            elif opc == "-":
                if pos_menu - 4 < 0:
                    if pos_menu == 0:
                        pos_menu = len(adventures_keys) - 4
                        print()
                    else:
                        pos_menu = 0
                        print()
                else:
                    pos_menu -= 4
                    print()
            else:
                # Elije Opcion del menú
                if opc == 0:
                    flg_10 = True
                    flg_11 = False
                    break
                else:
                    flg_juego = True
                    flg_11 = False
                    break
    while flg_10:
        funciones.getMainHeader()
        funciones.getMainHeader()
        opc = funciones.getOpt(head_loged_menu, menu_input, [1, 2, 3, 4, 5], {}, ["+", "-"])
        if opc == 1:
            flg_0 = True
            flg_10 = False
        elif opc == 2:
            flg_11 = True
            flg_10 = False
        elif opc == 3:
            flg_3 = True
            break
        elif opc == 4:
            flg_4 = True
            break
        elif opc == 5:
            print("\nThank you for using playing this game, hope you come back soon")
            flg_10 = False
            flg_0 = False
            Exit = True

    #Flag para iniciar un juego
    while flg_juego:
        print("\n\n")

        funciones.getHeader()


    # Flag para la creación de usuario
    while flg_2:
        while True:
            user = input("Username -> ")
            if funciones.checkUser(user):
                break

        while True:
            password = input("Password -> ")
            if funciones.checkPassword(password):
                break

        funciones.insertUser(user, password)
        print("USER CREATED")
        input("Press enter to continue")
        flg_0 = True
        flg_2 = False

    # Flag para Replays
    while flg_3:
        print("Falta por implementar")
        input()
        flg_3 = False

    # Flag para el menú de reports
    while flg_4:
        funciones.getReportHeader()
        opc = funciones.getOpt(head_report_menu, menu_input, [1, 2, 3, 4])
        if opc == 4:
            flg_4 = False
