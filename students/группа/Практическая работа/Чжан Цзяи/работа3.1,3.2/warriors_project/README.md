## Инструкция о проекте
**Это приложение войны**
***
Его структура
```
│  db.sqlite3
│  list.txt
│  manage.py
│  README.md
│  
├─warriors
│  │  mkdocs.yml
│  │  
│  └─docs
│          index.md
│          
├─warriors_app
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  serializers.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          0001_initial.cpython-38.pyc
│  │          __init__.cpython-38.pyc
│  │          
│  └─__pycache__
│          admin.cpython-38.pyc
│          apps.cpython-38.pyc
│          models.cpython-38.pyc
│          serializers.cpython-38.pyc
│          urls.cpython-38.pyc
│          views.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
└─warriors_project
    │  asgi.py
    │  settings.py
    │  urls.py
    │  wsgi.py
    │  __init__.py
```
**Модель.py**
***
Warrior-Это описание война
***
Profession-Это описание профессии
***
Skill-Это описание умений
***
SkillOfWarrior-Это описание умений война
### Start the server
```
$ python manage.py runserver
```
### Функции сайта
***
Вывод полной информации о всех войнах и их профессиях (в одном запросе).
***
Вывод полной информации о всех войнах и их скилах (в одном запросе).
***
Вывод полной информации о войне (по id), его профессиях и скилах.
***
Удаление война по id.
***
Редактирование информации о войне.
