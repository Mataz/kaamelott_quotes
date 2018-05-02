# quotes.py - Citations des personnages de Kaamelott

import requests
import bs4
import textwrap
from urllib.parse import urljoin


""" TODO: Use pandas to organise the quotes in dataframes then style them with
          matplolib
"""
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}


def get_urls():

    url = 'https://fr.wikiquote.org/wiki/Kaamelott'

    req = requests.get(url, headers=headers).text
    soup = bs4.BeautifulSoup(req, 'lxml')

    for link in soup.select('dd a[href]')[:27]:
        print(urljoin(url, link.get('href')))


get_urls()


def perceval():
    perceval_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Perceval', headers=headers).text
    soup = bs4.BeautifulSoup(perceval_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Perceval \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(textwrap.fill(ref, width=90) + '\n'))


perceval()


def karadoc():
    karadoc_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Karadoc', headers=headers).text
    soup = bs4.BeautifulSoup(karadoc_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Karadoc \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(textwrap.fill(ref, width=90) + '\n'))


karadoc()


def arthur():
    arthur_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Arthur', headers=headers).text
    soup = bs4.BeautifulSoup(arthur_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations d\'Arthur \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(textwrap.fill(ref, width=90) + '\n'))


arthur()


def merlin():
    merlin_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Merlin', headers=headers).text
    soup = bs4.BeautifulSoup(merlin_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Merlin \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(textwrap.fill(ref, width=90) + '\n'))


merlin()


def leodagan():
    leodagan_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/L%C3%A9odagan', headers=headers).text
    soup = bs4.BeautifulSoup(leodagan_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Léodagan \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(textwrap.fill(ref, width=90) + '\n'))


leodagan()


def père_blaise():
    père_blaise_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/P%C3%A8re_Blaise', headers=headers).text
    soup = bs4.BeautifulSoup(père_blaise_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Père Blaise \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(
            textwrap.fill(ref, width=90) + '\n'))


père_blaise()


def bohort():
    bohort_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Bohort', headers=headers).text
    soup = bs4.BeautifulSoup(bohort_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Bohort \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(
            textwrap.fill(ref, width=90) + '\n'))


bohort()


def gauvain():
    gauvain_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Gauvain', headers=headers).text
    soup = bs4.BeautifulSoup(gauvain_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Gauvain \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(
            textwrap.fill(ref, width=90) + '\n'))


gauvain()


def guenièvre():
    guenièvre_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Gueni%C3%A8vre', headers=headers).text
    soup = bs4.BeautifulSoup(guenièvre_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Guenièvre \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(
            textwrap.fill(ref, width=90) + '\n'))


guenièvre()


def guethenoc():
    guethenoc_source = requests.get('https://fr.wikipedia.org/wiki/Personnages_de_Kaamelott#Guethenoc', headers=headers).text
    soup = bs4.BeautifulSoup(guethenoc_source, 'lxml')

    quote = soup.find_all('div', class_='citation')
    quotes = [x.text for x in quote]

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Guethenoc \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(
            textwrap.fill(ref, width=90) + '\n'))


guethenoc()



