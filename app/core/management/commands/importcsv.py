"""
This command Help to import CSV dataset file to the Database
"""

import csv
from django.core.management import BaseCommand
from core.models import GlobalLandTemperaturesByCity
from django.utils import timezone
from datetime import datetime


class Command(BaseCommand):
    help = "Loads Global_Land_Temperatures_By_City from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        self.stdout.write("Please wait...")
        start_time = timezone.now()

        file_path = options["file_path"]
        with open(file_path, "r") as csv_file:
            data = list(csv.reader(csv_file, delimiter=","))
            for row in data[1:]:

                if "/" in row[0]:
                    # 9/1/1960
                    tmp = row[0].split('/')
                    dt = datetime.date(tmp[2], tmp[0], tmp[1])
                elif "-" in row[0]:
                    # 1772-10-01
                    tmp = row[0].split('-')
                    dt = datetime.date(tmp[0], tmp[1], tmp[2])
                else:
                    dt = None

                obj = GlobalLandTemperaturesByCity.objects.create(
                    dt=dt,
                    AverageTemperature=float(row[1]),
                    AverageTemperatureUncertainty=float(row[2]),
                    City=row[3],
                    Country=row[4],
                    Latitude=row[5],
                    Longitude=row[6]
                )
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
