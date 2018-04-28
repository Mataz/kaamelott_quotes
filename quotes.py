# quotes.py - Citations des personnages de Kaamelott

import requests
import bs4
import textwrap


""" TODO: Use pandas to organise the quotes in dataframes then style them with
          matplolib
"""


def perceval():
    perceval_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Perceval').text
    soup = bs4.BeautifulSoup(perceval_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    print('\n Citations de Perceval \n')
    for x in quotes:
        print(str(textwrap.fill(x, width=90) + '\n'))


perceval()


def karadoc():
    karadoc_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Karadoc').text
    soup = bs4.BeautifulSoup(karadoc_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    print('\n Citations de Karadoc \n')
    for x in quotes:
        print(str(textwrap.fill(x, width=90) + '\n'))


karadoc()


def arthur():
    arthur_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Arthur').text
    soup = bs4.BeautifulSoup(arthur_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    print('\n Citations d\'Arthur \n')
    for x in quotes:
        print(str(textwrap.fill(x, width=90) + '\n'))


arthur()



