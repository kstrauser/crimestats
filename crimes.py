#!/usr/bin/env python

import csv
import os

# Data was downloaded from http://1.usa.gov/1j19Hpl -
# "January to June 2013 Offenses Reported to Law Enforcement" -
# and exported to a CSV file with Numbers 3.2.
RAW = '~/Downloads/Table_4_January_to_June_2012-2013_Offenses_Reported_to_Law_Enforcement_by_State_by_City.csv'
COLUMNS = ('state', 'city', 'year', 'population', 'violent crime', 'murder', 'rape', 'robbery',
           'aggravated assault', 'property crime', 'burglary', 'larceny-theft',
           'motor-vehicle-theft', 'arson')
VIOLENT_COLUMNS = {'murder', 'rape', 'robbery', 'aggravated assault'}
PROPERTY_COLUMNS = {'burglary', 'larceny-theft','motor-vehicle-theft'}

def string_to_number(value):
    if not value:
        return None
    value = value.replace(',', '')
    return int(value)

def crime_data():
    """
    Convert the raw CSV data into usable information.
    """

    previous_row = None

    with open(os.path.expanduser(RAW)) as infile:
        rows = csv.DictReader(infile, COLUMNS)

        # Skip past the description lines at the top of the file until we get into actual data
        while next(rows)['state'] != 'State':
            pass

        for row in rows:
            if row['state'].startswith('1 The 2013 population figures are FBI estimates based '):
                break            

            # The spreadsheet leaves out certain values that were repeated from previous rows.
            # This copies those values forward when needed.
            for key in {'state', 'city', 'population'}:
                if not row[key]:
                    row[key] = previous_row[key]

            if row['year'] != '2013':
                previous_row = row
                continue

            # Remove the extra cruft columns
            del row[None]

            # Convert fields stored as text to numbers
            for key, value in row.items():
                if key not in {'state', 'city'}:
                    row[key] = string_to_number(value)

            # Phoenix, AZ did not report aggravated assaults in 2013, so this uses the rate from
            # 2012 under the assumption that it should be similar.
            if row['city'] == 'PHOENIX7 ':
                row['aggravated assault'] = 2411
                row['violent crime'] = sum(row[value] for value in VIOLENT_COLUMNS)

            # Chicago, IL did not report rapes in 2012 or 2012. This assumes that Chicago has
            # a similar rate as the rest of the country and multiplies that rate by Chicago's
            # 2012 population.
            if row['city'] == 'CHICAGO9':
                row['rape'] = 485
                row['violent crime'] = sum(row[value] for value in VIOLENT_COLUMNS)

            # Sanity checking
            total_violent = sum(row[value] for value in VIOLENT_COLUMNS)
            assert row['violent crime'] == total_violent, row

            total_property = sum(row[value] for value in PROPERTY_COLUMNS)
            assert row['property crime'] == total_property, row

            row['raw'] = {}
            row['rate'] = {}
            for key, value in row.items():
                if key in {'state', 'city', 'population', 'year', 'raw', 'rate'}:
                    continue
                del row[key]
                row['raw'][key] = value

                row['rate'][key] = None if value is None else 100000 * value / row['population']

            yield row

            previous_row = row

def alpha_by_city_state(row):
    return row['city'], row['state']


for row in sorted(list(crime_data()), key=alpha_by_city_state):
    print row
