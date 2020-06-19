import scraperwiki
import mechanize
import cookielib
from bs4 import BeautifulSoup
from datetime import datetime


url = 'https://www.marketindex.com.au/asx-listed-companies'
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    # sometimes the server is sensitive to this information
br.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36')]



#scraperwiki.sqlite.execute("drop table if exists company")  
#scraperwiki.sqlite.execute("create table company (`Rank` string, `Code` string, `Company` string, `Price` real, `Change` real, `% Change` real, `% Change 1 Year` real, `Market Cap` integer)")


page = br.open(url)
htmlcontent = page.read()
soup = BeautifulSoup(htmlcontent, features="lxml")


eoddate = soup.findAll("div", {"class": "header-timestamp"})[0].text[-11:]
print eoddate

date_obj = datetime.strptime(eoddate, '%d-%b-%Y')
print date_obj.strftime('%d-%m-%Y')


