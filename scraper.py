import scraperwiki
import mechanize
import re

# ASPX pages are some of the hardest challenges because they use javascript and forms to navigate
# Almost always the links go through the function function __doPostBack(eventTarget, eventArgument)
# which you have to simulate in the mechanize form handling library

# This example shows how to follow the Next page link

url = 'www.google.com'
url2 = 'https://www.aussiebulls.com/SignalPage.aspx?lang=en&Ticker=3PL.AX'
br = mechanize.Browser()

    # sometimes the server is sensitive to this information
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response = br.open(url2)

for pagenum in range(1):
   html = response.read()
    
  # test1 = re.search(r'MainContent_CompanyTicker((.)+)span', html).group(0)
  
#print re.findall(r'MainContent_signalpagehistory_PatternHistory24((.)+)\<\\table\>', html) 
test1 = re.search(r'MainContent_signalpagehistory_PatternHistory24_DXDataRow0((.|\n)+)MainContent_signalpagehistory_PatternHistory24_IADD', html).group(0) 
# test2 = re.findall(r'(\"\>|img\/)((.)+)\<\/td\>\<td', test1)
#test2 = re.findall('\">(.*)<\/', test1)
#test2 = re.findall('\">(.*?)<\/', test1)
#test2 re.search(r'\"\>(.*)\<\/?', test1)
#test2 = re.findall('\">(.*?)<\/', test1) GOOD
#test2 = re.findall('(\">|img\/)(.*?)(<\/|\.gif)', test1) BETTER
test2 = re.findall('(\">|img\/)(.*?)(<\/|\.gif)', test1.replace("\B", ""))
test3 = re.findall('\', \'(.*?)\', \'', test2)
print test3

   
  # print re.search(r'\w{3}\.AX', re.search(r'MainContent_CompanyTicker((.)+)span', html).group(0)).group(0)
