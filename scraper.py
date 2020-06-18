import scraperwiki
#import mechanize
#import re
import csv
#import time
#from datetime import datetime, date
#import datetime
import requests

URL = 'https://www.listcorp.com/_api/services/discovery/download-companies-list?sortBy=market_capitalisation&descending=true&recentlyListedCompanies=false'
page = requests.get(URL)
print page
