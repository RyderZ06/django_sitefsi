# WEB-SITE FLIGHT SAFETY INSPECTION

| Purpose                         | Badges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Latest (`master`: future 0.1)** | ![Create App](https://github.com/jupyter-widgets/ipywidgets/actions/workflows/tests.yml/badge.svg?query=branch%3Amain) ![App Status: latest](https://img.shields.io/readthedocs/ipywidgets?logo=read-the-docs) ![Binder:main](https://mybinder.org/badge_logo.svg)                                               |
| **Stable**                      | [![Version](https://img.shields.io/pypi/v/ipywidgets.svg?logo=pypi)](https://pypi.python.org/pypi/ipywidgets) [![Conda Version](https://img.shields.io/conda/vn/conda-forge/ipywidgets.svg?logo=conda-forge)](https://anaconda.org/conda-forge/ipywidgets) [![Documentation Status](https://img.shields.io/readthedocs/ipywidgets?logo=read-the-docs)](https://ipywidgets.readthedocs.io/en/stable/?badge=stable) [![Binder:7.x](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-widgets/ipywidgets/7.x?urlpath=lab/tree/docs%2Fsource%2Fexamples) |
| **Communication**               | [![Join the chat at https://gitter.im/ipython/ipywidgets](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jupyter-widgets/Lobby) [![Discourse](https://img.shields.io/badge/help_forum-discourse-blue?logo=discourse)](https://discourse.jupyter.org/c/widgets/46)                                                                                                                                                                                                                                                                                             |
|                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |


**Latest (`main`: future 0.1)**  
![Create App](https://github.com/jupyter-widgets/ipywidgets/actions/workflows/tests.yml/badge.svg?query=branch%3Amain)  
*Статус сборки проекта*

![App Status: latest](https://img.shields.io/readthedocs/ipywidgets?logo=read-the-docs)  
*Статус документации*

![Binder:main](https://mybinder.org/badge_logo.svg)  
*Интерактивный запуск в Binder*


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