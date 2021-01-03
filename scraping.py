from bs4 import BeautifulSoup
import requests as req
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://play-life.jp/search?utf8=%E2%9C%93&q=%E5%86%AC%E3%80%80%E3%83%87%E3%83%BC%E3%83%88%E3%80%80%E6%9D%B1%E4%BA%AC'
html = req.get(url).content
soup = BeautifulSoup(html, 'html.parser')
text = soup.select(".l-mt10.text-ellipsis__body--2lines.contents-list__item-name")
print([t.get_text() for t in text])
