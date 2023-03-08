import openai
import speech_recognition as sr
import pyttsx3
import sys
openai.api_key = "API KEY"
# Iniciar el reconocimiento de voz 
r = sr.Recognizer()
engine = pyttsx3.init()
# Función para la entrada de voz 
def get_audio()
:
 
# Contador de intentos fallidos
 
attempts = 0
 
while True:
 
with sr.Microphone() as source:
 
print("Escuchando.
.
.")
 
audio = r.listen(source)
 
try:
 
text = r.recognize_google(audio, language='es-ES'
)
 
print(f"Usuario: {text}")
 
return text
 
except:
 
attempts += 1
 
if attempts >= 3:
 
print("Ha superado el límite de intentos. Ingresa 
tu pregunta manualmente.")
 
break
 
else:
 
print("No se ha podido reconocer la voz. Intenta de 
nuevo.")
 
# En caso no se reconozca la voz por 3 intentos se tendra que hacer 
de manera manual
 
while True:
 
text = input("Ingresa tu pregunta: ")
 
if text:
 
return text
# Función para la salida de audio de las respuestas
def speak(text)
:
 
engine.say(text)
 
engine.runAndWait()
# Contador de intentos fallidos
attempts = 0
while True:
 
if attempts >= 3:
 
speak("Ingresa tu pregunta manualmente.")
 
user_input = input("Ingresa tu pregunta: ")
 
attempts = 0
 
else:
 
user_input = get_audio()
#Al decir culminar proyecto se cierra las peticiones y cierra el 
programa
 
if user_input:
 
if user_input == "culminar proyecto":
 
speak("Cerrando el programa.
.
.")
 
sys.exit()
 
else:
 
# Para hacer las preguntas a la API
 
completion = openai.Completion.create(engine="text-davinci-
003",
 
prompt=user_input,
 
max_tokens=2048)
 
response = completion.choices[0]
.text
 
print(f"Chatbot: {response}")
 
speak(response)
 
else:
 
attempts += 1
