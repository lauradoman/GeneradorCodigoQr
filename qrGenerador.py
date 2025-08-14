import qrcode
from PIL import Image, ImageDraw, ImageFilter
from qrcode.image.svg import SvgImage


def generar_qr(data, logo_path, file_name, fill_color="#000000", back_color="#ffffff", qr_size=1000, recuadro_ratio=0.2):
    # --------------------
    # Crear QR
    # --------------------
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generar QR inicial y redimensionar
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")
    qr_img = qr_img.resize((qr_size, qr_size), Image.LANCZOS)

    # --------------------
    # Si hay logo, crear recuadro y pegarlo
    # --------------------
    if logo_path:
        recuadro_size = int(qr_size * recuadro_ratio)
        corner_radius = recuadro_size // 6
        blur_radius = recuadro_size // 20

        mask = Image.new("L", (qr_size, qr_size), 0)
        draw = ImageDraw.Draw(mask)

        x0 = (qr_size - recuadro_size) // 2
        y0 = (qr_size - recuadro_size) // 2
        x1 = x0 + recuadro_size
        y1 = y0 + recuadro_size

        draw.rounded_rectangle([x0, y0, x1, y1], radius=corner_radius, fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

        # Recuadro del mismo color que el fondo
        recuadro = Image.new("RGB", (qr_size, qr_size), back_color)
        qr_img.paste(recuadro, (0, 0), mask=mask)

        # Pegar logo
        logo = Image.open(logo_path).convert("RGBA")
        logo_max_size = int(recuadro_size * 0.8)
        logo.thumbnail((logo_max_size, logo_max_size), Image.LANCZOS)

        logo_x = (qr_size - logo.size[0]) // 2
        logo_y = (qr_size - logo.size[1]) // 2
        qr_img.paste(logo, (logo_x, logo_y), mask=logo)

    # --------------------
    # Guardar PNG con efectos
    # --------------------
    png_filename = f"{file_name}.png"
    qr_img.save(png_filename)
    print(f"✅ PNG generado: {png_filename}")

    # Generar SVG puro (sin logo ni recuadro)
    svg_filename = f"{file_name}.svg"
    with open(svg_filename, "w") as f:
        qr.make_image(image_factory=SvgImage).save(f)
    print(f"✅ SVG generado: {svg_filename}")


if __name__ == "__main__":
    print("==== Mini QR Generator ====")
    url = input("Ingresa la URL o texto para el QR: ")
    logo_file = input("Ingresa el nombre del archivo de logo (PNG) o ENTER para omitir: ").strip()
    nombre_archivo = input("Ingresa el nombre base del archivo (sin extensión, ENTER para 'qr_personalizado'): ").strip() or "qr_personalizado"
    
    color_qr = input("Color del QR (ej. #000000 para negro, ENTER para negro): ").strip() or "#000000"
    color_fondo = input("Color de fondo (ej. #ffffff para blanco, ENTER para blanco): ").strip() or "#ffffff"

    generar_qr(url, logo_file if logo_file else None, nombre_archivo, fill_color=color_qr, back_color=color_fondo)
    print("🎉 ¡Listo! Revisa los archivos generados en la carpeta del programa.")
