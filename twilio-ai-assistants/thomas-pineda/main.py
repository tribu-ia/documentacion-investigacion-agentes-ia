import os
import json
import base64
import asyncio
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.websockets import WebSocketDisconnect
from twilio.twiml.voice_response import VoiceResponse, Connect, Say, Stream
from dotenv import load_dotenv
from aiohttp import ClientSession, WSMsgType

load_dotenv()

# Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # requires OpenAI Realtime API Access
PORT = int(os.getenv('PORT', 5050))

                                                                                                                                                        # SYSTEM_MESSAGE = (
                                                                                                                                                        #     "Eres un asistente de la empresa llamada Agenx.AI, empresa dedicada al desarrollo de Inteligencia Artificial y a la automatización de procesos basados en AI. "
                                                                                                                                                        #     "Tú tarea será la de conversar con futuros clientes y contarles acerca de los servicios de Agenx.AI. "
                                                                                                                                                        #     "Agenx.AI ofrece servicios de desarrollo de Inteligencia aritificial, acá un poco de contexto: "
                                                                                                                                                        #     "En Agenx.AI impulsamos la eficiencia de las empresas mediante automatizaciones inteligentes que eliminan tareas operativas y repetitivas. Nuestro objetivo es liberar a los equipos de trabajo para que se concentren en lo que realmente importa: hacer crecer su negocio. Con nuestras soluciones basadas en Inteligencia Artificial, optimizamos procesos, reducimos costos y potenciamos la productividad."
                                                                                                                                                        # )

nombre = "Thomas Pineda"
Puesto = "Científico de datos"
# SYSTEM_MESSAGE = (f"""Tú Nombre es Andrés AI Recluter. Actúa como un reclutador experto en reclutamiento de posiciones que tengan que ver con Analítica de datos de la empresa 'Agenx AI'. 
# Tú tarea será entrevistar a {nombre}, el cual es un candidato que se está postulando a un puesto de {Puesto}, hazles las preguntas que
# consideres necesarias para evaluar sus conocimientos, experiencias y habilidades para este cargo y ver si es un candidato idoneo, aquí tienes el contexto del cargo.

# Contexto:
# Un científico de datos (o data scientist) es un profesional especializado en la recolección, análisis e interpretación de grandes volúmenes de datos. Su objetivo es extraer conocimientos valiosos para tomar decisiones informadas, resolver problemas complejos y predecir tendencias futuras. Este rol es clave en empresas que buscan aprovechar sus datos para mejorar procesos, optimizar operaciones o desarrollar productos innovadores.

# Herramientas que debe manejar:
# Lenguajes de programación:

# Python: Es uno de los lenguajes más utilizados debido a su facilidad, robustez y las bibliotecas específicas para análisis de datos (como pandas, numpy, scikit-learn, matplotlib, seaborn).
# R: Es ampliamente usado en estadísticas y análisis de datos, especialmente en áreas de investigación.
# SQL: Esencial para trabajar con bases de datos, realizar consultas y gestionar datos estructurados.
# Herramientas de análisis y manipulación de datos:

# pandas: Para manipulación y análisis de datos en estructuras como DataFrames.
# NumPy: Para cálculo numérico y manejo de matrices.
# SciPy: Para cálculos científicos avanzados.
# Frameworks de Machine Learning:

# scikit-learn: Para crear modelos de machine learning supervisados y no supervisados.
# TensorFlow o PyTorch: Herramientas de deep learning para construir modelos más complejos.
# Keras: Interfaz para crear redes neuronales profundas.
# Plataformas de Big Data:

# Apache Hadoop y Apache Spark: Para procesar grandes volúmenes de datos en entornos distribuidos.
# Visualización de datos:

# Tableau o Power BI: Herramientas para crear dashboards interactivos.
# Matplotlib, Seaborn o Plotly: Bibliotecas en Python para visualización de datos.
# Entornos de trabajo colaborativos:

# Jupyter Notebooks: Ideal para análisis interactivo y presentación de resultados.
# Git: Para control de versiones y colaboración en proyectos de datos.
# Skills (habilidades) necesarias:
# Estadística y matemáticas:

# Conocimiento de conceptos estadísticos (distribuciones, pruebas de hipótesis, regresión, etc.) y matemáticas (álgebra lineal, cálculo).
# Machine learning:

# Entender algoritmos de aprendizaje supervisado y no supervisado, así como técnicas de optimización.
# Programación:

# Ser competente en lenguajes como Python, R y SQL.
# Manejo de grandes volúmenes de datos:

# Comprender cómo manejar, limpiar y transformar grandes datasets.
# Comunicación efectiva:

# Poder explicar resultados técnicos a audiencias no técnicas y presentar insights de manera clara y visual.
# Resolución de problemas:

# Habilidad para abordar problemas complejos y pensar críticamente sobre los datos.
# Conocimiento del negocio:

# Comprender las necesidades del negocio para traducir preguntas y problemas en análisis de datos significativos.
# Responsabilidades de un científico de datos:
# Recolección y preparación de datos:

# Obtener datos desde diversas fuentes (bases de datos, APIs, archivos, etc.) y procesarlos para que sean utilizables.
# Análisis exploratorio de datos (EDA):

# Investigar los datos para identificar patrones, tendencias y correlaciones. Esto incluye la limpieza y transformación de los datos.
# Desarrollo de modelos predictivos:

# Construir y entrenar modelos de machine learning para hacer predicciones o clasificaciones basadas en los datos.
# Evaluación y ajuste de modelos:

# Probar la efectividad de los modelos utilizando métricas de rendimiento (precisión, recall, F1-score, etc.) y realizar ajustes para mejorar su rendimiento.
# Comunicación de resultados:

# Presentar los hallazgos y recomendaciones a los stakeholders (gerentes, directores, etc.) de manera comprensible.
# Automatización de procesos:

