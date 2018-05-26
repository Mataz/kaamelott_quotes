# quotes.py - Citations des personnages de Kaamelott
import requests
import bs4
import json

import pandas as pd

pd.set_option('display.max_colwidth', 120)

""" TODO: Use pandas to organise the quotes in dataframes then style them with
          matplolib
"""
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

urls = ['https://fr.wikiquote.org/wiki/Kaamelott', 'https://fr.wikiquote.org/wiki/Kaamelott/Perceval',
        'https://fr.wikiquote.org/wiki/Kaamelott/Karadoc', 'https://fr.wikiquote.org/wiki/Kaamelott/Arthur',
        'https://fr.wikiquote.org/wiki/Kaamelott/Merlin', 'https://fr.wikiquote.org/wiki/Kaamelott/P%C3%A8re_Blaise',
        'https://fr.wikiquote.org/wiki/Kaamelott/Bohort', 'https://fr.wikiquote.org/wiki/Kaamelott/Gauvain',
        'https://fr.wikiquote.org/wiki/Kaamelott/L%C3%A9odagan', 'https://fr.wikiquote.org/wiki/Kaamelott/Gueni%C3%A8vre',
        'https://fr.wikiquote.org/wiki/Kaamelott/Lancelot', 'https://fr.wikiquote.org/wiki/Kaamelott/Venec']
data = []


# Scrape the characters' names, quotes and their references over a list of URLs.
def scrape_site():
    for url in urls:
        req = requests.get(url, headers=headers)
        soup = bs4.BeautifulSoup(req.content, 'lxml')

        if url is not None:

            names = [x.text for x in soup.find_all('span', class_='mw-headline')]
            quotes = [x.text for x in soup.find_all('div', class_='citation')]
            refs = [x.text for x in soup.find_all('div', class_='ref')]

        data.append({
            'Name': names,
            'Quotes': quotes,
            'References': refs
        })

    return json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)


print(scrape_site())















