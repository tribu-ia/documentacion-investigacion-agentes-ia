import os
from dotenv import load_dotenv
from trello import TrelloClient

from crewai.tools import tool

load_dotenv()

API_KEY = os.environ.get('TRELLO_API_KEY') # Es recomendable usar variables de entorno para no exponer tus credenciales
API_SECRET = os.environ.get('TRELLO_API_SECRET') # Es recomendable usar variables de entorno para no exponer tus credenciales
TOKEN = os.environ.get('TRELLO_TOKEN') # Es recomendable usar variables de entorno para no exponer tus credenciales
BOARD_ID = 'LtsRVJ8A'#os.environ.get('TRELLO_BOARD_ID') # Reemplaza con tu Board ID

def crear_tarjeta_trello(columna_base_nombre, titulo_tarjeta, descripcion_tarjeta):
    """
    Crea una tarjeta de Trello en la columna base especificada.

    Args:
        api_key (str): Tu API key de Trello.
        api_secret (str): Tu API secret de Trello.
        token (str): Tu token de Trello.
        board_id (str): El ID del tablero de Trello.
        columna_base_nombre (str): El nombre de la columna base donde se creará la tarjeta.
        titulo_tarjeta (str): El título de la nueva tarjeta.
        descripcion_tarjeta (str): La descripción de la nueva tarjeta.

    Returns:
        str: El ID de la tarjeta recién creada, o None si ocurre un error.
    """
    try:
        client = TrelloClient(
            api_key=API_KEY,
            api_secret=API_SECRET,
            token=TOKEN
        )

        tablero = client.get_board(BOARD_ID)
        columnas = tablero.list_lists()
        columna_base = None
        for columna in columnas:
            if columna.name == columna_base_nombre:
                columna_base = columna
                break

        if columna_base:
            nueva_tarjeta = columna_base.add_card(titulo_tarjeta, desc=descripcion_tarjeta)
            return nueva_tarjeta.id
        else:
            print(f"No se encontró la columna base con el nombre: {columna_base_nombre}")
            return None

    except Exception as e:
        print(f"Ocurrió un error al crear la tarjeta de Trello: {e}")
        return None

def crear_comentario_tarjeta_trello(tarjeta_id, texto_comentario):
    """
    Crea un comentario en una tarjeta de Trello determinada.

    Args:
        api_key (str): Tu API key de Trello.
        api_secret (str): Tu API secret de Trello.
        token (str): Tu token de Trello.
        tarjeta_id (str): El ID de la tarjeta de Trello donde se añadirá el comentario.
        texto_comentario (str): El texto del comentario a añadir.

    Returns:
        bool: True si el comentario se creó correctamente, False si ocurre un error.
    """
    try:
        client = TrelloClient(
            api_key=API_KEY,
            api_secret=API_SECRET,
            token=TOKEN
        )
        tarjeta = client.get_card(tarjeta_id)
        tarjeta.comment(texto_comentario)
        return True
    except Exception as e:
        print(f"Ocurrió un error al crear el comentario en la tarjeta de Trello: {e}")
        return False


def listar_tarjetas_columna_trello(nombre_columna):
    """
    Lista las tarjetas disponibles en una columna de Trello determinada, con detalles y comentarios.

    Args:
        board_id (str): El ID del tablero de Trello.
        nombre_columna (str): El nombre de la columna de Trello de la cual se listarán las tarjetas.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa una tarjeta con su nombre,
              descripción y una lista de comentarios organizados por fecha. Retorna una lista vacía si no se
              encuentra la columna o si hay un error.
    """
    try:
        client = TrelloClient(
            api_key=API_KEY,
            api_secret=API_SECRET,
            token=TOKEN
        )

        tablero = client.get_board(BOARD_ID)
        columnas = tablero.list_lists()
        columna_deseada = None
        for columna in columnas:
            if columna.name == nombre_columna:
                #print(f'columna deseada: {columna.name}')
                columna_deseada = columna
                break

        if columna_deseada:
            tarjetas = columna_deseada.list_cards()
            lista_tarjetas_detalles = []
            for tarjeta in tarjetas:
                # Cambio importante: Acceder a los comentarios directamente con tarjeta.comments
                comentarios_trello = tarjeta.comments
                comentarios = []
                for comentario_trello in comentarios_trello:
                    #print(f'comentario trello : {comentario_trello['id']}')
                    comentarios.append({
                        'id': comentario_trello['id'],  # Añadido ID del comentario
                        'fecha': comentario_trello['date'],
                        'texto': comentario_trello['data'][
                            'text'] if 'text' in comentario_trello['data'] else comentario_trello['data'].get('message',
                                                                                                        'Sin texto disponible')
                        # Manejo de 'message' si 'text' no está
                    })
                comentarios_ordenados = sorted(comentarios, key=lambda k: k['fecha'])

                lista_tarjetas_detalles.append({
                    'id': tarjeta.id,
                    'nombre': tarjeta.name,
                    'descripcion': tarjeta.desc,
                    'comentarios': comentarios_ordenados
                })
            return lista_tarjetas_detalles
        else:
            print(f"No se encontró la columna con el nombre: {nombre_columna}")
            return []

    except Exception as e:
        print(f"Ocurrió un error al listar las tarjetas de la columna de Trello: {e}")
        return []


