# Проект: запуск docker-compose

Данный проект собирает отзывы пользователей на произведения, но в нём нет самих файлов произведений.

Права администратора:
 - Добавлять произведения, жанр, категорию.
Права аутентифицированного пользователя:
 - К произведениям могут оставлять тестовые отзывы;
 - Ставить произведению оценку в диапозоне от 1 до 10. Далее на основе оценок
 формируется рейтинг произвдений. Важно: На одно произвдение может быть только
 один отзыв.;
 - Оставлять комментарии к отзывам;

### Ресурсы API YaMDb

AUTH: аутентификация.

USERS: пользователи.

TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

CATEGORIES: категории (типы) произведений ("Фильмы", "Книги", "Музыка").

GENRES: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.

REVIEWS: отзывы на произведения. Отзыв привязан к определённому произведению.

COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.

Примеры некоторых запросов API

Регистрация пользователя:
POST /api/v1/auth/signup/

Получение данных своей учетной записи:
GET /api/v1/users/me/

Добавление новой категории:
POST /api/v1/categories/

Удаление жанра:
DELETE /api/v1/genres/{slug}

Частичное обновление информации о произведении:
PATCH /api/v1/titles/{titles_id}

Получение списка всех отзывов:
GET /api/v1/titles/{title_id}/reviews/

Добавление комментария к отзыву:
POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/

### Технологии проекта
Python 3.7.9
Django 3.2
Django Rest framework 3.12.4
PostgreSQL


### Запуск проекта в Dev-режиме (код для Windows)
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Markporsh/api_yamdb
cd api_yamdb
```

- Установить и активировать виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
- Установить зависимости из файла **requirements.txt**
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Выполнить миграции
```
python manage.py migrate
```
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```

- Установить Docker
- Из дирректории \infra_sp2\infra выполнить:
```
docker-compose up -d --build
```
- Выполните по очереди команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
- Теперь проект доступен по адресу http://localhost/
- Для безопасности изменить настройки setting.py DATABASE
- Именно создать файл .env в директории \infra_sp2\infra
- и поместить в него переменные с значением по умолчанию

### Автор
    _Уланов Павел_
