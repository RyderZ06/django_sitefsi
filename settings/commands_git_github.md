# **Основные команды Git**
### Команда	Описание

| Commands | Description |
|----------|-------------|
|`git config --global user.name "Имя"`|Настройка имени и почты пользователя (важно для коммитов)|  
|`git config --global user.email "email"`| Настройка имени и почты пользователя (важно для коммитов)|
|`git init`|	Создание нового локального репозитория|
|`git clone <url>`|	Клонирование удалённого репозитория на локальную машину|
|`git status`|	Просмотр текущего состояния репозитория (изменённые, подготовленные файлы и т.д.)|
|`git add <файл>	`| Добавление файла(ов) в индекс (staging area) для последующего коммита|
|`git add .`|	Добавление всех изменений в индекс|
|`git commit -m "сообщение"`|	Создание коммита с описанием изменений|
|`git commit --amend`|	Изменение последнего коммита|
|`git log`|	Просмотр истории коммитов|
|`git log --oneline`|	Краткий однострочный вывод истории|
|`git diff`|	Просмотр изменений, ещё не добавленных в индекс|
|`git checkout <ветка>`|	Переключение на другую ветку|
|`git switch <ветка>`|	Современная команда для переключения веток (безопаснее, чем checkout)|
|`git branch`|	Просмотр списка веток|
|`git branch <новая_ветка>`|	Создание новой ветки|
|`git branch -d <ветка>`|	Удаление ветки|
|`git merge <ветка>`|	Слияние указанной ветки с текущей|
|`git remote add origin <url>`|	Привязка локального репозитория к удалённому|
|`git remote`|	Просмотр списка удалённых репозиториев|
|`git push`|	Отправка локальных коммитов в удалённый репозиторий|
|`git pull`|	Получение и слияние изменений из удалённого репозитория|
|`git stash`|	Временное сохранение изменений, чтобы переключиться на другую ветку без коммита|
|`git reset <файл>`|	Удаление файла из индекса (отмена git add)|
|`git show <коммит>`|	Просмотр деталей конкретного коммита|
## **Полезные советы**
Для настройки `Git` перед началом работы обязательно выполните `git config` с вашим именем и email, чтобы коммиты корректно отображали автора.

`Для переключения между ветками` лучше `использовать` `git switch`, так как эта команда более безопасна для новичков.

Для просмотра истории удобно использовать `git log --oneline --graph --decorate`, чтобы видеть коммиты в виде графа.

Команда `git stash` полезна, если нужно временно убрать изменения, чтобы переключиться на другую ветку без коммита.