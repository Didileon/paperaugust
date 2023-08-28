from django.core.management.base import BaseCommand, CommandError
from ...models import Post, PostCategory



class Command(BaseCommand):
    help = 'Delete news'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"

    def add_arguments(self, parser):
        parser.add_argument('category', type=str, nargs='?', default=21)

    def handle(self, *args, **options):
        answer = input(f'Do you really want to delete posts in {options["category"]}? yes/no  ')  # спрашиваем пользователя действительно ли он хочет удалить все товары
        # считываем подтверждение

        if answer != 'yes':  # в случае подтверждения действительно удаляем все товары
            self.stdout.write(self.style.ERROR('Access denied'))
            return
        try:
            category = PostCategory.objects.get(name="options['category']")
            Post.objects.filter(postCategory=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfull deleted all posts from category Это Питер, детка!'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category Это Питер, детка!'))

