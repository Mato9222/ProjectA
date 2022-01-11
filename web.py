import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0100',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#frm > div > table > tbody > tr')

for tr in trs:
    title = tr.select_one('td:nth-child(5) > div > div > div.ellipsis.rank01 > span > a')['title']

    print(title)
