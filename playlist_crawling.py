import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017 ) #mongoDB는 27017 포트 사용
db = client.dbsparta #dbsparta 라는 DB 생성

def thema_melon():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=501856302', headers=headers) #해당 URL 입력
    #HTML을
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#frm > div > table > tbody >tr')

# selector 입력
    for music in musics:
        title = music.select_one('div.ellipsis.rank01 > span > a').text
        artist = music.select_one('div.ellipsis.rank02 > a').text
        url = music.select_one('div > a > img')['src']


        doc = {
            'title': title,
            'artist': artist,
            'image.url': url
        }

        db.Rest_playlist.insert_one(doc) #DB에 저장


# #     title = title.find('a').get_text() for title in soup.find_all('div', attrs={'class': 'ellipsis rank01'})
# #     artist = singer.get_text() for singer in soup.find_all('span', attrs={'class': 'checkEllipsis'})
# #     url = img.get('src') for img in soup.find_all('img',attrs={'onerror':"WEBPOCIMG.defaultAlbumImg(this);"})
#
    # doc = {
    #     'title': title,
    #     'artist': artist,
    #     'image.url' : url
    #      }
    # db.playlist.insert_one(doc) #DB에 저장

thema_melon()
