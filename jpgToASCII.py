from PIL import Image
import shutil

def image_to_ascii(image_path, output_width=None):
    try:
        img = Image.open(image_path)
        img = img.convert("L")  # Преобразование в черно-белое изображение
        aspect_ratio = img.height / img.width

        if output_width is None:
            terminal_width = shutil.get_terminal_size().columns
            output_width = int(terminal_width * 1.5)

        output_height = int(output_width * aspect_ratio)
        img = img.resize((output_width, output_height))
        ascii_chars = "@%#*+=-:. "  # Символы, используемые для создания ASCII-изображения
        ascii_img = ""

        for y in range(output_height):
            for x in range(output_width):
                pixel_value = img.getpixel((x, y))
                ascii_img += ascii_chars[pixel_value // 25]

            ascii_img += "\n"

        return ascii_img
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    image_path = "./makar.jpg"  # Замените на путь к вашему изображению
    ascii_text = image_to_ascii(image_path)
    print(ascii_text)
