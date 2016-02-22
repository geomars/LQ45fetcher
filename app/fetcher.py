import csv
import requests


URL = "http://www.sharecsv.com/dl/139bd57779f5b84910d471900bdb6ffb/lq45_quotes_v2.csv"


def get_data():
    r = requests.get(URL)
    data = r.text
    RESULTS = {'children': []}
    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        if float(line['share_volume']) > .001:
            RESULTS['children'].append({
                'symbol': line['symbol'],
                'company_name': line['company_name'],
                'lastsale': line['lastsale'],
                'netchange': line['netchange'],
                'percent_change': line['pctchange'],
                'volume': line['share_volume'],
            })

    return RESULTS
