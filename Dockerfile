# Используем официальный образ Python
FROM python:3.8-slim

MAINTAINER "Dmitry <7292337@gmail.com>"
LABEL version="1.0"
LABEL description="Images pre-process Function"

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы со скриптом и зависимостями
COPY requirements.txt .
COPY script.py .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем скрипт
ENTRYPOINT ["python", "script.py"]
