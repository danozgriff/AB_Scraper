import scraperwiki
import mechanize
import cookielib
import re
from bs4 import BeautifulSoup
from datetime import datetime, date, time
# generate random integer values
import time    
from random import seed, randint
import pytz


au_tz = pytz.timezone('Australia/Perth')
dtstart = datetime.now(tz=au_tz).strftime("%Y-%m-%d %H:%M:%S")
dtend = None

#scraperwiki.sqlite.execute("create table RunHistory (`Start_DateTime` date NOT NULL, `End_DateTime`, UNIQUE (`Start_DateTime`))")

scraperwiki.sqlite.execute("insert or replace into RunHistory values (?, ?)",  [dtstart, dtend) 
scraperwiki.sqlite.commit() 

if 1==1:

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



    scraperwiki.sqlite.execute("drop table if exists company")  
    scraperwiki.sqlite.execute("create table company (`Rank` string, `Code` string, `Company` string, `Price` real, `Change` real, `% Change` real, `% Change 1 Year` real, `Market Cap` integer, `Date` string)")
    #scraperwiki.sqlite.execute("delete from company")  


    page = br.open(url)
    htmlcontent = page.read()
    soup = BeautifulSoup(htmlcontent, features="lxml")


    eoddate = soup.findAll("div", {"class": "header-timestamp"})[0].text[-11:].replace(" ", "-")
    date_obj = datetime.strptime(eoddate, '%d-%b-%Y')
    eoddate = date_obj.strftime('%Y-%m-%d')
    eoddateint = int(date_obj.strftime('%Y%m%d'))

    table = soup.find( "table", {"id":"asx_sp_table"} )

    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text + ",")
        output_rows.append(output_row)
        

    for sublst in output_rows:
        if len(sublst) > 0:
            rank = sublst[0].replace(",", "")
            code = sublst[2].replace(",", "") 
            company = sublst[3].replace(",", "") 
            price = sublst[4].replace(",", "").replace("$", "") 
            change = sublst[5].replace(",", "").replace("+", "")
            perchg = round(float(sublst[6].replace(",", "").replace("+", "").replace("%", "").strip('"'))/100.0, 4)                                                                                                   
            yrperchg = round(float(sublst[8].replace(",", "").replace("+", "").replace("%", "").strip('"'))/100.0, 4)                                                                                                 
            marketcap = sublst[7].replace(",", "").replace("$", "").replace(".", "").replace(" B", "0000000").replace(" M", "0000").replace(" TH", "0")    
            
            scraperwiki.sqlite.execute("insert or ignore into company values (?, ?, ?, ?, ?, ?, ?, ?, ?)",  [rank, code, company, price, change, perchg, yrperchg, marketcap, eoddate]) 

    scraperwiki.sqlite.commit()  


if 1==1:

    url = 'https://www.aussiebulls.com/SignalPage.aspx?lang=en&Ticker='

    
    #scraperwiki.sqlite.execute("delete from Signal_History")
    #scraperwiki.sqlite.commit()
    
    scraperwiki.sqlite.execute("drop table if exists Signal_History")  
    scraperwiki.sqlite.execute("create table Signal_History (`Code` varchar2(8) NOT NULL, `Date` date NOT NULL, `Price` real NOT NULL, `Signal` varchar2(15) NOT NULL, `Confirmation` char(1) NOT NULL, `AUD100` real NOT NULL, UNIQUE (`Code`, `Date`))")
    
    
    asxlist = scraperwiki.sqlite.execute("select distinct `Code` from company where Rank <= 300 and Date = ?", [eoddate])
    
    for x in asxlist["data"]:
        asxcode = str(x)[3:-2] + '.AX'
        #print asxcode
        #print str(asxlist["data"][x])[3:-2]
    
    #for x in asxlist:
    #    print asxlist
    
    #data = scraperwiki.scrape("http://www.asx.com.au/asx/research/ASXListedCompanies.csv")
    #url2 = 'https://www.aussiebulls.com/SignalPage.aspx?lang=en&Ticker=WOW.AX'
        br = mechanize.Browser()
    
        # sometimes the server is sensitive to this information
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        #scraperwiki.sqlite.execute("drop table if exists Signal_History")  
        #scraperwiki.sqlite.execute("create table Signal_History (`TIDM` varchar2(8) NOT NULL, `Date` date NOT NULL, `Price` real NOT NULL, `Signal` varchar2(15) NOT NULL, `Confirmation` char(1) NOT NULL, `GBP 100` real NOT NULL, UNIQUE (`TIDM`, `Date`))")
    

    
    #scraperwiki.sqlite.commit()
    #scraperwiki.sqlite.execute(".schema companies")
    #scraperwiki.sqlite.execute("select * from company") 
    
    #####for record in reader:
    #####        print record
    
        
        
        # seed random number generator
        seed(1)
        pausetime = randint(0, 60)
            
        print asxcode + " (Pause: " + str(pausetime) + ")"
        time.sleep(pausetime)
    
        response = br.open(url + asxcode)
    
        for pagenum in range(1):
            html = response.read()

            test1 = re.search(r'MainContent_signalpagehistory_PatternHistory24_DXDataRow0((.|\n)+)MainContent_signalpagehistory_PatternHistory24_IADD', html)
    
            if test1:
                test1 = test1.group(0)
        

                test3 = re.findall('(\">|img\/)(.*?)(<\/|\.gif)', test1.replace("\B", ""))
                
                #print test3

    
                while len(test3) >= 5:
        
                #print ASX_Code
                    sh_Date = re.search("(\w|\d)(.*)(\w|\d)", str(test3.pop(0)).replace(" ", "")).group(0)
                    #sh_Date = substr(sh_Date, 7,4) + '-' + substr(sh_Date, 4,2) + '-' + substr(sh_Date, 1,2)
                    #sh_Date = sh_Date[6:10] + '-' + sh_Date[3:5] + '-' + sh_Date[:2]
                    sh_Date = date(int(sh_Date[6:10]),int(sh_Date[3:5]),int(sh_Date[:2]))
                    sh_Price = re.search("(\w|\d)(.*)(\w|\d)", str(test3.pop(0)).replace(" ", "").replace(",", "")).group(0)
                    sh_Signal = re.search("(\w|\d)(.*)(\w|\d)", str(test3.pop(0)).replace(" ", "")).group(0)
                    sh_Confirmation = (re.search("[Uncheck|Check]", str(test3.pop(0)).replace(" ", "")).group(0).lower().replace("u","N")).replace("c", "Y").replace("h", "YY")
                    sh_AUD100 = re.search("(\w|\d)(.*)(\w|\d)", str(test3.pop(0)).replace(" ", "").replace(",", "")).group(0)
            
                    scraperwiki.sqlite.execute("insert or ignore into Signal_History values (?, ?, ?, ?, ?, ?)",  [asxcode, sh_Date, sh_Price, sh_Signal, sh_Confirmation, sh_AUD100]) 
    
                    scraperwiki.sqlite.commit()    
    





if 1==1:

    dtend = datetime.now(tz=au_tz).strftime("%Y-%m-%d %H:%M:%S")
     
    scraperwiki.sqlite.execute("insert or replace into RunHistory values (?, ?)",  [dtstart, dtend]) 
    scraperwiki.sqlite.commit() 
    
