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
        print(str(textwrap.fill(x, width=110) + '\n'))


perceval()


def karadoc():
    karadoc_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Karadoc').text
    soup = bs4.BeautifulSoup(karadoc_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    print('\n Citations de Karadoc \n')
    for x in quotes:
        print(str(textwrap.fill(x, width=110) + '\n'))


karadoc()


def arthur():
    arthur_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Arthur').text
    soup = bs4.BeautifulSoup(arthur_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    print('\n Citations d\'Arthur \n')
    for x in quotes:
        print(str(textwrap.fill(x, width=110) + '\n'))


arthur()


def merlin():
    merlin_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Merlin').text
    soup = bs4.BeautifulSoup(merlin_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    print('\n Citations de Merlin \n')
    for x in quotes:
        print(str(textwrap.fill(x, width=110) + '\n'))


merlin()


def leodagan():
    leodagan_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/L%C3%A9odagan').text
    soup = bs4.BeautifulSoup(leodagan_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Léodagan \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(textwrap.fill(ref, width=90) + '\n'))


leodagan()