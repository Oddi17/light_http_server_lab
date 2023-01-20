# light_http_server_lab

# Задание:
Создать простой http-сервер. Имеется форма регистрации и логина. Также вохможна отправка сообщений от одного пользователя другому. Доступен список всех сообщений, а также их просмотр. Сообщения хранятся в базе (например sqlite)

# Проверка результата
Все задачи обернуть в докер. Чекер для второго - скрипт,который проверяет работу обработчиков.Если все проверки пройдены приходит сообщение "ОК". 

# Сборка контейнера:
Необходимо собрать докер командой sudo docker-compose up --build -d
# Запуск
После всех установок и сборки можно заходить на сайт по адресу:http://0.0.0.0:1234
# Проверка
Для проверки работы в архиве прикреплен файл checker.py
Также прикреплен файл data.json для проверки БД

## Начальная страница
<p align="center">
  <img src="https://github.com/Oddi17/light_http_server_lab/blob/main/screenshots/1.png" width="600px" height="400px"/></p>

## Страница после регистрации нового пользователя и процесса авторизации
<p align="center">
  <img src="https://github.com/Oddi17/light_http_server_lab/blob/main/screenshots/2.png" width="600px" height="400px"/></p>
  
## Страница после этапа авторизации
<p align="center">
  <img src="https://github.com/Oddi17/light_http_server_lab/blob/main/screenshots/3.png" width="600px" height="400px"/></p>
  
## Процесс отправки сообщения
<p align="center">
  <img src="https://github.com/Oddi17/light_http_server_lab/blob/main/screenshots/4.png" width="600px" height="400px"/></p>

## Страница отправленного сообщения
<p align="center">
  <img src="https://github.com/Oddi17/light_http_server_lab/blob/main/screenshots/5.png" width="600px" height="400px"/></p>

## Страница с полученным сообщением на другой стороне
<p align="center">
  <img src="https://github.com/Oddi17/light_http_server_lab/blob/main/screenshots/6.png" width="600px" height="400px"/></p>

## Страница с просмотром полученного сообщения
<p align="center">
  <img src="https://github.com/Oddi17/light_http_server_lab/blob/main/screenshots/7.png" width="600px" height="400px"/></p>

## Страница после нажатия кнопки выход на главной странице
<p align="center">
  <img src="https://github.com/Oddi17/light_http_server_lab/blob/main/screenshots/8.png" width="600px" height="400px"/></p>

## Результат проверки чекера(тест)
<p align="center">
  <img src="https://github.com/Oddi17/light_http_server_lab/blob/main/screenshots/9.png" width="500px" height="200px"/></p>
