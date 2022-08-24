"""
    Script for init Unesco application DB with the sample data.
    Script erases all previous data.

    Usage of this script:
        `python3 manage.py runscript many_load`

    Created:  Dmitrii Gusev, 24.08.2022
    Modified:
"""

import csv
import logging
from unesco.models import Category, State, Iso, Region, Site

log = logging.getLogger(__name__)
log.info('Initializing Unesco application DB with sample data...')

# CSV file wit hdata
CSV_FILE = 'csv/whc-sites-2018-clean.csv'


def run():
    log.info(f'Loading data for Unesco app DB from [{CSV_FILE}] file.')

    fhand = open(CSV_FILE)
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header
    log.debug(f'CSV file [{CSV_FILE}] opened OK.')

    # cleanup database - remove all data
    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()
    log.debug('Unesco DB cleaned OK.')

    for row in reader:
        print(row)

        # p, created = Person.objects.get_or_create(email=row[0])
        # c, created = Course.objects.get_or_create(title=row[2])

        # r = Membership.LEARNER
        # if row[1] == 'I':
        #     r = Membership.INSTRUCTOR
        # m = Membership(role=r, person=p, course=c)
        # m.save()
