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

                s = str(data).find("Region:</strong>")
                e = str(data).find("</div>", s+1)
                k['Region'] = str(
                    data)[s+len("Region:</strong>"):e]

                s = str(data).find("Canton:</strong>")
                e = str(data).find("</div>", s+1)
                k['Canton'] = str(
                    data)[s+len("Canton:</strong>"):e]

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
