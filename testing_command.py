from abc.models import Xyz


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('abc')
