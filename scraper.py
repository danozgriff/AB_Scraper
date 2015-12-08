import scraperwiki
import mechanize
import re
import csv

# ASPX pages are some of the hardest challenges because they use javascript and forms to navigate
# Almost always the links go through the function function __doPostBack(eventTarget, eventArgument)
# which you have to simulate in the mechanize form handling library

# This example shows how to follow the Next page link

data = scraperwiki.scrape("http://www.asx.com.au/asx/research/ASXListedCompanies.csv")
url2 = 'https://www.aussiebulls.com/SignalPage.aspx?lang=en&Ticker=3PL.AX'
br = mechanize.Browser()

    # sometimes the server is sensitive to this information
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

#####reader = csv.DictReader(data.splitlines()[2:10])

#scraperwiki.sqlite.execute("drop table if exists companies")  
#scraperwiki.sqlite.execute("create table companies (`GICS industry group` string, `ASX  code` string, `Company  name` string)")           

scraperwiki.sqlite.save([`ASX  code`], list(csv.DictReader(scraperwiki.scrape('http://www.asx.com.au/asx/research/ASXListedCompanies.csv').splitlines()[2:10])), table_name='companies')
#scraperwiki.sqlite.save(['industry', 'code', 'company'], list(csv.DictReader(scraperwiki.scrape('http://www.asx.com.au/asx/research/ASXListedCompanies.csv').splitlines()[2:10])), table_name="companies")


scraperwiki.sqlite.commit()
#scraperwiki.sqlite.execute(".schema companies")
scraperwiki.sqlite.execute("select * from companies") 

#####for record in reader:
#####        print record

###response = br.open(url2)

###for pagenum in range(1):
###   html = response.read()
    
#comp = re.search(r'MainContent_CompanyTicker(\w{3,}\.AX)span', html).group(0)
###comp = '3PL.AX'
  
#print re.findall(r'MainContent_signalpagehistory_PatternHistory24((.)+)\<\\table\>', html) 
###test1 = re.search(r'MainContent_signalpagehistory_PatternHistory24_DXDataRow0((.|\n)+)MainContent_signalpagehistory_PatternHistory24_IADD', html).group(0) 
# test2 = re.findall(r'(\"\>|img\/)((.)+)\<\/td\>\<td', test1)
#test2 = re.findall('\">(.*)<\/', test1)
#test2 = re.findall('\">(.*?)<\/', test1)
#test2 re.search(r'\"\>(.*)\<\/?', test1)
#test2 = re.findall('\">(.*?)<\/', test1) GOOD
#test2 = re.findall('(\">|img\/)(.*?)(<\/|\.gif)', test1) BETTER

#test2 = re.findall('(\">|img\/)(.*?)(<\/|\.gif)', test1.replace("\B", ""))

#test3 = re.findall('\', \'(.*?)\', \'', test2)
###test3 = re.findall('(\">|img\/)(.*?)(<\/|\.gif)', test1.replace("\B", ""))
#print "".join(test3[0].split)
#test4 = [x.replace(" ", "") for x in test3]

#print re.search(r"\',\'(.*)\',\'", str(test3[0]).replace(" ", "")).group(0)
###while len(test3) >= 5:
###    print comp
###    print re.search("(\w|\d)(.*)(\w|\d)", str(test3.pop(0)).replace(" ", "")).group(0)
###    print re.search("(\w|\d)(.*)(\w|\d)", str(test3.pop(0)).replace(" ", "")).group(0)
###    print re.search("(\w|\d)(.*)(\w|\d)", str(test3.pop(0)).replace(" ", "")).group(0)
###    print (re.search("[Unc|C]heck", str(test3.pop(0)).replace(" ", "")).group(0).replace("Uncheck","N")).replace("Check", "Y")
###    print re.search("(\w|\d)(.*)(\w|\d)", str(test3.pop(0)).replace(" ", "")).group(0)


   
  # print re.search(r'\w{3}\.AX', re.search(r'MainContent_CompanyTicker((.)+)span', html).group(0)).group(0)
