# quotes.py - Citations des personnages de Kaamelott

import requests
import bs4


def perceval():
    source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Perceval').text
    soup = bs4.BeautifulSoup(source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    for x in quotes:
        print(str(x))


perceval()



