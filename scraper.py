import scraperwiki
#import mechanize
#import re
import csv
#import time
#from datetime import datetime, date
#import datetime
#import requests

#URL = 'https://www.listcorp.com/_api/services/discovery/download-companies-list?sortBy=market_capitalisation&descending=true&recentlyListedCompanies=false'
#page = requests.get(URL)
#print page

#br = mechanize.Browser()

    # sometimes the server is sensitive to this information
#br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

data = scraperwiki.scrape("https://www.listcorp.com/_api/services/discovery/download-companies-list?sortBy=market_capitalisation&descending=true&recentlyListedCompanies=false")
print data
