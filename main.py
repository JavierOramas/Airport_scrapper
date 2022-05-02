from bs4 import BeautifulSoup
import requests
from os import path
import json


def scrap_page(url):
    soup = BeautifulSoup(requests.get(url).text, features="html.parser")
    countries = []
    for i in soup.find_all("ul", {"class": 'airport-list'}):
        countries.append(
            [{"url": j.get("href"), "country": j.get("title"), "airports": []} for j in i.find_all("a")])

    for i in countries:
        for j in i:
            new_url = 'https://www.air-port-codes.com'+j['url']
            print(new_url)
            soup = BeautifulSoup(requests.get(new_url).text,
                                 features="html.parser")
            for k in soup.find_all("ul", {"class": 'airport-list'}):
                for l in k.find_all("a"):
                    j['airports'].append({"url": "https://www.air-port-codes.com" +
                                          l.get('href'),
                                          "name": l.get('title'),
                                          "keywords": '',
                                          "IATA Code": '',
                                          "City": '',
                                          "Province": '',
                                          "Country": '',
                                          "Continent": '',
                                          "Full Location": '',
                                          "Website": '',
                                          "Latitude": '',
                                          "Longitude": '',
                                          "Elevation": ''
                                          })

            for k in j['airports']:
                soup = BeautifulSoup(requests.get(
                    k['url']).text, features="html.parser")

                data = soup.find_all("div", {'class': "gaptiny"})[0]

                s = str(data).find("Airport Keywords:</strong>")
                e = str(data).find("</div>", s+1)
                k['keywords'] = str(
                    data)[s+len("Airport Keywords:</strong>"):e]

                s = str(data).find("Airport (IATA) Code:</strong>")
                e = str(data).find("</div>", s+1)
                k['IATA Code'] = str(
                    data)[s+len("Airport (IATA) Code:</strong>"):e]

                t_s = str(data).find("City:</strong>")
                s = str(data).find("title=", t_s)
                e = str(data).find("</a>", s+1)
                k['City'] = str(
                    data)[s+len("title= "):e]

                t_s = str(data).find("Province:</strong>")
                s = str(data).find("title=", t_s)
                e = str(data).find("</a>", s+1)
                k['Province'] = str(
                    data)[s+len("title= "):e]

                t_s = str(data).find("State:</strong>")
                s = str(data).find("title=", t_s)
                e = str(data).find("</a>", s+1)
                k['State'] = str(
                    data)[s+len("title= "):e]

                t_s = str(data).find("Country:</strong>")
                s = str(data).find("title=", t_s)
                e = str(data).find("</a>", s+1)
                k['Country'] = str(
                    data)[s+len("title= "):e]

                s = str(data).find("Continent:</strong>")
                e = str(data).find("</div>", s+1)
                k['Continent'] = str(
                    data)[s+len("Continent:</strong>"):e]

#
                s = str(data).find("Atoll:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Atoll:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Atoll'] = temp

                s = str(data).find("Canton:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Canton:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Canton'] = temp

                s = str(data).find("Commune:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Commune:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Commune'] = temp

                s = str(data).find("Corporation:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Corporation:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Corporation'] = temp

                s = str(data).find("Council:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Council:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Council'] = temp

                s = str(data).find("County:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("County:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['County'] = temp

                s = str(data).find("Department:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Department:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Department'] = temp

                s = str(data).find("District:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("District:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['District'] = temp

                s = str(data).find("Division:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Division:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Division'] = temp

                s = str(data).find("Emirate:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Emirate:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Emirate'] = temp

                s = str(data).find("Governorate:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Governorate:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Governorate'] = temp

                s = str(data).find("Island:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Island:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Island'] = temp

                s = str(data).find("Municipality:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Municipality:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Municipality'] = temp

                s = str(data).find("Parish:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Parish:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Parish'] = temp

                s = str(data).find("Periphery:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Periphery:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Periphery'] = temp

                s = str(data).find("Prefecture:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Prefecture:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Prefecture'] = temp

                s = str(data).find("Province:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Province:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Province'] = temp

                s = str(data).find("Quarter:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Quarter:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Quarter'] = temp

                s = str(data).find("Rayon:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Rayon:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Rayon'] = temp

                s = str(data).find("Region:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Region:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Region'] = temp

                s = str(data).find("Section:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Section:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Section'] = temp

                s = str(data).find("State:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("State:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['State'] = temp

                s = str(data).find("State/Province:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("State/Province:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['State/Province'] = temp

                s = str(data).find("Sub-Division:</strong>")
                e = str(data).find("</div>", s+1)
                temp = str(data)[s+len("Sub-Division:</strong>"):e]
                if temp[:len("lass")+1] != 'lass':
                    k['Sub-Division'] = temp
#
                s = str(data).find("Full Location:</strong>")
                e = str(data).find("</div>", s+1)
                k['Full Location'] = str(
                    data)[s+len("Full Location:</strong>"):e]

                s = str(data).find("Latitude:</strong>")
                e = str(data).find("</div>", s+1)
                k['Latitude'] = str(
                    data)[s+len("Latitude:</strong>"):e]

                s = str(data).find("Longitude:</strong>")
                e = str(data).find("</div>", s+1)
                k['Longitude'] = str(
                    data)[s+len("Longitude:</strong>"):e]

                s = str(data).find("Elevation:</strong>")
                e = str(data).find("</div>", s+1)
                k['Elevation'] = str(
                    data)[s+len("Elevation:</strong>"):e]

    with open('airports.json', "w") as file:
        json.dump(countries, file)


scrap_page("https://www.air-port-codes.com/airport-list/countries/")