def cambiar_estado_tarjeta_trello(tarjeta_id, nuevo_estado_columna_nombre):
    """
    Cambia el estado de una tarjeta de Trello, moviéndola a una nueva columna.

    Args:
        tarjeta_id (str): El ID de la tarjeta de Trello a mover.
        nuevo_estado_columna_nombre (str): El nombre de la columna de destino (nuevo estado).

    Returns:
        bool: True si el estado se cambió correctamente, False si ocurre un error.
    """
    try:
        client = TrelloClient(
            api_key=API_KEY,
            api_secret=API_SECRET,
            token=TOKEN
        )

        tablero = client.get_board(BOARD_ID)
        columnas = tablero.list_lists()
        columna_destino = None
        for columna in columnas:
            if columna.name == nuevo_estado_columna_nombre:
                columna_destino = columna
                break

        if not columna_destino:
            print(f"No se encontró la columna de destino con el nombre: {nuevo_estado_columna_nombre}")
            return False

        tarjeta = client.get_card(tarjeta_id)
        tarjeta.change_list(columna_destino.id) # Mueve la tarjeta a la nueva columna
        return True

    except Exception as e:
        print(f"Ocurrió un error al cambiar el estado de la tarjeta de Trello: {e}")
        return False


@tool("trello_tool_create")
def trello_tool_create(columna: str, titulo_tarjeta: str, descripcion_tarjeta: str) -> str:
    """Esta herramienta permite crear tarjetas que representan historias de usuario o historias técnicas en Trello.
    - columna: Columna en la cual se va a crear la tarjeta.
    - titulo_tarjeta: Título de la tarjeta.
    - descripcion_tarjeta: Descripción de la tarjeta
    """
    print(f'''
        Llamado a Herramienta Trello (CREAR TARJETA):
        Parametros de entrada:  
        - columna: {columna}, 
        - titulo_tarjeta: {titulo_tarjeta}, 
        - descripcion_tarjeta: {descripcion_tarjeta}
    ''')

    response = crear_tarjeta_trello(columna, titulo_tarjeta, descripcion_tarjeta)
    print(f'Respuesta CREAR desde trello: {response}')
    return response


@tool("trello_tool_comment")
def trello_tool_comment(tarjeta_id: str, texto_comentario: str) -> str:
    """Esta herramienta permite crear un comentario en una tarea determinada en Trello
    - tarjeta_id: Identificador de la tarjeta.
    - texto_comentario: Comentario a incluir en la tarjeta
    """
    print(f'''
        Llamado a Herramienta Trello (COMENTAR TARJETA):
        Parametros de entrada: 
        - tarjeta_id: {tarjeta_id}, 
        - texto_comentario: {texto_comentario} 
    ''')
    # Function logic here
    print("Comentar tickets")
    response = crear_comentario_tarjeta_trello(tarjeta_id, texto_comentario)
    print(f'Respuesta CREAR COMENTARIO desde trello: {response}')
    return response

@tool("trello_tool_list")
def trello_tool_list(columna: str) -> str:
    """Esta herramienta permite listar todas las tarjetas existentes en una columna
    - columna: Columna a listar, los valores pueden ser: TODO, REFINAMIENTO
    """
    print(f'''
        Llamado a Herramienta Trello (LISTAR TARJETAS):
        Parametros de entrada: 
        - columna: {columna}, 
    ''')
    # Function logic here
    print("Listar tickets")
    response = listar_tarjetas_columna_trello(columna)
    print(f'Respuesta LISTAR desde trello: {response}')
    return response

@tool("trello_tool_change_column")
def trello_tool_change_column(tarjeta_id: str, nueva_columna: str) -> str:
    """Esta herramienta permite mover la tarjeta a un nuevo estado
    - tarjeta_id: identificador de la tarjeta
    - nueva_columna: Columna a listar, los valores pueden ser: TODO, REFINAMIENTO
    """
    print(f'''
        Llamado a Herramienta Trello (CAMBIAR COLUMNA):
        Parametros de entrada: 
        - columna: {nueva_columna}, 
    ''')
    # Function logic here
    print("Listar tickets")
    response = cambiar_estado_tarjeta_trello(tarjeta_id, nueva_columna)
    print(f'Respuesta CAMBIAR ESTADO COLUMNA desde trello: {response}')
    return response
