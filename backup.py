import yadisk
import os
from datetime import datetime

y = yadisk.YaDisk(token="y0_AgAAAABfpo5pAAsJ8QAAAAD1zmkh9I1DQVIDRK-qXQKLBFhIBxndd74")

def run(path):
    date = datetime.strftime(datetime.now(), "%d.%m.%Y-%H.%M.%S")
    y.mkdir(f'/backup/{date}')

    for address, dirs, files in os.walk(path):
        for dir in dirs:
            y.mkdir(f'/backup/{date}/{dir}')
            #print(f'Папка {dir} создана')
        for file in files:
            #print(f'Файл {file} загружен')
            y.upload(f'{address}/{file}', f'/backup/{date}/{file}')


if __name__ == '__main__':
    run(r'backup')
