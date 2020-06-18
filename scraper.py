import requests
from bs4 import BeautifulSoup

website_url = requests.get('https://www.marketindex.com.au/asx-listed-companies').text

soup = BeautifulSoup(website_url,'lxml')

print soup

table = soup.find("asx_sp_table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
    
for p in output_rows: print p
