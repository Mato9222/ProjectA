import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

def thema_melon():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=487635230', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    artist = [singer.get_text() for singer in soup.find_all('span', attrs={'class': 'checkEllipsis'})]
    title = [title.find('a').get_text() for title in soup.find_all('div', attrs={'class': 'ellipsis rank01'})]

    doc = {
        'artist': artist,
        'title': title
         }

    db.playlist.insert_one(doc)

thema_melon()