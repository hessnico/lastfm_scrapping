import config as cf
import requests
from bs4 import BeautifulSoup
import csv
import datetime
import sys

def get_last_library_page(user):
    page = requests.get(f'https://www.last.fm/pt/user/{user}/library')
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="col-main")
    uls = results.select('nav.pagination')

    lis = [li.text for ul in uls for li in ul.findAll('li')]
    last_page_to_search = int(''.join(filter(str.isdigit, lis[-2])))

    return last_page_to_search

def get_soup(index, user):
    cookies, headers = cf.import_cookies_headers()
    response = requests.get(f'https://www.last.fm/pt/user/{user}', cookies=cookies, headers=headers)
    print(f"    Getting soup...")
    try:
        page = requests.get(f'https://www.last.fm/pt/user/{user}/library?page={index}', cookies=cookies, headers=headers)
        print("    Success")
    except:
        print("    Failed getting soup")
    return BeautifulSoup(page.content, "html.parser")

def write_csv(soup):
    tbodys = soup.find_all('tbody')[:-1]
    with open("out.csv", "a", newline="") as f:
        print("     Appending new information in csv")
        writer = csv.writer(f)
        for tbody in tbodys[::-1]:
            for row in tbody.find_all('tr')[::-1]:
                writer.writerow(main_info(row))

def main_info(row):
    """main function to scrap lastfm scrobbles
        return a list with 
            artist_name
            track_name
            timestamp in unix format
            track_id
            action (loved ou unloved)
            cover name
            lastfm link for music
            lastfm link for artist
            href for listening
            link for cover
            cover icon link
    """
    itens = []
    get_artist_track_timestamp(row, lst = ['track_name', 'artist_name', 'timestamp', 'track_spelling_id', 'action'], info_lst=itens)
    itens.append(row.find('td', {'class' : 'chartlist-image'}).find('img')['alt'])
    itens.append(row.find('a', {'class' : 'dropdown-menu-clickable-item more-item--track'})['href'])
    itens.append(row.find('a', {'class' : 'dropdown-menu-clickable-item more-item--artist'})['href'])
    itens.append(row.find('a').attrs['href'])
    try:
        itens.append(row.find('td', {'class' : 'chartlist-image'}).find('a')['href'])
    except:
        itens.append(None)
    itens.append(row.find('td', {'class' : 'chartlist-image'}).find('img')['src'])
    print(f"        Got: {itens}")
    return itens

def get_artist_track_timestamp(soup, lst, info_lst):
    for val in lst:
        info_lst.append(soup.find('input', {'name' : val})['value'])  