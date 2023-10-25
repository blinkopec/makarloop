from PIL import Image
import os

def rotate_and_save_to_ascii(image_path, output_folder, rotation_degrees):
    try:
        # Открываем изображение
        img = Image.open(image_path)
        
        for degree in rotation_degrees:
            # Создаем новую копию изображения для каждого угла поворота
            rotated_img = img.rotate(degree)
            
            # Конвертируем изображение в ASCII-графику
            ascii_img = image_to_ascii(rotated_img)
            
            # Генерируем имя файла на основе угла поворота
            output_path = os.path.join(output_folder, f"output_{degree}deg.txt")
            
            # Сохраняем ASCII-графику в текстовом файле
            with open(output_path, "w") as text_file:
                text_file.write(ascii_img)
            
            print(f"ASCII-изображение сохранено в текстовый файл: {output_path}")
    except Exception as e:
        print(f"Ошибка: {str(e)}")

def image_to_ascii(img):
    ascii_chars = "@%#*+=-:. "  # Символы, используемые для создания ASCII-изображения
    ascii_img = ""

    for y in range(img.height):
        for x in range(img.width):
            pixel_value = img.getpixel((x, y))
            ascii_img += ascii_chars[pixel_value // 25]

        ascii_img += "\n"

    return ascii_img

if __name__ == "__main__":
    input_image_path = "makar.jpg"  # Замените на путь к вашему изображению
    output_folder = "./test"  # Папка для сохранения ASCII-изображений
    rotation_degrees = [90, 180, 270]  # Углы поворота (в градусах)

    # Создаем папку для сохранения ASCII-изображений, если она не существует
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    rotate_and_save_to_ascii(input_image_path, output_folder, rotation_degrees)
