# blog-on-flask

 MVC:
   - model - db: модель, описание данных в базе данных
   - View - template: отвечает за отображение пользователю данных
   - Controller - связывает базу данных и приложение (пользователя):
                  - получение запроса от пользователя
                  - обработка запроса
                  - перенаправление на выполнение (формируется страница и отдаётся пользователю)
                  
  flask    ->  django
  
Controller ->   View

   View    -> Templates

  django ->    View   = Controller -> flask
  
  django -> Templates =    View    -> flask

1. Установка mysql/ password = spectr (ond) / root (new)

--> https://www.youtube.com/watch?v=3vsC05rxZ8c

!!!  https://www.digitalocean.com/community/tutorials/mysql-ubuntu-18-04-ru

в новой версии mysql после устновки необходимо выполнить скрипт безопасности и настроить аутентификацию и привилегии
пользователь root в MySQL по умолчанию аутентифицируется с помощью плагина auth_socket, а не по паролю.
когда вам необходимо организовать доступ к MySQL со стороны сторонней программы
необходимо изменить метод аутентификации с auth_socket на mysql_native_password

mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;

mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

mysql> FLUSH PRIVILEGES;

mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;


2.

--> virtualenv venv
--> venv\Scripts\activate.bat

3. Функциональность выделяется в отдельный модуль, плагин -> Blueprint (app django)

blueprint.py - кусок настолько изолированной функциональности, что его можно
скопипастить в другой проект
