import scraperwiki
import mechanize
import cookielib
from bs4 import BeautifulSoup


url = 'https://www.marketindex.com.au/asx20'
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    # sometimes the server is sensitive to this information
br.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36')]

page = br.open(url)
htmlcontent = page.read()
soup = BeautifulSoup(htmlcontent, features="lxml")

##print soup

#table = soup.find("asx_sp_table")
table = soup.find( "table", {"id":"asx_sp_table"} )

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
#output_rows = [item.replace("u'", "").replace("'", "").replace("\n", "").replace("[", "").replace("]", "") for item in output_rows]

for r in range(len(output_rows)):    
    print output_rows[r]
