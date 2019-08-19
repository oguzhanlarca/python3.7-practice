from csv import DictReader
from datetime import datetime
from django.core.management import BaseCommand
from dashboard.models import DashboardData
from pytz import UTC

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from dashBoardData.csv into our DashboardData model"

    def handle(self, *args, **options):
        if DashboardData.objects.exists():
            print('Dashboard data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading dashboard data for manufacturing process")
        for row in DictReader(open('./dashBoardData.csv')):
            data = DashboardData()
            data.pulsometer_readout = row['Pulsometer_readout']
            data.engine_efficiency = float(row['Engine_efficiency'])
            data.red_value = row['red_Value']
            data.blue_value = row['blue_Value']
            data.green_value = row['green_Value']

            raw_timestamp = row['time_stamp']
            timestamp = UTC.localize(
                datetime.strptime(raw_timestamp, DATETIME_FORMAT))
            data.timestamp = timestamp
            data.save()
        print("Dashboard data finished loading")
