# backend_community_homework

# Yatube

## Yatube - это социальная сеть для обмена записями пользователей. В данном проекте реализованы возможности регистрации пользователей, публикации постов.

# Установка
1. Склонируйте репозиторий:

``` git clone https://github.com/freddy7753/hw02_community.git ```

2. Установите зависимости:

``` python3 -m venv env && source env/bin/activate && pip install -r requirements.txt ```

3. Создайте базу данных и выполните миграции:

``` python manage.py migrate ```

4. Создайте суперпользователя:

``` python manage.py createsuperuser ```

5. Запустите сервер:

``` python manage.py runserver ```

# Использование

>- Регистрация и аутентификация
Для того чтобы зарегистрироваться, необходимо перейти по ссылке "Регистрация" на главной странице сайта и заполнить форму регистрации.

>- Для того чтобы войти в свой аккаунт, необходимо перейти по ссылке "Вход" на главной странице сайта и заполнить форму аутентификации.

>- Публикация и удаление постов
Чтобы опубликовать новый пост, необходимо нажать на кнопку "Новый запись" на главной странице сайта и заполнить форму создания нового поста.
