import scraperwiki
import mechanize
import cookielib
from bs4 import BeautifulSoup


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
#scraperwiki.sqlite.execute("create table company (`Rank` real, `Code` string, `Company` string, `Price` real, `Change` real, `% Change` real, `% Change 1 Year` real, `Market Cap` string)")



page = br.open(url)
htmlcontent = page.read()
soup = BeautifulSoup(htmlcontent, features="lxml")

##print soup

#table = soup.find("asx_sp_table")
table = soup.find( "table", {"id":"asx_sp_table"} )

#i=0
output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
        #if i < 100:
            #print column.text
         #   i += 1
    output_rows.append(output_row)
    
#output_rows = [item.replace("u'", "").replace("'", "").replace("\n", "").replace("[", "").replace("]", "") for item in output_rows]

#output_rows = str(row).replace("u'", "").replace("'", "").replace("\n", "").replace("[", "").replace("]", "").split(',')

#output_rows = 

#for p in output_rows: print str(p).split(',')

#.replace("u'", "").replace("'", "").replace("\n", "").replace("[", "").replace("]", "")

#for p in output_rows:
#    print [val for val in str(p).split()]

for sublst in output_rows:
    #for item in sublst:
    scraperwiki.sqlite.execute("insert or ignore into company values (?, ?, ?, ?, ?, ?, ?, ?)",  [sublst[0], sublst[2], sublst[3], sublst[4], sublst[5], sublst[6], sublst[8], sublst[7]) 
        #print item,        # note the ending ','
    #print 
