import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%ED%99%94+%EC%83%81%EC%98%81'
data = requests.get(url).text
#print(data)
res_status =requests.get(url).status_code
#print('상대코드:', res_status)

movie = BeautifulSoup(data, 'lxml')#parsing
titles = movie.select('a.this_text.text')
#print(titles)
ratings = movie.select('span.num')
#print(ratings')

info = []
for title, rating in zip(titles,ratings):
    info.append({
        'Title': title.get_text(strip=True),
        'Rating': rating.get_text(strip=True)
    })

print('수집영화정보')
for i, info in enumerate(info, start=1):
    print(f'{i} : {info["Title"]} 평점 => {info["Rating"]}')