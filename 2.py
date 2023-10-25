import os
from PIL import Image
import pywhatkit as kt
import shutil

def convert_images_to_ascii(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                input_image_path = os.path.join(root, file)
                output_text_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.txt")

                try:
                    img = Image.open(input_image_path)
                    img = img.convert("RGB")
                    ascii_art = kt.image_to_ascii_art(input_image_path)

                    # Получаем размеры терминала
                    terminal_width, _ = shutil.get_terminal_size()
                    
                    # Увеличиваем количество пробелов для смещения вправо
                    padding_width = (terminal_width - len(ascii_art.split('\n')[0])) // 2 + 10

                    # Создаем отступ для смещения вправо
                    padding = ' ' * padding_width
                    right_aligned_ascii_art = '\n'.join([padding + line for line in ascii_art.split('\n')])

                    # Сохраняем ASCII-графику в текстовом файле
                    with open(output_text_path, "w") as text_file:
                        text_file.write(right_aligned_ascii_art)

                    print(f"Конвертировано: {input_image_path}")
                except Exception as e:
                    print(f"Ошибка при конвертации: {str(e)}")

if __name__ == "__main__":
    input_folder = "./images/"  # Путь к папке с фотографиями
    output_folder = "./test2/"  # Путь к папке, в которую будут сохранены ASCII-изображения
    convert_images_to_ascii(input_folder, output_folder)
