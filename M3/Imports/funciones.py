from datetime import datetime
import pymysql

#conn = pymysql.connect(host="52.157.66.187", user="aleix", password="1Q2w3e4r5t6y", db="CHOOSE_YOUR_ADVENTURE")
conn = pymysql.connect(host="127.0.0.1", user="brahian", password="Pelochocolo1", db="CHOOSE_YOUR_ADVENTURE")
cur = conn.cursor()


def getMainHeader():
    print("*" * 100)
    print("                 ######## ##       ####  ######   ########    ######## ##     ##    "
          "\n                 ##       ##        ##  ##    ##  ##             ##    ##     ##    "
          "\n                 ##       ##        ##  ##        ##             ##    ##     ##    "
          "\n                 ######   ##        ##  ##   #### ######         ##    ##     ##    "
          "\n                 ##       ##        ##  ##    ##  ##             ##    ##     ##    "
          "\n                 ##       ##        ##  ##    ##  ##             ##    ##     ##    "
          "\n                 ######## ######## ####  ######   ########       ##     #######     ")
    print("\n                    ########  ########   #######  ########  ####    ###       "
          "\n                    ##     ## ##     ## ##     ## ##     ##  ##    ## ##      "
          "\n                    ##     ## ##     ## ##     ## ##     ##  ##   ##   ##     "
          "\n                    ########  ########  ##     ## ########   ##  ##     ##    "
          "\n                    ##        ##   ##   ##     ## ##         ##  #########    "
          "\n                    ##        ##    ##  ##     ## ##         ##  ##     ##    "
          "\n                    ##        ##     ##  #######  ##        #### ##     ##    ")
    print("\n              ###    ##     ## ######## ##    ## ######## ##     ## ########     ###       "
          "\n             ## ##   ##     ## ##       ###   ##    ##    ##     ## ##     ##   ## ##      "
          "\n            ##   ##  ##     ## ##       ####  ##    ##    ##     ## ##     ##  ##   ##     "
          "\n           ##     ## ##     ## ######   ## ## ##    ##    ##     ## ########  ##     ##    "
          "\n           #########  ##   ##  ##       ##  ####    ##    ##     ## ##   ##   #########    "
          "\n           ##     ##   ## ##   ##       ##   ###    ##    ##     ## ##    ##  ##     ##    "
          "\n           ##     ##    ###    ######## ##    ##    ##     #######  ##     ## ##     ##    ")
    print("*" * 100)


def getReportHeader():
    print("*" * 100)
    print("                ########  ######## ########   #######  ########  ########  ######  "
          "\n                ##     ## ##       ##     ## ##     ## ##     ##    ##    ##    ## "
          "\n                ##     ## ##       ##     ## ##     ## ##     ##    ##    ##       "
          "\n                ########  ######   ########  ##     ## ########     ##     ######  "
          "\n                ##   ##   ##       ##        ##     ## ##   ##      ##          ## "
          "\n                ##    ##  ##       ##        ##     ## ##    ##     ##    ##    ## "
          "\n                ##     ## ######## ##         #######  ##     ##    ##     ######  ")
    print("*" * 100)


