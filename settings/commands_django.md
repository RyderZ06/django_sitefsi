# **Основные команды DJANGO**

## Создание проектов и приложений
| Команда |	Описание |
|---------|----------|
|`django-admin startproject <project>`|	Создать новый проект Django|
|`python manage.py startapp <appname> `| Создать новое приложение внутри проекта|

## Работа с сервером разработки
| Команда |	Описание |
|---------|----------|
|`python manage.py runserver `| Запуск локального сервера для разработки|

## Миграции базы данных
| Команда |	Описание |
|---------|----------|
|`python manage.py makemigrations `| Создание миграций для всех приложений
|`python manage.py makemigrations <appname> `| Создание миграций для конкретного приложения|
|`python manage.py makemigrations --empty <appname> `| Создание пустой миграции для приложения (например, для кастомных изменений)|
|`python manage.py migrate`| Применение миграций, обновление схемы базы данных|
|`python manage.py showmigrations `| Просмотр списка миграций и их статуса|

## Работа с пользователями
| Команда |	Описание |
|---------|----------|
|`python manage.py createsuperuser `| Создание суперпользователя с правами администратора|
|`python manage.py changepassword <username> `| Смена пароля пользователя через консоль|

## Работа со статическими файлами
| Команда |	Описание |
|---------|----------|
|`python manage.py collectstatic `| Сбор статических файлов из приложений в одну папку (для деплоя)|

## Работа с данными и тестами
| Команда |	Описание |
|---------|----------|
|`python manage.py shell `| Запуск интерактивной оболочки Python с доступом к проекту Django|
|`python manage.py test `| Запуск тестов проекта|
|`python manage.py dumpdata `| Экспорт данных базы в формате JSON или YAML|
|`python manage.py loaddata <fixture> `| Импорт данных из файла фикстуры|
|`python manage.py sqlflush `| Генерация SQL для очистки базы данных|

## Диагностика и утилиты
| Команда |	Описание |
|---------|----------|
|`python manage.py check `| Проверка проекта на ошибки и предупреждения|
|`python manage.py diffsettings `| Показать отличия текущих настроек от стандартных|
|`python manage.py inspectdb `| Автоматическая генерация моделей из существующей базы данных|
|`python manage.py sendtestemail `| Тестирование отправки email|
## Управление зависимостями (непосредственно pip)
| Команда |	Описание |
|---------|----------|
|`pip install -r requirements.txt `| Установка зависимостей из файла requirements.txt|
|`pip freeze > requirements.txt `| Сохранение текущих зависимостей в файл|

### Быстрый набор команд с django-command (альтернатива)
Для удобства можно использовать инструмент `django-command`, который объединяет часто используемые команды в одну:

`bash`
`django-command make_migrations migrate update_local`  
Где команды соответствуют:  
- `make_migrations` — python manage.py makemigrations  
- `migrate` — python manage.py migrate
- `update_local` — обновление локалей (интернационализации)