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

def getUsers():
    print("escribir")
def get_answers_bystep_adventure():
    idAnswers_ByStep_Adventure = {}
    idAnswers_ByStep_Adventure["id_answer"] = "the actual answer"
    return idAnswers_ByStep_Adventure


# FUNCIONES QUE FALTAN POR IMPLEMENTAR(TIENEN PARTE DE SQL)
# def get_id_bystep_adventure():
# def get_first_step_adventure():
# def get_characters():
# def getReplayAdventures():
# def getChoices():
# def getIdGames():
# def insertCurrentGame(idGame,idUser,isChar,idAdventure):
# def get_table(query):
# def setIdGame():
# def insertCurrentChoice(idGame,actual_id_step,id_answer):
# def getFormatedTable(queryTable,title=""):
# def userExists(user):
# def replay(choices):

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

# Mira que exista el usuario y la contraseña, si no existe el usuario devuelve 0, si la contra esta mal devuelve -1, y
# si esta bien devuelve 1.
def checkUserbdd(user, password):
    users_list = []
    password_list = []
    query_user = f"select user_name from USER order by id_user asc"
    cur.execute(query_user)
    users = cur.fetchall()
    # Crea una lista con todos los usuarios ordenados por id
    for i in users:
        users_list.append(i[0])

    query_password = f"select password from USER order by id_user asc"
    cur.execute(query_password)
    passwords = cur.fetchall()
    # Crea una lista con todas las contraseñas ordenadas por id
    for i in passwords:
        password_list.append(i[0])

    if user in users_list:
        if password == password_list[users_list.index(user)]:
            return 1
        else:
            return -1
    else:
        return 0
