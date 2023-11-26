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
        for u in users:
            user = User.objects.create(
                email=u.get('email'),
                first_name=u.get('first_name'),
                last_name=u.get('last_name'),
                is_staff=u.get('is_staff'),
                is_active=u.get('is_active'),
            )
            user.set_password(u.get('password'))
            user.save()
            count += 1

            print(f'{count}. email: {user.email}, password: {u.get("password")};')