# Crear scripts y procesos automatizados para la recolección y análisis continuo de datos.
# Colaboración multidisciplinaria:

# Trabajar junto con otros departamentos (TI, marketing, operaciones, etc.) para alinear las soluciones de datos con los objetivos de la empresa.
# En resumen, un científico de datos debe ser una persona con una sólida base en matemáticas, programación y estadística, además de contar con habilidades para comunicar de forma efectiva sus hallazgos. También debe estar familiarizado con las herramientas tecnológicas más modernas para procesar y analizar datos.
# """

# )

SYSTEM_MESSAGE = (
    "Eres un asistente de la empresa de 'Agenx AI ', tú tarea será la de comunicarte con posibles clientes y ofrecerles el servicio de la Agenx AI"
    "Actúa como un experto en técnologias de Inteligencia artificial y ofrece soluciones basadas en estas para la empresa a la que llames"
    "Intenta agendar una reunión con el posible cliente para charlar sobre como podemos automatizar sus procesos con AI "
    "Agenx AI es una empresa que se dedica a la creación de software basado en AI y en automatizaciones de procesos con inteligencia artificial. En Agenx.AI impulsamos la eficiencia de las empresas mediante automatizaciones inteligentes que eliminan tareas operativas y repetitivas. Nuestro objetivo es liberar a los equipos de trabajo para que se concentren en lo que realmente importa: hacer crecer su negocio. Con nuestras soluciones basadas en Inteligencia Artificial, optimizamos procesos, reducimos costos y potenciamos la productividad."
)


VOICE = 'alloy'
LOG_EVENT_TYPES = [
    'response.content.done', 'rate_limits.updated', 'response.done',
    'input_audio_buffer.committed', 'input_audio_buffer.speech_stopped',
    'input_audio_buffer.speech_started', 'session.created'
]
app = FastAPI()
if not OPENAI_API_KEY:
    raise ValueError('Missing the OpenAI API key. Please set it in the .env file.')

@app.get("/", response_class=JSONResponse)
async def index_page():
    return {"message": "Twilio Media Stream Server is running!"}

@app.api_route("/incoming-call", methods=["GET", "POST"])
async def handle_incoming_call(request: Request):
    """Handle incoming call and return TwiML response to connect to Media Stream."""
    response = VoiceResponse()
    # <Say> punctuation to improve text-to-speech flow
    response.say("Please wait while we connect your call to the A. I. voice assistant, powered by Twilio and the Open-A.I. Realtime API")
    response.pause(length=1)
    response.say("O.K. you can start talking!")
    host = request.url.hostname
    connect = Connect()
    connect.stream(url=f'wss://{host}/media-stream')
    response.append(connect)
    return HTMLResponse(content=str(response), media_type="application/xml")

@app.websocket("/media-stream")
async def handle_media_stream(websocket: WebSocket):
    """Handle WebSocket connections between Twilio and OpenAI."""
    print("Client connected")
    await websocket.accept()

    # Establecer la conexión WebSocket con OpenAI usando aiohttp
    async with ClientSession() as session:
        async with session.ws_connect(
            'wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2024-10-01',
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "OpenAI-Beta": "realtime=v1"
            }
        ) as openai_ws:
            await send_session_update(openai_ws)
            stream_sid = None

            async def receive_from_twilio():
                """Receive audio data from Twilio and send it to the OpenAI Realtime API."""
                nonlocal stream_sid
                try:
                    async for message in websocket.iter_text():
                        data = json.loads(message)
                        if data['event'] == 'media' and not openai_ws.closed:
                            audio_append = {
                                "type": "input_audio_buffer.append",
                                "audio": data['media']['payload']
                            }
                            await openai_ws.send_json(audio_append)
                        elif data['event'] == 'start':
                            stream_sid = data['start']['streamSid']
                            print(f"Incoming stream has started {stream_sid}")
                except WebSocketDisconnect:
                    print("Client disconnected.")
                    if not openai_ws.closed:
                        await openai_ws.close()

            async def send_to_twilio():
                nonlocal stream_sid
                try:
                    async for openai_message in openai_ws:
                        if openai_message.type == WSMsgType.TEXT:
                            response = json.loads(openai_message.data)
                            if response['type'] in LOG_EVENT_TYPES:
                                print(f"Received event: {response['type']}", response)
                            if response['type'] == 'session.updated':
                                print("Session updated successfully:", response)
                            if response['type'] == 'response.audio.delta' and response.get('delta'):
                                # Audio from OpenAI
                                try:
                                    audio_payload = base64.b64encode(base64.b64decode(response['delta'])).decode('utf-8')
                                    audio_delta = {
                                        "event": "media",
                                        "streamSid": stream_sid,
                                        "media": {
                                            "payload": audio_payload
                                        }
                                    }
                                    await websocket.send_json(audio_delta)
                                except Exception as e:
                                    print(f"Error processing audio data: {e}")
                        elif openai_message.type == WSMsgType.ERROR:
                            print(f"WebSocket error: {openai_message.data}")
                except Exception as e:
                    print(f"Error in send_to_twilio: {e}")

            await asyncio.gather(receive_from_twilio(), send_to_twilio())

async def send_session_update(openai_ws):
    """Send session update to OpenAI WebSocket."""
    session_update = {
        "type": "session.update",
        "session": {
            "turn_detection": {"type": "server_vad"},
            "input_audio_format": "g711_ulaw",
            "output_audio_format": "g711_ulaw",
            "voice": VOICE,
            "instructions": SYSTEM_MESSAGE,
            "modalities": ["text", "audio"],
            "temperature": 0.8,
        }
    }
    print('Sending session update:', json.dumps(session_update))
    await openai_ws.send_json(session_update)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
