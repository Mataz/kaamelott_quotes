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

    ref = soup.find_all('div', class_='ref')
    refs = [x.text for x in ref]

    print('\n Citations de Perceval \n')
    for quote, ref in zip(quotes, refs):
        print(str(textwrap.fill(quote, width=110) + '\n') + str(textwrap.fill(ref, width=90) + '\n'))


perceval()


def karadoc():
    karadoc_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Karadoc').text
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
    arthur_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Arthur').text
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
    merlin_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Merlin').text
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


def père_blaise():
    père_blaise_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/P%C3%A8re_Blaise').text
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
    bohort_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Bohort').text
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
    gauvain_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Gauvain').text
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
    guenièvre_source = requests.get('https://fr.wikiquote.org/wiki/Kaamelott/Gueni%C3%A8vre').text
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
    guethenoc_source = requests.get('https://fr.wikipedia.org/wiki/Personnages_de_Kaamelott#Guethenoc').text
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


