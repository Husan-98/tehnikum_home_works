from bs4 import BeautifulSoup
import requests
import re

link = 'https://www.afisha.uz/afisha/movies/?date=2021-04-08'

response = requests.get(link).text

reg = r'movie\/[0-9]+\/'

find_all_reg = re.findall(reg, response)

list_full_links = []

item_for_links = 'https://www.afisha.uz/'

for i in find_all_reg:
    list_full_links.append(item_for_links + i)

print("Кино которое идет сегодня: ")
print('\n')

# 3make json

forjson = []

for i in list_full_links:
    dict_for_json = {}
    response = requests.get(i).text
    soup = BeautifulSoup(response,features="html.parser")
    # name block
    name1 = soup.find('div', class_='data')
    name = name1.find('h3').text
    dict_for_json["name"] = name
    # print(name)
    # cinema
    cinema = soup.find('td', class_='place').text
    dict_for_json["cinema"] = cinema
    # print(cinema)
    # time
    time = soup.find('td', class_='time').text
    dict_for_json["time"] = time
    # print(time)
    # picture
    # picture1 = soup.find('th', class_ = 'image')
    # pict = str(picture1)
    # reg_img = r'https:\/\/.+.jpeg'
    # picture = re.findall(reg_img, pict)
    # #picture = picture[0]
    # print(str(picture))

    # dict_for_json['picture'] = picture
    # описание
    description = soup.find('div', class_='article').text
    # print(description)
    dict_for_json['description'] = description
    forjson.append(dict_for_json)

# print(forjson)

qwe = []
for i in forjson:
	if i not in qwe:
		r = i["name"]
		r = r.strip()
		r = r.title()
		qwe.append(r)
qwe = '\n'.join(qwe)
print(qwe)
