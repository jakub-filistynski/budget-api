import os

from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """Command to load fixtures"""

    def handle(self, *args, **options):
        management.call_command("flush", "--noinput")

        for filename in sorted(os.listdir("fixtures")):
            if not filename.startswith("_"):
                exec(open(f"fixtures/{filename}").read())
                self.stdout.write(filename)
