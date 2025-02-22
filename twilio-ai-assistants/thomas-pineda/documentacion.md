# 1. Introducción

En la actualidad, la atención al cliente enfrenta un desafío constante para adaptarse a las expectativas cambiantes de los consumidores. La emergente tecnología de inteligencia artificial (IA) ha revolucionado este panorama, permitiendo a las empresas ofrecer interacciones más personalizadas, eficientes y accesibles. Dentro de este contexto, los Asistentes de IA de Twilio se presentan como una solución innovadora que combina la sofisticación del procesamiento del lenguaje natural con la flexibilidad de una plataforma modular. Esta herramienta no solo facilita la creación de asistentes virtuales conversacionales, sino que también permite a las organizaciones optimizar sus procesos y mejorar la experiencia del cliente.

Este documento explora en profundidad la manera de desarrollar un asistente virtual comversacional el cual puede llamar a un número de telefono y conversar e interactura mediante voz en tiempo real.

# 2. ¿Qué es Twilio AI Assistants?

## Descripción de Twilio AI Assistants

Twilio AI Assistants es una plataforma de desarrollo de asistentes virtuales conversacionales que permite a los desarrolladores crear experiencias de interacción de voz y texto personalizadas e inteligentes. A diferencia de una simple herramienta de respuesta de voz interactiva (IVR), Twilio AI Assistants se basa en la potencia de la Inteligencia Artificial para ofrecer interacciones más naturales y contextuales. Su arquitectura modular y flexible permite la integración con diversos modelos de lenguaje, incluyendo, aunque no limitándose a, GPT-4, para ofrecer capacidades avanzadas de procesamiento del lenguaje natural (PNL).

### Estructura de la Plataforma

La plataforma se estructura en torno a tres componentes principales:

1. **Flujos de conversación (Conversation Flows):** Estos son los "cerebros" del asistente, definidos mediante un lenguaje de programación visual o mediante código. Los flujos definen la lógica de la conversación, incluyendo la gestión de estados, la enrutamiento de llamadas, la recolección de información del usuario y la respuesta a las solicitudes. Se pueden crear flujos complejos con múltiples ramas y bucles, permitiendo la gestión de conversaciones complejas y dinámicas. Los desarrolladores pueden definir nodos específicos para la integración con modelos de lenguaje externos como GPT-4.

2. **Modelos de lenguaje (Language Models):** Esta capa permite la integración con diferentes modelos de PNL, como GPT-4, para el procesamiento del lenguaje natural. Twilio AI Assistants ofrece una interfaz para conectar con estos modelos, permitiendo que el asistente comprenda el lenguaje natural del usuario, genere respuestas coherentes y contextuales, y realice tareas complejas como la traducción o la generación de texto. La elección del modelo de lenguaje dependerá de las necesidades específicas de la aplicación, considerando factores como el costo, la precisión y las capacidades del modelo.

3. **Canales de comunicación (Communication Channels):** Esta capa permite la interacción con el usuario a través de diferentes canales, incluyendo voz (llamadas telefónicas), SMS, chat en línea y aplicaciones de mensajería. La flexibilidad de Twilio permite que un mismo flujo de conversación pueda ser utilizado en múltiples canales, ofreciendo una experiencia consistente al usuario independientemente del método de interacción.

### Ejemplos de uso

* **Atención al cliente:** Un asistente virtual puede responder preguntas frecuentes, resolver problemas técnicos y guiar a los usuarios a través de los diferentes procesos de la empresa.

* **Ventas y comercio electrónico:** Un asistente puede ayudar a los clientes a encontrar productos, realizar compras y gestionar sus pedidos.

* **Salud:** Un asistente puede programar citas médicas, responder preguntas sobre medicamentos y proporcionar información sobre la salud.

* **Educación:** Un asistente puede ayudar a los estudiantes a acceder a recursos educativos, responder preguntas sobre el material de estudio y proporcionar retroalimentación.

En resumen, Twilio AI Assistants ofrece una plataforma completa y flexible para el desarrollo de asistentes virtuales inteligentes. Su capacidad de integración con modelos de lenguaje de última generación, como GPT-4, junto con sus características de personalización y gestión de la memoria del cliente, permite la creación de experiencias de usuario altamente personalizadas y eficientes.


## 3. Caso de uso

# Documentación del Asistente de Voz con Twilio AI Assistant y OpenAI en Tiempo Real

