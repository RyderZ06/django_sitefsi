# WEB-SITE FLIGHT SAFETY INSPECTION

## Статус и Технологии

| Назначение                | Бейджи и описание                                                                                                                           |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Статус сборки**         | ![Build Status](https://github.com/RyderZ06/django_sitefsi/actions/workflows/tests.yml/badge.svg?query=branch%3Amain) <br> *Автоматические тесты и CI* |
| **Документация**          | ![Docs](https://img.shields.io/readthedocs/django_sitefsi?logo=read-the-docs) <br> *Актуальная документация проекта*                         |
| **Python версия**         | ![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white) <br> *Требуемая версия Python*                      |
| **Django версия**         | ![Django](https://img.shields.io/badge/django-5.2.3-green?logo=django&logoColor=white) <br> *Используемый фреймворк*                        |
| **REST API**              | ![Django REST Framework](https://img.shields.io/badge/djangorestframework-API-blue?logo=django&logoColor=white) <br> *API на DRF*            |
| **pandas**                | ![pandas](https://img.shields.io/badge/pandas-data%20analysis-blue?logo=pandas&logoColor=white) <br> *Импорт и обработка данных*             |
| **openpyxl**              | ![openpyxl](https://img.shields.io/badge/openpyxl-Excel%20import%2Fexport-007ACC?logo=python&logoColor=white) <br> *Работа с Excel файлами*  |
| **Анализ данных**         | ![Jupyter](https://img.shields.io/badge/Jupyter%20Lab-Data%20Analysis-orange?logo=jupyter&logoColor=white) <br> *Работа с данными*            |
| **Запуск проекта**        | ![Run Server](https://img.shields.io/badge/run-server-brightgreen) <br> *Команда запуска: `python manage.py runserver`*                      |

## Описание
Веб-приложение для управления данными инспекционных проверок, разработанное на базе Django 5.2.3. Позволяет вводить, сохранять и просматривать записи аудита с различными параметрами и статусами. Все данные хранятся в реляционной базе данных, что обеспечивает надежность, масштабируемость и удобный доступ из любой точки с помощью браузера.

## Структура проекта
- `flightsafetyinspection/` — основной модуль Django-проекта.
- `.djvenv/` — виртуальное окружение.
- `apps/` — директория с приложениями (например, audit, users и т.д.).
- `templates/` — HTML-шаблоны для веб-интерфейса.
- `static/` — статические файлы (CSS, JS, изображения).
- `requirements.txt` — список зависимостей проекта.
- `README.md` — описание проекта и инструкции по запуску.


## Планы развития
- Расширение функциональности аудита, добавление фильтрации и поиска записей.
- `Реализация системы ролей и прав доступа.`
- Интеграция с внешними сервисами и экспорт данных.
- `Поддержка работы с мобильных устройств.`

## Требования
- `Python 3.10+`
- `Django 5.2.3`
- `djangorestframework` (при необходимости API)
- `pandas`, `openpyxl` (для импорта/экспорта данных в Excel)
- Другие зависимости указаны в `requirements.txt`

## Используемая IDLE
- `Jupyter Lab` (для анализа и обработки данных)
- Любая современная IDE для Python (PyCharm, VSCode и др.)

## Запуск
Выполнить `python manage.py runserver` для запуска сайта.