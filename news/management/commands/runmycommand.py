from django.core.management.base import BaseCommand, CommandError
from ...models import Post, Category


class Command(BaseCommand):
    help = 'Delete news'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)


    def handle(self, *args, **options):


        # здесь можете писать любой код, который выполнется при вызове вашей команды
        self.stdout.readable()
        self.stdout.write('Do you really want to delete posts in IT? yes/no')
        answer = input()

          # считываем подтверждение

        if answer == 'yes':  # в случае подтверждения действительно удаляем все товары


            Post.objects.filter(categoryType=Category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfull deleted all posts from category IT'))
            return

        self.stdout.write(self.style.ERROR(f'Could not find category IT'))



