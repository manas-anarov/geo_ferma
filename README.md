0) 
переименовать файл .env.example в .env

1) 
чтобы запустить переходим в папку проекта и запускаем
строим<br>
<b>sudo make build</b>


2)
запускаем<br>
<b>sudo make up</b>

3)
миграции
<br><b>sudo make makemigrations</b><br>
<b>sudo make migrate</b><br>



4)
создаем админа<br>
<b>sudo make superuser</b>


5) 
запускаем тесты<br>
<b>sudo make test</b>



для логов<br>
<b>sudo make logs</b><br>
остальные команды смотрим в файле Makefile

6)
открываем админку, вводим логин и пароль<br>
http://0.0.0.0:8080/admin/<br>
добавляем Culture и Season<br>


7)
Зарегистрировать фермера. <br>

Открыть в браузере register. <br>
http://localhost:8080/api/v1/rest-auth/register/<br>


Указать username, email, password. После нажатия на кнопку регистрации, на экран должно вывестись, поле key, с токеном из символов. Нужно скопировать token.<br>
Вот пример токена : 551fcd43bbe00b10021b6ebc7ab58f725c6f262e

8)
Фермер указывает свою землю и культуру.<br>
В команду ниже вставить ранее скопированный Token. <br>

<b>curl -d '{"season_id": 1,"culture_id": 1,"latitude": 3,"longitude": 100}' -H "Content-Type: application/json" -H "Authorization: Token <Вставь токен Сюда>" -X POST http://localhost:8080/api/v1/post/create/</b><br>

Должно получиться примерно так:<br>
<b>curl -d '{"season_id": 1,"culture_id": 1,"latitude": 3,"longitude": 100}' -H "Content-Type: application/json" -H "Authorization: Token 551fcd43bbe00b10021b6ebc7ab58f725c6f262e" -X POST http://localhost:8080/api/v1/post/create/</b><br>

Запустить в консоли команду полученную команду curl. После этого должна создаться запись в базе.

9)
Список земель фермера, get запрос<br>
Можно посмотреть все земли фермера запустив команду curl вставив туда свой токен.<br>
<b>curl -H "Authorization: Token 551fcd43bbe00b10021b6ebc7ab58f725c6f262e" -X GET http://localhost:8080/api/v1/post/list/</b>
