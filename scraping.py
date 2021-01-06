from bs4 import BeautifulSoup
import requests as req
import json
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://play-life.jp/search?utf8=%E2%9C%93&q=%E5%86%AC%E3%80%80%E3%83%87%E3%83%BC%E3%83%88%E3%80%80%E6%9D%B1%E4%BA%AC'
html = req.get(url).content
soup = BeautifulSoup(html, 'html.parser')
pre_texts = soup.select(".l-mt10.text-ellipsis__body--2lines.contents-list__item-name")
pre_links= soup.select(".l-mt20.contents-list__item")
pre_images= soup.select(".image--full-width")
texts= [t.get_text() for t in pre_texts]
links= [t.get('href') for t in pre_links]
images= [t.get("data-original") for t in pre_images]
lst= [
{
'title': [texts[num]],
'details': [{'LINK': links[num], 'IMAGE': images[num]}]
} for num in range(len(texts))
]
json_text = json.dumps(lst, ensure_ascii=False, indent=1)
print(json_text)
