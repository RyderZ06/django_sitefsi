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
Веб-приложение для комплексного управления данными инспекционных проверок, разработанное с использованием фреймворка `Django версии 5.2.3`. Система обеспечивает возможность ввода, сохранения и просмотра инспекционных проверок и выявленных несоответствий с различными параметрами и статусами, что способствует эффективному контролю и анализу проверок.

Кроме того, приложение предоставляет пользователям доступ к информации об инспекционном составе, включая контактные данные сотрудников (почта, рабочий телефон), а также позволяет ознакомиться с иерархической структурой службы. Важным функционалом является возможность просмотра нормативных и организационных документов `Инспекции по Безопасности полётов`, таких как `должностные инструкции`, `положения об инспекции` и входящих в неё группах, а также иных регламентирующих материалов, на основании которых осуществляется деятельность инспекции.

Все `данные хранятся в реляционной базе данных`, что гарантирует их `надёжность`, `масштабируемость` и обеспечивает удобный и безопасный доступ к информации из любой точки посредством веб-браузера.

## Структура проекта
| Технология                | Бейджи / Название папки / описание |
|--------------------------|-------------------------------------|
| **`Django`** | ![Django](https://img.shields.io/badge/flightsafetyinspection-основной%20модуль%20Django--проекта-brightgreen?logo=django&logoColor=white) |
| **`Python`** | ![Python](https://img.shields.io/badge/.djvenv-виртуальное%20окружение-orange?logo=python&logoColor=white) |  
| **`Python`** | ![Python](https://img.shields.io/badge/requirements.txt-список%20зависимостей%20проекта-blue?logo=python&logoColor=white) |
| **`GitHub`** | ![GitHub](https://img.shields.io/badge/README.md-описание%20проекта-blue?logo=github&logoColor=white) |

#### `Структура проекта, которая будет добавлена позже`
- `templates/` — HTML-шаблоны для веб-интерфейса.
- `static/` — статические файлы (CSS, JS, изображения).

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
**создать новый проект командой:** `django-admin startproject myproject`