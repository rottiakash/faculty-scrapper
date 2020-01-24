import requests 
from bs4 import BeautifulSoup
import json
dept = 'CS'
URL = "https://bit-bangalore.edu.in/index.php/computer-science/"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib') 
div = soup.find('div',{'id':'tabs_desc_373_4'})
table = div.find('table')
names = table.findAll('td',string="Name")
result = []
for p in names:
    ires = {}
    ires['Name'] = p.parent.findAll('td')[2].text
    result.append(ires)
i=0
names = table.findAll('td',string="Designation")
for p in names:
    result[i]['Desig'] = p.parent.findAll('td')[2].text
    i += 1

i=0
names = table.findAll('td',string="Qualification")
for p in names:
    result[i]['Qualification'] = p.parent.findAll('td')[2].text
    i += 1

i=0
names = table.findAll('td',string="Experience")
for p in names:
    result[i]['Experience'] = p.parent.findAll('td')[2].text
    i += 1

i=0
names = table.findAll('td',string="Publications")
for p in names:
    result[i]['Publications'] = p.parent.findAll('td')[2].text
    i += 1

i=0
names = table.findAll('td',string="Area of Interest")
for p in names:
    result[i]['AOI'] = p.parent.findAll('td')[2].text
    i += 1

i=0
names = table.findAll('td',string="Email ID")
for p in names:
    result[i]['Email'] = p.parent.findAll('td')[2].text
    i += 1

i=0
photos = table.findAll('img')
for photo in photos:
    result[i]['img'] = photo['src']
    i += 1

print(json.dumps(result ,indent=4, sort_keys=True))
print(len(result))

print('Saving images')
i=1
for ele in result:
    img_data = requests.get(ele['img']).content
    with open('images/'+dept+f"{i:02d}"+".jpg", 'wb') as handler:
        handler.write(img_data)
    i += 1