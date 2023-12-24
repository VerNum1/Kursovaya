#!/bin/bash

# Путь к upload_to_drive.py
UPLOAD_SCRIPT_PATH="C:\Users\vadim\Desktop\backup\upload_to_drive.py"

# Путь к backup.py
BACKUP_SCRIPT_PATH="C:\Users\vadim\Desktopbackup\backup.py"

# Функция для выполнения бекапа и загрузки на Яндекс.Диск
perform_backup_and_upload() {
    # Выполняем скрипт для создания бекапа
    python3 "$BACKUP_SCRIPT_PATH"
    
    # Ждем некоторое время для завершения создания бекапа
    sleep 10
    
    # Выполняем скрипт для загрузки бекапа на Яндекс.Диск
    python3 "$UPLOAD_SCRIPT_PATH"
}

# Бесконечный цикл с интервалом в 30 минут (1800 секунд)
while true
do
    perform_backup_and_upload
    sleep 1800
done