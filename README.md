# Проект Yatube(api)

## Описание

Api для портала блоггеров Yatube 

## Установка

Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/yandex-praktikum/kittygram.git
cd kittygram

Cоздать и активировать виртуальное окружение:
python3 -m venv env
source env/bin/activate

Установить зависимости из файла requirements.txt:
python3 -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:
python3 manage.py migrate

Запустить проект:
python3 manage.py runserver

## Примеры запросов

Получить список всех постов
/api/v1/posts/

Получить пост по id
/api/v1/posts/{id}/