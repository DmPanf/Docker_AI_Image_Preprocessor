from PIL import Image                           # Обработка изображений
import numpy as np                              # Работа с массивами
import argparse                                 # Модуль для извлечения аргументов, передаваемых скрипту через командную строку


def prepare_image(path):
    img = Image.open(path)                                    # Загружаем картинку по переданному пути
    print(f'Размер исходных данных: {np.array(img).shape}')   # Выводим информацию о размере исходного изображения

    img = img.resize((32, 32)).convert('L')                   # Приводим изображения к фиксированному размеру и переводим в оттенки серого
    img = np.array(img)                                       # Преобразуем изображение в numpy-массив
    img = img.reshape(1, -1)                                  # Вытягиваем в вектор
    img = img.astype('float32') / 255.                        # Нормализуем данные
    print(f'Размер данных после преобразования: {img.shape}') # Выводим информацию о новом размере данных

    with open('prepared_image.npy', 'wb') as f:               # Создаем новый файл для записи данных
        np.save(f, img)                                       # Записываем в файл обработанный numpy-массив

    print('Изображение обработано!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Обработка изображения')
    parser.add_argument('path', type=str, help='Путь к изображению')
    args = parser.parse_args()

    prepare_image(args.path)
