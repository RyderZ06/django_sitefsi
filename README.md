# WEB-SITE FLIGHT SAFETY INSPECTION

## Используемые технологии

![Version](https://img.shields.io/badge/project%20ver-0.1-brightgreen)  
![Django](https://img.shields.io/badge/django-5.2.3-green?logo=django&logoColor=white)  
![Python](https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=white)  
![pandas](https://img.shields.io/badge/pandas-data%20analysis-blue?logo=pandas&logoColor=white)  
![openpyxl](https://img.shields.io/badge/openpyxl-Excel%20import%2Fexport-007ACC?logo=python&logoColor=white)  
![Jupyter](https://img.shields.io/badge/Jupyter%20Lab-IDE%20&%20Data%20Analysis-orange?logo=jupyter&logoColor=white)  
![Run Server](https://img.shields.io/badge/runserver-manage.py%20runserver-brightgreen)

## Описание
Веб-приложение для комплексного управления данными инспекционных проверок, разработанное с использованием фреймворка `Django версии 5.2.3`. Система обеспечивает возможность ввода, сохранения и просмотра инспекционных проверок и выявленных несоответствий с различными параметрами и статусами, что способствует эффективному контролю и анализу проверок.

Кроме того, приложение предоставляет пользователям доступ к информации об инспекционном составе, включая контактные данные сотрудников (почта, рабочий телефон), а также позволяет ознакомиться с иерархической структурой службы. Важным функционалом является возможность просмотра нормативных и организационных документов `Инспекции по Безопасности полётов`, таких как `должностные инструкции`, `положения об инспекции` и входящих в неё группах, а также иных регламентирующих материалов, на основании которых осуществляется деятельность инспекции.

Все `данные хранятся в реляционной базе данных`, что гарантирует их `надёжность`, `масштабируемость` и обеспечивает удобный и безопасный доступ к информации из любой точки посредством веб-браузера.

## Структура проекта
- `flightsafetyinspection/` — основной модуль Django-проекта.
- `.djvenv/` — виртуальное окружение.
- `templates/` — HTML-шаблоны для веб-интерфейса.
- `static/` — статические файлы (CSS, JS, изображения).
- `requirements.txt` — список зависимостей проекта.
- `README.md` — описание проекта и инструкции по запуску.

## Структура проекта
| Принадлежность                | Бейджи / Название папки / описание                                                                                                                           |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **`Django`** | ![Django](https://img.shields.io/badge/flightsafetyinspection-основной%20модуль%20Django--проекта-green?logo=django&logoColor=white) |
| **`Python`** | ![Python](https://img.shields.io/badge/.djvenv-виртуальное%20окружение-blue?logo=python&logoColor=white) |  
| **`Python`** | ![Python](https://img.shields.io/badge/requirements.txt-список%20зависимостей%20проекта-blue?logo=python&logoColor=white) |
| **`Python`** | ![Python](https://img.shields.io/badge/requirements.txt-список%20зависимостей%20проекта-blue?logo=python&logoColor=white) |


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