def getHeader(header):
    if len(header) % 2 != 0:
        tam = 50 - (len(header) // 2)
        print("*" * 100 + "\n" + "=" * tam + header + "=" * (tam - 1) + "\n" + "*" * 100)
    else:
        tam = 50 - (len(header) // 2)
        print("*" * 100 + "\n" + "=" * tam + header + "=" * tam + "\n" + "*" * 100)


def formatText(phrase, lenline, split):
    lista = phrase.split()
    sizes = lenline
    stringres = ""
    for words in lista:
        if sizes - len(words) > 0:
            stringres = stringres + words + " "
            sizes = sizes - len(words) - 1
        else:
            while sizes != 0:
                stringres = stringres + " "
                sizes = sizes - 1
            stringres = stringres + split + words + " "
            sizes = int(lenline) - len(words) - 1
    if sizes != 0:
        stringres = stringres + " " * sizes

    return stringres


def getFormatedBodyColumns(tupla_texts, tupla_sizes, margin=1):
    textResultado = ""
    textlist = []
    for i in range(len(tupla_texts)):
        a = formatText(tupla_texts[i], tupla_sizes[i], "º").split("º")
        textlist.append(a)

    num_lines = 0
    for i in range(len(textlist)):
        if len(textlist[i]) > num_lines:
            num_lines = len(textlist[i])

    for i in range(num_lines):
        textResultado += "\n"
        for j in range(len(tupla_texts)):
            try:
                textResultado += textlist[j][i] + " " * margin
            except:
                textResultado += " " * tupla_sizes[j] + " " * margin

    return textResultado


def getFormatedAdventures(adventures):
    id_adventures_list = list(adventures.keys())
    stringRes = "=" * 44 + " Adventures " + "=" * 44 + "\n\n" + "Id Adventure" + " " * 3 + "Adventure" + \
                " " * 28 + "Description" + "\n" + "*" * 100
    for i in id_adventures_list:
        stringRes += getFormatedBodyColumns((str(i), adventures[i]["Name"], adventures[i]["Description"]), (13, 35, 45),
                                            2) + "\n"

    return stringRes


def getFormatedAnswers(idAnswer, text, lenLine, leftMargin):
    print(" " * leftMargin + "{})".format(idAnswer), end="")
    print(formatText(text, lenLine, "\n" + " " * (leftMargin + 2)))


def getHeadeForTableFromTuples(t_name_columns, t_size_columns, title=""):
    sum = 0
    for i in range(len(t_name_columns)):
        sum += len(t_name_columns[i])
        sum += t_size_columns[i]

    if len(title) != 0:
        tam = (sum // 2) - (len(title) // 2)
        if len(title) % 2 != 0:
            stringRes = "=" * tam + title + "=" * (tam - 1) + "\n"
        else:
            stringRes = "=" * tam + title + "=" * tam + "\n"
    else:
        stringRes = "=" * 100 + "\n"

    for i in range(len(t_name_columns)):
        stringRes = stringRes + t_name_columns[i] + " " * t_size_columns[i]

    return stringRes


def getTableFromDict(tuple_of_keys, weigth_of_columns, dict_of_data):
    list_of_data_keys = list(dict_of_data.keys())
    stringRes = ""
    for id in list_of_data_keys:
        stringRes += str(id)
        for data_pos in range(len(tuple_of_keys)):
            stringRes += " " * weigth_of_columns[data_pos] + str(dict_of_data[id][tuple_of_keys[data_pos]])
        stringRes += "\n"

    return stringRes


def getOpt(textOpts="", inputOptText="", rangeList=[], dictionary={}, exceptions=[]):
    # Lista donde se ponen la cantidad de opciones + 1 (el primer elemento de la lista està vacío por el espacio)
    list_text = textOpts.split("\n")
    list_keys = list(dictionary.keys())
    # Bucle que comprueba que sea una opción válida y imprime el menú otra vez en caso de que escriba un "+" o un "-"
    while True:
        print(textOpts + "\n")
        opc = input(inputOptText)
        if opc.isdigit():
            if (opc in str(rangeList)) or (opc in str(exceptions)) or (opc in str(list_keys)):
                return int(opc)
            else:
                print("=" * 15 + "'{}' is not a valid option".format(opc) + "=" * 15)
                input("Press enter to continue")
        # En este else està el caso que introduzca un "+" o un "-" para imprimir más o menos menú
        else:
            if (opc in str(exceptions)) or (opc in str(list_keys)):
                return str(opc)
            else:
                print("=" * 15 + "'{}' is not a valid option".format(opc) + "=" * 15)
                input("Press enter to continue")


def checkPassword(password):
    minus = False
    majus = False
    nums = False
    blanks = True
    if 8 <= len(password) <= 12:
        for character in password:
            if character.isupper():
                majus = True
            elif character.islower():
                minus = True
            elif character.isnumeric():
                nums = True
            elif character.isspace():
                blanks = False
    else:
        if 8 > len(password):
            print("Your password is too short!")
        else:
            print("Your password is too long!")
        return False
    if majus and minus and nums and blanks:
        return True
    else:
        print("Errors: ")
        if not majus:
            print("-The passwords must have capital letters")
        if not minus:
            print("-The passwords must have lowercase letters")
        if not nums:
            print("-The passwords must have numbers")
        if not blanks:
            print("-The passwords must not have spaces")
        return False


# opc = input("Contraseña ->")
# print(checkPassword(opc))

def checkUser(user):
    if (6 <= len(user) <= 10) and user.isalpha():
        return True
    else:
        print("The user must have between 6-10 characters")
        return False


# opc = input("Usuari ->")
# print(checkUser(opc))

# ----------------------------------------------------------------------------------------------------Parte de SQL

def insertUser(user, password):
    query = f"insert into USER (password,user_name,date_creation) values('{password}','{user}'," \
            f"'{datetime.today().strftime('%Y-%m-%d')}')"
    cur.execute(query)
    conn.commit()


# {'NomUsuari': {'password': 'passwordDelUsuari', 'idUser': id de l’usuari}, 'Jordi': {'password':
# '1234', 'idUser': 2}}


def getUserIds():
    list_iduser = []
    list_username = []
    query_id = f"select id_user from USER order by id_user asc"
    query_name = f"select user_name from USER order by id_user asc"
    cur.execute(query_id)
    id_rows = cur.fetchall()
    cur.execute(query_name)
    name_rows = cur.fetchall()
    for i in range(len(id_rows)):
        list_iduser.append(id_rows[i][0])
        list_username.append(name_rows[i][0])
    list_res = [list_username, list_iduser]
    return list_res


# Devuelve el diccionario 'Adventures' que es del tipo {id_aventura:{Nombre,descripcion,id_personajes},...}
def get_adventures_with_chars():
    dic_adv = {}
    id_list = []
    query_id = f"select id_adventure from ADVENTURE order by id_adventure asc"
    cur.execute(query_id)
    id = cur.fetchall()
    # Mete todos los id de todas las aventuras en una lista
    for i in id:
        id_list.append(i[0])
    # Busca el nombre de la aventura, su descripción y el id de los personajes que la forman a partir de la lista de ids
    for i in id_list:
        dic_properties = {}
        id_characters = []

        query_name = f"select adventure_name from ADVENTURE where id_adventure = '{i}'"
        cur.execute(query_name)
        name = cur.fetchone()
        dic_properties["Name"] = name[0]

        query_description = f"select description from ADVENTURE where id_adventure = '{i}'"
        cur.execute(query_description)
        description = cur.fetchone()
        dic_properties["Description"] = description[0]

        query_characters = f"select id_character from CHARACTER_ADVENTURE where id_adventure = '{i}'"
        cur.execute(query_characters)
        characters = cur.fetchall()
        for j in characters:
            id_characters.append(j[0])
        dic_properties["Characters"] = id_characters

        dic_adv[i] = dic_properties
    return dic_adv

# Funcion que devuelve un diccionario con los nombres como clave y un diccionario con la contra y el id como valor
def getUsers():
    dic_users = {}
    query_idusers = f"select id_user from USER order by id_user asc"
    cur.execute(query_idusers)
    idusers = cur.fetchall()
    query_username = f"select user_name from USER order by id_user asc"
    cur.execute(query_username)
    usernames = cur.fetchall()
    query_passw = f"select password from USER order by id_user asc"
    cur.execute(query_passw)
    passws = cur.fetchall()
    for i in range(len(idusers)):
        dic_users[str(usernames[i][0])] = {'Password': passws[i][0], 'idUser': idusers[i][0]}
    return dic_users


# Funcion que devuelve True si el usuario existe y False en caso contrario
def userExists(user):
    users_list = []
    query_user = f"select user_name from USER"
    cur.execute(query_user)
    tuple_users = cur.fetchall()
    for i in tuple_users:
        users_list.append(i[0])
    if user in users_list:
        return True
    else:
        return False


# Mira que exista el usuario y la contraseña, si no existe el usuario devuelve 0, si la contra esta mal devuelve -1, y
# si esta bien devuelve 1.
def checkUserbdd(user, password):
    if userExists(user):
        query_pass = f"select password from USER where user_name = '{user}'"
        cur.execute(query_pass)
        real_pass = cur.fetchone()
        if real_pass[0] == password:
            return 1
        else:
            return -1
    else:
        return 0


def insertCurrentGame(idUser, isChar, idAdventure):
    query_insert = f"insert into GAME (id_adventure,id_character,id_user,date)" \
                   f" values ('{idAdventure}','{isChar}','{idUser}','{datetime.today().strftime('%Y-%m-%d')}')"
    cur.execute(query_insert)
    conn.commit()


def insertCurrentChoice(idGame, actual_id_step, id_answer):
    query_insert = f"insert into ADVENTURE_SAVE (id_game,id_step,id_option) " \
                   f"values ('{idGame}','{actual_id_step}','{id_answer}')"
    cur.execute(query_insert)
    conn.commit()


def get_table(query):
    list_colums = []
    cur.execute(query)
    colums = cur.description
    rows = cur.fetchall()
    for i in colums:
        list_colums.append(i[0])
    tuple_colums = (tuple(list_colums),)
    tuple_colums += rows
    return tuple_colums


def get_characters():
    dic_chars = {}
    query_idchars = f"select id_character from CHOOSE_YOUR_ADVENTURE.CHARACTER order by id_character asc"
    cur.execute(query_idchars)
    idchars = cur.fetchall()
    query_namechars = f"select character_name from CHOOSE_YOUR_ADVENTURE.CHARACTER order by id_character asc"
    cur.execute(query_namechars)
    namechars = cur.fetchall()
    for i in range(len(idchars)):
        dic_chars[idchars[i][0]] = namechars[i][0]
    return dic_chars


def getIdGames():
    list_idgames = []
    query_idgames = f"select id_game from GAME order by id_game asc"
    cur.execute(query_idgames)
    idgames = cur.fetchall()
    for i in range(len(idgames)):
        list_idgames.append(idgames[i][0])
    tuple_idgames = tuple(list_idgames)
    return tuple_idgames

def getReplayAdventures():
    dic_replays = {}
    tuple_idgames = getIdGames()
    for i in range(len(tuple_idgames)):
        query_iduser = f"select id_user from GAME where id_game = ('{tuple_idgames[i]}')"
        cur.execute(query_iduser)
        idusers = cur.fetchone()

        query_username = f"select user_name from USER where id_user = ('{idusers[0]}')"
        cur.execute(query_username)
        user_name = cur.fetchone()

        query_idadventure = f"select id_adventure from GAME where id_game = ('{tuple_idgames[i]}')"
        cur.execute(query_idadventure)
        idadventure = cur.fetchone()

        query_advname = f"select adventure_name from ADVENTURE where id_adventure = ('{idadventure[0]}')"
        cur.execute(query_advname)
        advname = cur.fetchone()

        query_date = f"select date from GAME where id_game = ('{tuple_idgames[i]}')"
        cur.execute(query_date)
        date = cur.fetchone()

        query_idchar = f"select id_character from GAME where id_game = ('{tuple_idgames[i]}')"
        cur.execute(query_idchar)
        idchar = cur.fetchone()

        query_charname = f"select character_name from CHOOSE_YOUR_ADVENTURE.CHARACTER" \
                         f" where id_character = ('{idchar[0]}')"
        cur.execute(query_charname)
        charname = cur.fetchone()

        dic_replays[tuple_idgames[i]] = {'idUser': idusers[0], 'Username': user_name[0], 'idAdventure': idadventure[0],
                                         'Name': advname[0], 'Date': date[0],
                                         'id_character': idchar[0], 'character_name': charname[0]}

    return dic_replays

def get_id_bystep_adventure():
    id_by_steps = {}

    #Llamo a la funcion getIdGames para cojer el último id
    id_game = getIdGames()
    id_game = id_game[len(id_game) - 1]
    get_adventures_with_chars()

    #Query para conseguir el id de aventura a partir del id del ultimo juego
    query_idadventure = f"select id_adventure from GAME where id_game = ('{id_game}')"
    cur.execute(query_idadventure)
    idadventure = cur.fetchone()
    idadventure = idadventure[0]

    #Query para sacar la tupla de tuplas que contienen los pasos de esa aventura
    query_idstep = f"select id_step from STEP where id_adventure = ('{idadventure}') order by id_step asc"
    cur.execute(query_idstep)
    id_steps = cur.fetchall()
    list_steps = []
    for i in range (len(id_steps)):
        list_steps.append(id_steps[i][0])

    #Query para sacar la tupla de tuplas que contienen la descripción de cada paso
    query_description = f"select description from STEP where id_adventure = ('{idadventure}') order by id_step asc"
    cur.execute(query_description)
    description = cur.fetchall()

    #Query para sacar todos los las last_step
    query_laststep = f"select last_step from CHOOSE_YOUR_ADVENTURE.OPTION order by id_option asc"
    cur.execute(query_laststep)
    laststep = cur.fetchall()
    list_laststep = []
    for i in range (len(laststep)):
        list_laststep.append(laststep[i][0])

    #For para ver si tiene paso final cada step
    for i in range (len(list_steps)):
        query_finalstep = f"select end_step from STEP where id_step = ('{list_steps[i]}')"
        cur.execute(query_finalstep)
        final_step = cur.fetchone()
        final_step = final_step[0]

        # Crea una tupla con las opciones que puede escojer cada step
        query_idoption = f"select id_option from CHOOSE_YOUR_ADVENTURE.OPTION where last_step = ('{list_steps[i]}')"
        cur.execute(query_idoption)
        idoption = cur.fetchall()
        list_idoption = []
        for x in range (len(idoption)):
            list_idoption.append(idoption[x][0])
        tuple_finalsteps = tuple (list_idoption)

        id_by_steps[list_steps[i]] = {'Description':description[i][0],'answer_in_step':tuple_finalsteps,
                                                   'Final_Step':final_step}
    return id_by_steps
# ------------------------------------------------------------------------------------------------------------

def get_first_step_adventure():
    id_by_steps = get_id_bystep_adventure()
    # Llamo a la funcion getIdGames para cojer el último id
    id_game = getIdGames()
    id_game = id_game[len(id_game) - 1]

    get_adventures_with_chars()

    # Query para conseguir el id de aventura a partir del id del ultimo juego
    query_idadventure = f"select id_adventure from GAME where id_game = ('{id_game}')"
    cur.execute(query_idadventure)
    idadventure = cur.fetchone()
    idadventure = idadventure[0]

    # Query para sacar la tupla de tuplas que contienen los pasos de esa aventura
    query_idstep = f"select id_step from STEP where id_adventure = ('{idadventure}') order by id_step asc"
    cur.execute(query_idstep)
    id_steps = cur.fetchall()

    return id_by_steps[id_steps[0][0]]


# {(idAnswers_ByStep_Adventure, idByStep_Adventure): {'Description': 'descripció daquest pas',
# 'Resolution_Answer': 'Texte al camp resolution answer de la taula a la BBDD', 'NextStep_Adventure': id del
# seguent pas}, (2, 1): {'Description': 'Escoge el camino del centro, del que parecen provenir ruidos de ramas al
# romperse y astillarse ...', 'Resolution_Anwer': 'Piensas que para ser digno de la espada de las valkirias, debes
# de afrontar tus miedos y peligros que acechan', 'NextStep_Adventure': 3}....}
def get_answers_bystep_adventure():
    idAnswers_ByStep_Adventure = {}
    id_by_steps = get_id_bystep_adventure()

    query_idgames = f"select id_option from ADVENTURE_SAVE order by id_adventure_save desc"
    cur.execute(query_idgames)
    id_option = cur.fetchall()[0][0]
    print("ID OPTION = ",id_option)

    # Query para sacar el ultimo paso escogido
    query_idstep = f"select last_step from CHOOSE_YOUR_ADVENTURE.OPTION where id_option = ('{id_option}')"
    cur.execute(query_idstep)
    id_steps = cur.fetchone()

    if len(id_steps) == 0:
        id_steps = 1
    else:
        id_steps = id_steps[0]

    #Tupla con los id_options posibles de cada step (last_step)
    #idsteps -->  {1:{'answers_in_step': (tupla amb els ids de les opcions posibles en aquest pas ), 'Final_Step': 0 }}
    tuple_id_answers = id_by_steps[id_steps]["answer_in_step"]

    for i in range(len(tuple_id_answers)):
        query_desc = f"select description from CHOOSE_YOUR_ADVENTURE.OPTION where id_option = ('{tuple_id_answers[i]}')"
        cur.execute(query_desc)
        description = cur.fetchone()[0]

        #Query per sacar answer del pas seleccionat
        query_answer = f"select answer from CHOOSE_YOUR_ADVENTURE.OPTION where id_option = ('{tuple_id_answers[i]}')"
        cur.execute(query_answer)
        answer = cur.fetchone()[0]

        #Query per sacar el id del següent pas
        query_next= f"select next_step from CHOOSE_YOUR_ADVENTURE.OPTION where id_option = ('{tuple_id_answers[i]}')"
        cur.execute(query_next)
        id_next = cur.fetchone()[0]

        #idAnswers_ByStep_Adventure[id_option siguiente , step actual]= {descripcion,respuesta,next_Step}
        idAnswers_ByStep_Adventure[(tuple_id_answers[i],id_steps)] =\
            {"Description":description,"Resolution_Answer":answer,"NextStep_Adventure":id_next}

    return idAnswers_ByStep_Adventure
print(get_answers_bystep_adventure())
def getChoices():
    a = get_id_bystep_adventure()
    b = get_answers_bystep_adventure()
    tuple_Res = (a,b)
    return tuple_Res
#-----------------------------------------------------------------FALTA
# #((1,14))
# #((1,2),(2,7))
# #necesitaria el id_game, sino no puedo saber el id_adventure que necesita imprimir
# def replay(choices):
#     for step in choices:
#         for options in step:
#             query_
#--------------------------------------------------------------------------


def getFormatedTable(queryTable,title=""):
    list_len_text = []
    space_left = 120
    #Añado a una lista los espacios que tiene cada columna equitativamente
    for i in range(len(queryTable[0])):
        list_len_text.append(120//len(queryTable[0]))
        space_left -= (120//len(queryTable[0]))

    while space_left != 0:
        for i in range(len(list_len_text)):
            if space_left != 0:
                list_len_text[i] += 1
                space_left -= 1

    for i in range(len(list_len_text)):
        list_len_text[i] = list_len_text[i] - len(queryTable[0][i])

    for i in range(len(list_len_text)*2):
        for j in range(len(list_len_text)-1):
            if list_len_text[j] > list_len_text[j+1]:
                list_len_text[j] = list_len_text[j] - 1
                list_len_text[j+1] = list_len_text[j+1] + 1

    tuple_lentext = tuple(list_len_text)
    header = (getHeadeForTableFromTuples(queryTable[0],tuple_lentext,title)) +"\n"+("*"*120)
    content = ""
    for i in range(1,len(queryTable)):
        content += "\n" + getFormatedBodyColumns(queryTable[i],tuple_lentext)

    return header+content

def idoptionstoidnextstep (tuple_idoptions):
    list_idnextstep = []
    for i in range (len(tuple_idoptions)):
        query_idnext = f"select next_step from CHOOSE_YOUR_ADVENTURE.OPTION where id_option = ('{tuple_idoptions[i]}')"
        cur.execute(query_idnext)
        list_idnextstep.append(cur.fetchone()[0])
    return tuple(list_idnextstep)

#print(getFormatedTable(get_table(f"select answer,description,user_create from CHOOSE_YOUR_ADVENTURE.OPTION"),"USUARIOS"))
