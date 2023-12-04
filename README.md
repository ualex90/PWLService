# PWLService

<h3>Cоздание демонстрационных пользователей</h3>

Админ:
```bash
python3 manage.py ccsu 
```
Обычные пользователи и 1 из них модератор:
```bash
python3 manage.py ccusers 
```
При создании пользователей в консоль выведутся email, пароли и группы

<h3>Заполнение базы данных из фикстур</h3>

```bash
python3 manage.py loaddata fixtures/db.json
```

Администратор:
```
email = 'admin@sky.pro'
password = 'admin'
```
Пользователи:
```
ivanov@sky.pro - MODERATOR
petrov@sky.pro
sidorov@sky.pro

password - 123qwe
```
