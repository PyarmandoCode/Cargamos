#Instalar la Libreria
#https://pypi.org/project/gTTS/

#Del modulo princial utilizar la funcion gTTS
from gtts import gTTS
import os
#El texto que voy a reproducir a audio
mytexto="Python es Muy Amigable"
#Cambiando el Lenguaje a español
lenguage="es"
convertir=gTTS(text=mytexto,lang=lenguage,slow=False)
#Salvar la conversion del texto a un audio
convertir.save("cargamos.mp3")
os.system("start cargamos.mp3")




