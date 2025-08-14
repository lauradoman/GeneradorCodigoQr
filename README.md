# 🎯 Mini QR Generator con Logo Opcional y Colores Personalizados

Generador de códigos QR en **PNG** y **SVG**, con opción de incluir un **logo centrado**, un **recuadro difuminado** y **colores personalizados**.  
Ideal para crear QR atractivos para branding, marketing y eventos.


## 📌 Características

✅ Genera **PNG** con efectos y **SVG vectorial** limpio.  
✅ Colores personalizados para el QR y el fondo (en formato HEX).  
✅ Logo opcional en el centro con recuadro difuminado.  
✅ Tamaño de imagen configurable (por defecto 1000×1000 px).  
✅ Alta corrección de errores (**H**) para asegurar la lectura incluso con logos grandes.  
✅ Fácil de usar desde la consola.
✅ Basado en la librería [qrcode](https://pypi.org/project/qrcode/) y [Pillow](https://pypi.org/project/Pillow/).



## 📦 Requisitos

Instala las dependencias necesarias con:

```bash
pip install qrcode[pil] pillow
````

---

## 🚀 Uso

Ejecuta el script en tu consola:

```bash
python generar_qr.py
```

El programa te pedirá:

1. **Texto o URL** para el QR.
2. **Archivo PNG del logo** (puedes dejarlo vacío para omitirlo).
3. **Nombre base del archivo** (sin extensión).
4. **Color del QR** (ej. `#000000` para negro, ENTER para negro por defecto).
5. **Color de fondo** (ej. `#ffffff` para blanco, ENTER para blanco por defecto).

---

## 📂 Ejemplo de uso

**Entrada:**

```
Ingresa la URL o texto para el QR: https://miweb.com
Ingresa el nombre del archivo de logo (PNG) o ENTER para omitir: logo.png
Ingresa el nombre base del archivo (sin extensión, ENTER para 'qr_personalizado'): mi_qr
Color del QR (ej. #000000 para negro, ENTER para negro): #ff0066
Color de fondo (ej. #ffffff para blanco, ENTER para blanco): #ffffff
```

**Salida:**

```
✅ PNG generado: mi_qr.png
✅ SVG generado: mi_qr.svg
🎉 ¡Listo! Revisa los archivos generados en la carpeta del programa.
```

---

## 📷 Ejemplo visual

| QR con logo                          | QR sin logo                          |
| ------------------------------------ | ------------------------------------ |
| ![QR con logo](qr_con_logo.png) | ![QR sin logo](qr_sin_logo.png) |

---

## ⚙️ Configuración avanzada

Si quieres modificar el tamaño del QR o el tamaño del recuadro, edita estas variables dentro del código:

```python
qr_size=1000         # Tamaño total del QR en píxeles
recuadro_ratio=0.2   # Proporción del recuadro con respecto al QR
```


## 📜 Licencia

Este proyecto está licenciado **solo para uso personal y con fines educativos**.  
No está permitido su uso con fines comerciales sin autorización previa del autor.
