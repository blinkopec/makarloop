import os
import time

def display_text_from_folder(folder_path):
    while True:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(".txt"):
                    text_filename = os.path.join(root, file)
                    with open(text_filename, "r") as text_file:
                        text = text_file.read()
                        print(f"Содержимое файла {text_filename}:\n{text}")
                    time.sleep(0.2) 

if __name__ == "__main__":
    folder_path = "./test2/"  # Замените на путь к папке, в которой хранятся текстовые файлы
    display_text_from_folder(folder_path)
    