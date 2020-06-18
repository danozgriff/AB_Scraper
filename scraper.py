import scraperwiki
#import mechanize
#import re
import csv
#import time
#from datetime import datetime, date
#import datetime


#br = mechanize.Browser()

    # sometimes the server is sensitive to this information
#br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

#data = scraperwiki.scrape("http://www.asx.com.au/asx/research/ASXListedCompanies.csv")

scraperwiki.sqlite.execute("drop table if exists company")  
scraperwiki.sqlite.execute("create table company (`GICS industry group` string, `ASX code` string, `Company name` string, `Last Refreshed` date, `Top 500` char(1))")
  
scraperwiki.sqlite.save(['GICS industry group', 'ASX code', 'Company name'], list(csv.DictReader(scraperwiki.scrape('http://www.asx.com.au/asx/research/ASXListedCompanies.csv').splitlines()[2:])), table_name='company')
#scraperwiki.sqlite.execute("update company set `Last Refreshed` = date('now') where `Last Refreshed` is null")
#scraperwiki.sqlite.execute("update company set `Top 500` = 'Y' where `Last Refreshed` = date('now')")
#scraperwiki.sqlite.execute("update company set `Top 500` = 'N' where `Last Refreshed` <> date('now')")
scraperwiki.sqlite.commit()
