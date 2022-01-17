from datetime import datetime
import pymysql

conn = pymysql.connect(host="52.157.66.187", user="aleix", password="1Q2w3e4r5t6y", db="CHOOSE_YOUR_ADVENTURE")
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
    print("*"*100)
    print("                ########  ######## ########   #######  ########  ########  ######  "
          "\n                ##     ## ##       ##     ## ##     ## ##     ##    ##    ##    ## "
          "\n                ##     ## ##       ##     ## ##     ## ##     ##    ##    ##       "
          "\n                ########  ######   ########  ##     ## ########     ##     ######  "
          "\n                ##   ##   ##       ##        ##     ## ##   ##      ##          ## "
          "\n                ##    ##  ##       ##        ##     ## ##    ##     ##    ##    ## "
          "\n                ##     ## ######## ##         #######  ##     ##    ##     ######  ")
    print("*"*100)

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
        print(textOpts+"\n")
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

#{'NomUsuari': {'password': 'passwordDelUsuari', 'idUser': id de l’usuari}, 'Jordi': {'password':
#'1234', 'idUser': 2}}


def getUserIds():
    query_id = f"select id_user from USER order by id_user asc"
    query_name = f"select user_name from USER order by id_user asc"
    cur.execute(query_id)
    id_rows = cur.fetchall()
    cur.execute(query_name)
    name_rows = cur.fetchall()
    res_list = [id_rows,name_rows]
    return res_list

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

#Funcion que devuelve True si el usuario existe y False en caso contrario
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


def insertCurrentGame(idGame,idUser,isChar,idAdventure):
    query_insert = f"insert into GAME (id_game,id_adventure,id_character,id_user,date)" \
                   f" values ('{idGame}','{idAdventure}','{isChar}','{idUser}','{datetime.today().strftime('%Y-%m-%d')}')"
    cur.execute(query_insert)
    conn.commit()

def insertCurrentChoice(idGame,actual_id_step,id_answer):
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

# -----------------------------------------------------------------------ARREGLAR, NO FORMATA BIEN
def getFormatedTable(queryTable,title=""):
    list_sizecols = []
    #Crea una tupla amb la mesura que ha de tenir cada columna
    num_columns = len(queryTable[0])
    for i in range (num_columns):
        list_sizecols.append((100//num_columns-len(str(queryTable[0][i]))))
    tuple_sizecols = tuple (list_sizecols)
    print("*"*100)
    print(tuple_sizecols)
    print(getHeadeForTableFromTuples(queryTable[0],tuple_sizecols,title))
    return tuple_sizecols

    # for i in id_adventures_list:
    #     stringRes += getFormatedBodyColumns((str(i), adventures[i]["Name"], adventures[i]["Description"]), (13, 35, 45),
    #                                         2) + "\n"


getFormatedTable(get_table(f"select * from USER"), "USUARIOS")



# FUNCIONES QUE FALTAN POR IMPLEMENTAR(TIENEN PARTE DE SQL)
#-Funciones que no comprendo:
    # def setIdGame():#En teoría actualiza la tabla Game con un nuevo game

# def get_id_bystep_adventure():
# def get_first_step_adventure():
# def get_characters():
# def getReplayAdventures():
# def getChoices():
# def getIdGames():
# def replay(choices):
# def getUsers():
# def get_answers_bystep_adventure():

