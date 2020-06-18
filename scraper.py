from bs4 import BeautifulSoup

html = open("https://www.marketindex.com.au/asx-listed-companies").read()
soup = BeautifulSoup(html)
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
    
for p in output_rows: print p
