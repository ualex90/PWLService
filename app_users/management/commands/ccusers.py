from django.core.management import BaseCommand

from app_users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        users = [
            {
                'email': 'ivanov@sky.pro',
                'first_name': 'Иван',
                'last_name': 'Иванов',
                'is_staff': False,
                'is_active': True,
                'password': '123qwe',
            },
            {
                'email': 'petrov@sky.pro',
                'first_name': 'Петр',
                'last_name': 'Петров',
                'is_staff': False,
                'is_active': True,
                'password': '123qwe',
            },
            {
                'email': 'sidorov@sky.pro',
                'first_name': 'Сидор',
                'last_name': 'Сидоров',
                'is_staff': False,
                'is_active': True,
                'password': '123qwe',
            },
        ]
        count = 0
        for i in users:
            user = User.objects.create(
                email=i.get('email'),
                first_name=i.get('first_name'),
                last_name=i.get('last_name'),
                is_staff=i.get('is_staff'),
                is_active=i.get('is_active'),
            )
            user.set_password(i.get('password'))
            user.save()
            count += 1

            print(f'{count}. email: {user.email}, password: {i.get("password")};')
