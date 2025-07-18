# **WEB-SITE FLIGHT SAFETY INSPECTION**

## Используемые технологии

![Version](https://img.shields.io/badge/project%20ver-0.1-brightgreen)  
![Django](https://img.shields.io/badge/django-5.2.3-green?logo=django&logoColor=white)  
![Python](https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=white)  
![pandas](https://img.shields.io/badge/pandas-data%20analysis-blue?logo=pandas&logoColor=white)  
![openpyxl](https://img.shields.io/badge/openpyxl-Excel%20import%2Fexport-007ACC?logo=python&logoColor=white)  
![Jupyter](https://img.shields.io/badge/Jupyter%20Lab-IDE%20&%20Data%20Analysis-orange?logo=jupyter&logoColor=white)  
![Run Server](https://img.shields.io/badge/runserver-manage.py%20runserver-brightgreen)

## Описание
Веб-приложение `inspection` написано для эффективного управления данными инспекционных проверок. Обеспечивает ввод, хранение и просмотр проверок и несоответствий, а также доступ к контактам инспекторов и структуре службы. Включает просмотр нормативных документов `Инспекции по Безопасности полётов`. Данные хранятся в реляционной базе, обеспечивая надёжность и доступность через веб-браузер.

## Структура проекта
| Технология                | Бейджи / Название папки / описание |
|--------------------------|-------------------------------------|
| **`Django`** | ![Django](https://img.shields.io/badge/inspection-основной%20модуль%20проекта-brightgreen?logo=django&logoColor=white) |
| **`Python`** | ![Python](https://img.shields.io/badge/.djvenv-виртуальное%20окружение-orange?logo=python&logoColor=white) |  
| **`Python`** | ![Python](https://img.shields.io/badge/requirements.txt-список%20зависимостей%20проекта-blue?logo=python&logoColor=white) |
| **`GitHub`** | ![GitHub](https://img.shields.io/badge/README.md-описание%20проекта-blue?logo=github&logoColor=white) |

## Планы развития
| Статус                | Бейджи / промежуточный статус / задача |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **`OPEN`** | ![GitHub](https://img.shields.io/badge/open-написание%20шаблонов%20HTML%20&%20CSS%20файлов-yellow?logo=github&logoColor=white) |
| **`OPEN`** | ![GitHub](https://img.shields.io/badge/open-наполнение%20БД%20информацией%20по%20сотрудникам%20инспекции-yellow?logo=github&logoColor=white) |
| **`OPEN`** | ![GitHub](https://img.shields.io/badge/open-Расширение%20функциональности%20аудита,%20добавление%20фильтрации%20и%20поиска%20записей-yellow?logo=github&logoColor=white) |
| **`OPEN`** | ![GitHub](https://img.shields.io/badge/open-Реализация%20системы%20ролей%20и%20прав%20доступа-yellow?logo=github&logoColor=white) |
| **`OPEN`** | ![GitHub](https://img.shields.io/badge/open-Интеграция%20с%20внешними%20сервисами%20и%20экспорт%20данных-yellow?logo=github&logoColor=white) |
| **`OPEN`** | ![GitHub](https://img.shields.io/badge/open-Поддержка%20работы%20с%20мобильных%20устройств-yellow?logo=github&logoColor=white) |

## Требования
![Python](https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=white)  
![Django](https://img.shields.io/badge/django-5.2.3-green?logo=django&logoColor=white)  
![pandas](https://img.shields.io/badge/pandas-для%20импорта/экспорта%20данных%20в%20Excel-blue?logo=pandas&logoColor=white)  
![openpyxl](https://img.shields.io/badge/openpyxl-для%20импорта/экспорта%20данных%20в%20Excel-007ACC?logo=python&logoColor=white)  
![GitHub](https://img.shields.io/badge/дополнительно%20смотри-requirements.txt-orange?logo=github&logoColor=white)

## Используемая IDLE
![Jupyter](https://img.shields.io/badge/Jupyter%20Lab-IDE%20&%20для%20анализа%20и%20обработки%20данных-orange?logo=jupyter&logoColor=white) 

## Запуск
![Run Server](https://img.shields.io/badge/запуск%20сайта-python%20manage.py%20runserver-brightgreen)

## Commands
#### Создание проектов и приложений
| Команда |	Описание |
|---------|----------|
|`django-admin startproject <project>`|	Создать новый проект Django|
|`python manage.py startapp <appname> `| Создать новое приложение внутри проекта|

#### Работа с сервером разработки
| Команда |	Описание |
|---------|----------|
|`python manage.py runserver `| Запуск локального сервера для разработки|

#### Миграции базы данных
| Команда |	Описание |
|---------|----------|
|`python manage.py makemigrations `| Создание миграций для всех приложений
|`python manage.py makemigrations <appname> `| Создание миграций для конкретного приложения|
|`python manage.py makemigrations --empty <appname> `| Создание пустой миграции для приложения (например, для кастомных изменений)|
|`python manage.py migrate`| Применение миграций, обновление схемы базы данных|
|`python manage.py showmigrations `| Просмотр списка миграций и их статуса|

#### Работа с пользователями
| Команда |	Описание |
|---------|----------|
|`python manage.py createsuperuser `| Создание суперпользователя с правами администратора|
|`python manage.py changepassword <username> `| Смена пароля пользователя через консоль|

#### Работа со статическими файлами
| Команда |	Описание |
|---------|----------|
|`python manage.py collectstatic `| Сбор статических файлов из приложений в одну папку (для деплоя)|

#### Работа с данными и тестами
| Команда |	Описание |
|---------|----------|
|`python manage.py shell `| Запуск интерактивной оболочки Python с доступом к проекту Django|
|`python manage.py test `| Запуск тестов проекта|
|`python manage.py dumpdata `| Экспорт данных базы в формате JSON или YAML|
|`python manage.py loaddata <fixture> `| Импорт данных из файла фикстуры|
|`python manage.py sqlflush `| Генерация SQL для очистки базы данных|

#### Диагностика и утилиты
| Команда |	Описание |
|---------|----------|
|`python manage.py check `| Проверка проекта на ошибки и предупреждения|
|`python manage.py diffsettings `| Показать отличия текущих настроек от стандартных|
|`python manage.py inspectdb `| Автоматическая генерация моделей из существующей базы данных|
|`python manage.py sendtestemail `| Тестирование отправки email|

#### Управление зависимостями (непосредственно pip)
| Команда |	Описание |
|---------|----------|
|`pip install -r requirements.txt `| Установка зависимостей из файла requirements.txt|
|`pip freeze > requirements.txt `| Сохранение текущих зависимостей в файл|