#!/bin/bash

# Сборка образа
docker build -t image-preprocessor .

# Запуск контейнера с передачей пути к изображению
docker run -v /home/bunta/ARCHIVE/Docker.Files.2023/Image.Process:/app/images image-preprocessor images/image.jpg
