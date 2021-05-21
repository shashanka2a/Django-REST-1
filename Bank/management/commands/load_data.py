from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from Bank.models import Bank
from pytz import UTC




ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from data.csv"

    def handle(self, *args, **options):
        if Bank.objects.exists():
            print('data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("Loading data...")

        for row in DictReader(open('./Data.csv',encoding="utf8")):
            try:
                i = Bank()
                print( row['ifsc'])
        
                i.ifsc = row['ifsc']
                i.bank_id = row['bank_id']
                i.address = row['address']
                i.city = row['city']
                i.state = row['state']
                i.branch = row['branch']
                i.district = row['district']
                i.bank_name = row['bank_name']

                i.save()
            except:
                print('Invalid format')

