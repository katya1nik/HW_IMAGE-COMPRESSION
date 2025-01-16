import os
from typing import Union
from PIL import Image
from pillow_heif import register_heif_opener
from plyer import notification

class Notification: # Класс для уведомлений
    @staticmethod
    def print_message(prefix: str, message: str) -> None:
        notification.notify(
            title=prefix,
            message=message,
            app_name="Image Compressor",
            timeout=10  
        )

    @staticmethod
    def info(message: str) -> None:
        Notification.print_message("Информация", message)
    
    @staticmethod
    def success(message: str) -> None:
        Notification.print_message("Успешно", message)
    
    @staticmethod
    def error(message: str) -> None:
        Notification.print_message("Ошибка", message)


QUALITY: int = 50  # Можно настроить качество сжатия

# def compress_image(input_path: str, output_path: str) -> None:
#     """
#     Сжимает изображение и сохраняет его в формате HEIF.

#     Args:
#         input_path (str): Путь к исходному изображению.
#         output_path (str): Путь для сохранения сжатого изображения.

#     Returns:
#         None
#     """
#     with Image.open(input_path) as img:
#         img.save(output_path, "HEIF", quality=QUALITY)
#     print(f"Сжато: {input_path} -> {output_path}")


# def process_directory(directory: str) -> None:
#     """
#     Обрабатывает все изображения в указанной директории и её поддиректориях.

#     Args:
#         directory (str): Путь к директории для обработки.

#     Returns:
#         None
#     """
#     for root, _, files in os.walk(directory):
#         for file in files:
#             # Проверяем расширение файла
#             if file.lower().endswith(('.jpg', '.jpeg', '.png')):
#                 input_path = os.path.join(root, file)
#                 output_path = os.path.splitext(input_path)[0] + '.heic'
#                 compress_image(input_path, output_path)

# def main(input_path: str) -> None:
#     """
#     Основная функция программы. Обрабатывает входной путь и запускает сжатие изображений.

#     Args:
#         input_path (str): Путь к файлу или директории для обработки.

#     Returns:
#         None
#     """
#     register_heif_opener()
#     input_path = input_path.strip('"')  # Удаляем кавычки, если они есть
    
#     if os.path.exists(input_path):
#         if os.path.isfile(input_path):
#             # Если указан путь к файлу, обрабатываем только этот файл
#             print(f"Обрабатываем файл: {input_path}")
#             output_path = os.path.splitext(input_path)[0] + '.heic'
#             compress_image(input_path, output_path)
#         elif os.path.isdir(input_path):
#             # Если указан путь к директории, обрабатываем все файлы в ней
#             print(f"Обрабатываем директорию: {input_path}")
#             process_directory(input_path)
#             # Функция process_directory рекурсивно обойдет все поддиректории
#             # и обработает все поддерживаемые изображения
#     else:
#         print("Указанный путь не существует")

# if __name__ == "__main__":
#     user_input: str = input("Введите путь к файлу или директории: ")
#     main(user_input)

"""
1. **ImageCompressor**
   - Атрибуты:
     - `__quality`: Приватный атрибут для хранения качества сжатия (тип: `int`).
     - `supported_formats`: Атрибут класса, содержащий кортеж поддерживаемых форматов файлов (например, `('.jpg', '.jpeg', '.png')`).
   - Методы:
     - `__init__(self, quality: int)`: Конструктор класса, который принимает значение качества сжатия и инициализирует атрибут `__quality`.
     - `compress_image(self, input_path: str, output_path: str) -> None`: Метод для сжатия изображения и сохранения его в формате HEIF.
     - `process_directory(self, directory: str) -> None`: Метод для обработки всех изображений в указанной директории и её поддиректориях.
     - `quality(self) -> int`: Геттер для получения значения качества сжатия.  `@property`
     - `quality(self, quality: int) -> None`: Сеттер для установки значения качества сжатия. `@quality.setter`
"""

class ImageCompressor:
    def __init__(self, quality: int) -> None:
        self. __quality = quality
        self. __supported_formats = (".jpg", ".jpeg", ".png")

    @property
    def quality(self) -> int:
        """Получает значение качества сжатия."""
        return self. __quality
    
    @quality.setter
    def quality(self, quality: int) -> None:
        """Устанавливает значение качества сжатия."""
        if not isinstance(quality, int):
            raise TypeError("Качество сжатия должно быть целым числом.")
        if quality < 1 or quality > 100:
            raise ValueError("Качество сжатия должно быть в диапазоне от 1 до 100.")
        self. __quality = quality

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение и сохраняет его в формате HEIF.

        Args:
        input_path (str): Путь к исходному изображению.
        output_path (str): Путь для сохранения сжатого изображения.

        Returns:
        None
        """
        try:
            with Image.open(input_path) as img:
                img.save(output_path, "HEIF", quality=self.__quality)
            Notification.success(f"Файл {input_path} сжат")
        except FileNotFoundError:
            Notification.error("Файл не найден")
        except Exception as e:
            Notification.error(f"Ошибка при сжатии {input_path}: {str(e)}")
        

    def process_directory(self, directory: str) -> None:
        """
        Обрабатывает все изображения в указанной директории и её поддиректориях.

        Args:
            directory (str): Путь к директории для обработки.

        Returns:
            None
    """
        for root, _, files in os.walk(directory):
            for file in files:
                # Проверяем расширение файла
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)

    def __call__(self, input_path: str) -> None:
        """
        Основной метод программы. Обрабатывает входной путь и запускает сжатие изображений.
        """
        register_heif_opener()
        input_path = input_path.strip('"')  # Удаляем кавычки, если они есть
        
        if os.path.exists(input_path):
            if os.path.isfile(input_path):
                # Если указан путь к файлу, обрабатываем только этот файл
                # Notification.info(f"Обрабатываем файл: {input_path}")
                output_path = os.path.splitext(input_path)[0] + '.heic'
                self.compress_image(input_path, output_path)
            elif os.path.isdir(input_path):
                # Если указан путь к директории, обрабатываем все файлы в ней
                # Notification.info(f"Обрабатываем директорию: {input_path}")
                self.process_directory(input_path)
                # Функция process_directory рекурсивно обойдет все поддиректории
                # и обработает все поддерживаемые изображения
        else:
            Notification.error("Указанный путь не существует")

if __name__ == "__main__":
    user_input: str = input("Введите путь к файлу или директории: ")
    compressor = ImageCompressor(QUALITY)
    compressor(user_input)

