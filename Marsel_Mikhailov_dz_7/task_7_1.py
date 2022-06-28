'''Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?'''


import os


def new_path(dirs):
    os.makedirs('my_project', exist_ok=True)
    os.chdir('my_project')
    for _ in dirs:
        os.makedirs(_, exist_ok=True)
    print('Шаблонные папки созданы и готовы к работе')


new_dirs_in_my_project = ('settings', 'mainapp', 'adminapp', 'authapp')
new_path(new_dirs_in_my_project)