## Тестовое задание для MEOWPUNK

Протестировано на Ubuntu 22.04.2 LTS.

Устанавливаем Python 3.10 или выше сборкой из исходников:
```
cd
wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
tar -xzvf Python-3.11.1.tgz
cd Python-3.11.1
./configure --enable-optimizations --prefix=/home/www/.python3.11
sudo make altinstall
```

Устанавливаем Poetry:
```
curl -sSL https://install.python-poetry.org | python3 -
```

Клонируем репозиторий:
```
mkdir -p ~/code/
cd ~/code
git clone https://github.com/hyypia/meowpunk_task.git
cd meowpunk_task
```

Перед запуском необходимо добавить файлы `client.csv` и `server.csv` в
директорию `data/`.

Устанавливаем зависимости Poetry и запускаем бота вручную:
```
poetry install
poetry run python main
```

Далее будет необходимо ввести необходимую дату, после чего пройдет инициализация
базы данных, создание таблицы и появится информация о количестве потребленной памяти.

После отработки скрипта в его корневой директории появится файл с данными `task.db`.
