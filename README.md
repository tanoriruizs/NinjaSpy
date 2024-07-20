# NinjaSpy - Keylogger

NinjaSpy es un keylogger básico creado en Python para una presentación sobre ciberseguridad en la universidad. Este proyecto tiene como objetivo educativo demostrar cómo funcionan los keyloggers y cómo pueden ser utilizados para atacar equipos, así como las maneras de prevenir dichos ataques.

## Características

- Captura todas las pulsaciones de teclado.
- Guarda las pulsaciones en un archivo de texto.
- Envía el archivo de registro por correo electrónico a intervalos regulares.
- Fácil de entender y modificar para propósitos educativos.

## Requisitos

- Python 3.x
- Bibliotecas adicionales: `pynput`, `smtplib`, `email`

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tuusuario/NinjaSpy.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd NinjaSpy
    ```
3. Instala las dependencias:
    ```bash
    pip install pynput
    ```

## Configuración

1. **Generar un código de aplicación en Google:**
   - Para enviar correos a través de Gmail, necesitas generar un código de aplicación. Esto es necesario porque Google requiere un método de autenticación seguro para aplicaciones menos seguras. Puedes seguir [esta guía](https://support.google.com/accounts/answer/185833) para crear un código de aplicación.
   
2. **Actualizar el archivo `ninjaspy.py`:**
   - Abre el archivo `ninjaspy.py` en un editor de texto.
   - Cambia las siguientes constantes a tus valores específicos:
     ```python
     FROM_EMAIL = "tucorreo@gmail.com"  # Cambia esto a tu correo electrónico
     TO_EMAIL = "destinatario@yopmail.com"  # Cambia esto al correo de destino
     APP_CODE = "tu_codigo_de_aplicacion"  # Cambia esto al código de aplicación generado en Google
     ```

## Uso

1. Ejecuta el keylogger:
    ```bash
    python ninjaspy.py
    ```
2. Para detener el keylogger, simplemente cierra la ventana del terminal o utiliza una combinación de teclas para finalizar el proceso.

## Prevención contra Keyloggers

Aquí hay algunas recomendaciones para proteger tu equipo contra keyloggers:

1. **Mantén tu software actualizado:** Asegúrate de que tu sistema operativo y todos los programas estén siempre actualizados.
2. **Utiliza un antivirus confiable:** Instala y mantén actualizado un buen software antivirus que pueda detectar y eliminar keyloggers.
3. **Ten cuidado con los correos electrónicos y descargas:** No abras archivos adjuntos ni hagas clic en enlaces de correos electrónicos sospechosos, y descarga software solo de fuentes confiables.
4. **Usa autenticación multifactor:** Esto añade una capa adicional de seguridad más allá de solo las contraseñas.
5. **Monitorea el uso del teclado:** Algunas soluciones de seguridad pueden detectar comportamientos anómalos en el uso del teclado.

## Disclaimer

Este proyecto es únicamente con fines educativos. **No me hago responsable del uso indebido de este software.** NinjaSpy está diseñado para ayudar a entender el funcionamiento básico de un keylogger y fomentar la ciberseguridad. No utilices esta herramienta con fines no éticos o ilegales.
