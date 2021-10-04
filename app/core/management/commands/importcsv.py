"""
This command Help to import CSV dataset file to the Database
"""

from django.core.management import BaseCommand
from core.models import GlobalLandTemperaturesByCity
from django.utils import timezone
from datetime import date
from django.db import Error, transaction


class Command(BaseCommand):
    help = "Loads Global_Land_Temperatures_By_City from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        self.stdout.write("Please wait...")
        start_time = timezone.now()

        file_path = options["file_path"]

        i = 0
        for line in open(file_path):
            if i == 0:
                i = 1
                continue
            i += 1
            row = line.strip().split(',')
            GlobalLandTemperaturesByCity.objects.create(
                dt=self.currect_date(row[0]),
                AverageTemperature=float(row[1]) if row[1] else 0,
                AverageTemperatureUncertainty=float(
                    row[2]) if row[2] else 0,
                City=row[3],
                Country=row[4],
                Latitude=row[5],
                Longitude=row[6]
            )
            if i % 10000 == 0:
                self.stdout.write(f"{i} item imported")

        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )

    def currect_date(self, datestr: str):
        if "/" in datestr:
            # 9/1/1960
            tmp = datestr.split('/')
            dt = date(int(tmp[2]), int(tmp[0]), int(tmp[1]))
        elif "-" in datestr:
            # 1772-10-01
            tmp = datestr.split('-')
            dt = date(int(tmp[0]), int(tmp[1]), int(tmp[2]))
        else:
            dt = None
        return dt
