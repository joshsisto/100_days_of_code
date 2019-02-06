import os
import csv
import collections
from typing import List
from datetime import datetime
from datetime import date

today = datetime.today()
today_date = date.today()
ww = date.today().isocalendar()[1]
day = date.today().isocalendar()[2]
print(f"current work week:{ww}.{day}")
print(date.today().isocalendar())
print(today, today_date)

data = []

Record = collections.namedtuple(
    'Record',
    'Week, Mon,	Tue, Wed, Thu, Fri,	Sat, Sun'
)


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'training_plan.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)


def parse_row(row):
    row['Week'] = int(row['Week'])

    record = Record(
        **row
    )

    return record


def hot_days() -> List[Record]:
    return sorted(data, key=lambda r: -r.actual_max_temp)


def cold_days() -> List[Record]:
    return sorted(data, key=lambda r: r.actual_max_temp)


def wet_days() -> List[Record]:
    return sorted(data, key=lambda r: -r.actual_precipitation)
