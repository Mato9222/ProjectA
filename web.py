import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017 ) #"host_num"을 지우고 해당 호스트 넘버로 변경
db = client.dbsparta

def get_tag_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://www.melon.com/dj/themegenre/djthemegenre_list.htm', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#old_content > table > tbody > tr')

    urls = []
    for tr in trs:
        a = tr.select_one('td.title > a')
        if a is not None:
            base_url = 'https://movie.naver.com/'
            url = base_url + a['href']
            urls.append(url)

    return urls

def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/sdb/rank/rpeople.nhn', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#old_content > table > tbody > tr')

    urls = []
    for tr in trs:
        a = tr.select_one('td.title > a')
        if a is not None:
            base_url = 'https://movie.naver.com/'
            url = base_url + a['href']
            urls.append(url)

    return urls

def thema_melon():
    headers: dict[str, str] = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0100',headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    trs = soup.select('#frm > div > table > tbody > tr')

    for tr in trs:
        title = tr.select_one(f"'tr:nth-child({tr}) > td:nth-child(5) > div > div > div.ellipsis.rank01 > span > a'")['title']
        artist = tr.select_one(f"tr:nth-child({tr}) > td:nth-child(5) > div > div > div.ellipsis.rank02 > a")['title']
        url = tr.select_one(f"'tr:nth-child({tr}) > td:nth-child(3) > div > a > img'")['src']

        doc = {
            'artist': artist,
            'title': title,
            'image.url': url
        }

    db.playlist.insert_one(doc)  # DB에 저장

thema_melon()
all_list = list(db.playlist.find())
print(all_list)