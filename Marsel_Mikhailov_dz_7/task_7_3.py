'''Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
например, во фреймворке django'''


import os
import shutil
from pathlib import Path


def diff_my_project():
    os.chdir('my_project/authapp')
    os.makedirs('templates/authapp', exist_ok=True)
    os.chdir('templates/authapp')
    with open("base.html", "w", encoding='utf-8') as fw:
        fw.write('Произвольный текс в файле "base.html"')
    with open("index.html", "w", encoding='utf-8') as fw:
        fw.write('Произвольный текс в файле "index.html"')

    '''остальные директории и файлы я создал руками через PyCharm'''

    os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    '''перехожу в директорию my_project, тут буду работать'''

    paths = sorted(Path('.').rglob('*/templates'))
    '''найдено 2 пути с данным именем папки'''
    list_dir = list(map(str, paths)) # перевожу путь к данным в строковый тип
    '''использую индексы для того чтобы вызвать пути к найденным папкам'''
    shutil.copytree(list_dir[0], 'templates', dirs_exist_ok=True)
    shutil.copytree(list_dir[1], 'templates', dirs_exist_ok=True)


diff_my_project()