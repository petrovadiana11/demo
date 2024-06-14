from django.shortcuts import render
import os
import random
import string
from django.db import connection
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, "index.html")

# Создание пользователей
# for i in range(1, 16):
#     username = f"m{i}"
#     password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
#     user = User.objects.create_user(username, f"{username}@example.com", password)
#     user.save()
#     break

# Создание баз данных
# for i in range(1, 16):
#     db_name = f"Base{i}"
#     with connection.cursor() as cursor:
#         cursor.execute(f"CREATE DATABASE {db_name}")
#     break

# Настройка прав доступа пользователей к базам данных
# for i in range(1, 16):
#     username = f"m{i}"
#     db_name = f"Base{i}"
#     with connection.cursor() as cursor:
#         cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {username}")
#         cursor.execute(f"REVOKE CREATE DATABASE, REVOKE, GRANT FROM {username}")
#

# # Создание базы данных BaseAll и таблицы UserAll
# with connection.cursor() as cursor:
#     cursor.execute("CREATE DATABASE BaseAll")
#     cursor.execute("CREATE TABLE UserAll (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50))")

# # Заполнение таблицы Users данными созданных пользователей и паролях
# for i in range(1, 16):
#     username = f"m{i}"
#     password = User.objects.get(username=username).password
#     with connection.cursor() as cursor:
#         cursor.execute(f"INSERT INTO UserAll (username, password) VALUES ('{username}', '{password}')")

#
def decrypt_password(encrypted_password):
    # Реализация алгоритма расшифровки пароля
    # В этом примере мы используем простой алгоритм расшифровки, но в реальном приложении вам нужно использовать более безопасный алгоритм
    decrypted_password = encrypted_password[::-1]
    return decrypted_password
#
# # отображение паролей
def display_users_with_decrypted_passwords():
    with connection.cursor() as cursor:
        cursor.execute("SELECT username, password FROM Users")
        users = cursor.fetchall()
        for user in users:
            username, encrypted_password = user
            decrypted_password = decrypt_password(encrypted_password)
            print(f"Username: {username}, Password: {decrypted_password}")

display_users_with_decrypted_passwords()
#
#
# # копирование
def backup_database():
    db_name = "BaseAll"
    backup_file = f"{db_name}_backup.sql"
    command = f"pg_dump -U sa {db_name} > {backup_file}"
    os.system(command)
    print(f"Backup file created: {backup_file}")

backup_database()
#
# # восстановление бд
def restore_database():
    db_name = "BaseAll"
    backup_file = f"{db_name}_backup.sql"
    command = f"psql -U sa {db_name} < {backup_file}"
    os.system(command)
    print(f"Database restored from backup file: {backup_file}")

restore_database()