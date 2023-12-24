import subprocess
import os

# Команда для выполнения
cmd = 'python manage.py dumpdata > backup/dump.json'

# Запускаем команду
subprocess.run(cmd, shell=True)