Imagina poder convertir un simple número de teléfono en un asistente inteligente capaz de conversar, resolver dudas y agendar reuniones como si fuera un humano. **¡Ahora es posible con Twilio, OpenAI y Python!** Este proyecto combina lo mejor de la tecnología de voz en tiempo real con la potencia de la inteligencia artificial para crear una experiencia única. Ya sea para reclutamiento, soporte al cliente o ventas, este asistente de voz está listo para transformar la forma en que interactúas con tus clientes. ¿Listo para dar el salto al futuro de la comunicación? ¡Vamos a ello! 🚀

Este proyecto consiste en un asistente de voz que responde llamadas telefónicas y proporciona respuestas mediante voz utilizando Twilio, OpenAI en tiempo real y Python. A continuación, se detalla el proceso de configuración, el código y cómo funciona el sistema.

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente:

1. **Cuenta de Twilio**: Regístrate en [Twilio](https://www.twilio.com/try-twilio) para obtener una cuenta gratuita.
2. **Número de Twilio con funciones de voz**: Compra un número de teléfono en Twilio con capacidades de voz. [Guía aquí](https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account#get-your-first-twilio-phone-number).
3. **Cuenta de OpenAI con acceso a Real Time**: Regístrate en [OpenAI](https://platform.openai.com/signup) y obtén una clave API.
4. **ngrok**: Para exponer tu servidor local a Internet durante las pruebas. Descárgalo [aquí](https://ngrok.com/download).
5. **Twilio dev-phone**: descarga este aplicativo de Twilio para llamar a tú número telefonico [twilio-devphone](https://www.twilio.com/docs/labs/dev-phone)

---

## Video guía

Mira este video para ver una demostración del asistente de voz en acción:
1. [Demostración del asistente](https://www.linkedin.com/feed/update/urn:li:activity:7297382594139115521/)
2. [Ver guía en YouTube](https://youtu.be/OVguB1h-eTs?si=jN7ceImqZuIS9cZI)



## Configuración del Proyecto

### 1. Instalación de Dependencias

Primero, crea un entorno virtual e instala las dependencias necesarias:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
pip install fastapi uvicorn twilio aiohttp python-dotenv
```

### 2. Configuración del Archivo .env
Crea un archivo .env en la raíz del proyecto y agrega las siguientes variables de entorno:

```.env
OPENAI_API_KEY=tu_clave_api_de_openai
PORT=5050
```

### 3. Código del Proyecto
El código principal del proyecto se divide en varias secciones, se crea un archivo main.py para esto:

**1. Importaciones y Configuración Inicial**


```python:
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

# Configuración
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Clave API de OpenAI
PORT = int(os.getenv('PORT', 5050))

```

**2. Mensaje del Sistema**
El asistente de voz utiliza un mensaje de sistema para definir su comportamiento. En este caso, actúa como un reclutador o un representante de ventas de la empresa "Agenx AI".

```python:
SYSTEM_MESSAGE = (
    "Eres un asistente de la empresa de 'Agenx AI', tú tarea será la de comunicarte con posibles clientes y ofrecerles el servicio de la Agenx AI. "
    "Actúa como un experto en tecnologías de Inteligencia Artificial y ofrece soluciones basadas en estas para la empresa a la que llames. "
    "Intenta agendar una reunión con el posible cliente para charlar sobre cómo podemos automatizar sus procesos con AI."
)
```

**3. Inicialización de FastAPI**
Se crea una instancia de FastAPI para manejar las solicitudes HTTP y WebSocket.


```python:
app = FastAPI()
if not OPENAI_API_KEY:
    raise ValueError('Missing the OpenAI API key. Please set it in the .env file.')
```

**4. Manejo de Llamadas Entrantes**
Cuando se recibe una llamada, se genera una respuesta TwiML que conecta la llamada a un flujo de medios (Media Stream).

```python:
@app.get("/", response_class=JSONResponse)
async def index_page():
    return {"message": "Twilio Media Stream Server is running!"}

@app.api_route("/incoming-call", methods=["GET", "POST"])
async def handle_incoming_call(request: Request):
    response = VoiceResponse()
    response.say("Please wait while we connect your call to the A. I. voice assistant, powered by Twilio and the Open-A.I. Realtime API")
    response.pause(length=1)
    response.say("O.K. you can start talking!")
    host = request.url.hostname
    connect = Connect()
    connect.stream(url=f'wss://{host}/media-stream')
    response.append(connect)
    return HTMLResponse(content=str(response), media_type="application/xml")
```

**5. Manejo del Flujo de Medios (Media Stream)**
El WebSocket /media-stream maneja la conexión entre Twilio y OpenAI. Recibe audio de Twilio, lo envía a OpenAI y devuelve la respuesta de OpenAI como audio. ¡¡Esta es la parte más importante del codigo¡¡


```python:
@app.websocket("/media-stream")
async def handle_media_stream(websocket: WebSocket):
    print("Client connected")
    await websocket.accept()

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
```


**Explicación detallada de /media-stream**
1. Definición del WebSocket (/media-stream)

```python:
@app.websocket("/media-stream")
async def handle_media_stream(websocket: WebSocket):
```

Este bloque define un endpoint WebSocket en la ruta /media-stream.

Cuando Twilio se conecta a este endpoint, se establece una conexión bidireccional en tiempo real para enviar y recibir datos.

2. Aceptar la conexión WebSocket

```python:
print("Client connected")
await websocket.accept()
```
Cuando un cliente (en este caso, Twilio) se conecta, se imprime un mensaje en la consola.

await websocket.accept() acepta la conexión WebSocket entrante.

3. Conexión con OpenAI
```python:
async with ClientSession() as session:
    async with session.ws_connect(
        'wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2024-10-01',
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "OpenAI-Beta": "realtime=v1"
        }
    ) as openai_ws:
```
Aquí se establece una conexión WebSocket con la API en tiempo real de OpenAI.

Se utiliza aiohttp.ClientSession para manejar la conexión.

La URL wss://api.openai.com/v1/realtime es el endpoint de OpenAI para la API en tiempo real.

Se envían las cabeceras necesarias, incluida la clave API de OpenAI (OPENAI_API_KEY).

4. Actualización de la sesión de OpenAI
```python:
await send_session_update(openai_ws)
```
Esta función envía una actualización de sesión a OpenAI para configurar el formato de audio, la voz y las instrucciones del asistente.

5. Manejo de datos desde Twilio (receive_from_twilio)

```python:
async def receive_from_twilio():
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
```
6. Manejo de datos hacia Twilio (send_to_twilio)
```python:
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
```
Esta función recibe respuestas de OpenAI y las envía de vuelta a Twilio.

Si el mensaje es de tipo response.audio.delta, se decodifica el audio y se envía a Twilio en formato JSON.

Si ocurre un error, se imprime en la consola.
Esta función recibe datos de Twilio a través del WebSocket.

Si el evento es media, se extrae el audio y se envía a OpenAI en formato JSON.

Si el evento es start, se guarda el streamSid (identificador único del flujo de medios).

Si el cliente se desconecta, se cierra la conexión con OpenAI.






**6. Actualización de la Sesión de OpenAI**
Se envía una actualización de sesión a OpenAI para configurar el formato de audio, la voz y las instrucciones del asistente.

```python:
async def send_session_update(openai_ws):
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
```

**7. Ejecución del Servidor**
Finalmente, el servidor se inicia utilizando Uvicorn.


```python:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
```

**8. Ejecución del Proyecto**
Inicia el servidor:

```bash
uvicorn main:app --host 0.0.0.0 --port 5050
```

**9. Expón el servidor local a Internet (opcional, usando ngrok):**
Después de haber descargado el ngrok y configurado tu cuenta, tienes que tener un archivo llamado ngrok.exe en tú proyecto para poder ejecutar los comandos del ngrok, abre una terminal nueva y pon el siguiente comando:

```bash
.\ngrok http 5050
```

luego de correr el comando debes copiar el dominio que proporciona ngrok para tú aplicativo, por ejemplo:
https://80eba09efc78.ngrok.app

Ahora entra a tú cuenta de Twilio y en las configuraciones del número que compraste (Recuerda que debes comprar un número con capacidades de voz), le agregas en dominio proporcionado por ngrok con el endpoint de [/incoming-call] en el apartado de [A call comes in] selecciona la opción "Webhook" y en el apartado [URL] pon tú dominio con el endpoint:
https://<tu_dominio>/incoming-call.

por ejemplo:
https://80eba09efc78.ngrok.app/incoming-call

Ahora guarda los cambios.

**10. Llamar al número de twilio**
Luego de esto abre otra terminal y corre el siguiente comando (recuerda que tienes que descargar el aplicativo de Twilio-devphone para realizar la llamada a tú número, o lo puedes hacer desde tú dispositivo movil.

```bash
twilio-devphone
```

Se te desplega un aplicativo el cual te permite hacer llamadas, copia el número que compraste en twilio y realiza la llamada para vivir la experiencia!!!

