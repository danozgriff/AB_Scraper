import scraperwiki
import mechanize
#import re
import csv
#import time
#from datetime import datetime, date
#import datetime
#import requests

url = 'https://www.marketindex.com.au/asx-listed-companies'
#page = requests.get(URL)
#print page

br = mechanize.Browser()

    # sometimes the server is sensitive to this information
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

response = br.open(url)
for pagenum in range(1):
    html = response.read()
print html

#data = scraperwiki.scrape("https://www.listcorp.com/_api/services/discovery/download-companies-list?sortBy=market_capitalisation&descending=true&recentlyListedCompanies=false")
#print data

    

#scraperwiki.sqlite.execute("drop table if exists company")  
#scraperwiki.sqlite.execute("create table company (`Code` string, `Company` string, `Market Cap` real, `Last Trade` real, `Change` real, `% Change` real, `Sector` string)")
  
#scraperwiki.sqlite.save(['Code', 'Company', 'Market Cap', 'Last Trade', 'Change', '% Change', 'Sector'], list(csv.DictReader(scraperwiki.scrape('https://www.listcorp.com/_api/services/discovery/download-companies-list?sortBy=market_capitalisation&descending=true&recentlyListedCompanies=false').splitlines()[1:])), table_name='company')
#scraperwiki.sqlite.execute("update company set `Last Refreshed` = date('now') where `Last Refreshed` is null")
#scraperwiki.sqlite.execute("update company set `Top 500` = 'Y' where `Last Refreshed` = date('now')")
#scraperwiki.sqlite.execute("update company set `Top 500` = 'N' where `Last Refreshed` <> date('now')")
#scraperwiki.sqlite.commit()
