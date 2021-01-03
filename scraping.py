from bs4 import BeautifulSoup
import requests as req
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://www.y-shinno.com/vgg16-finetuning-uecfood100/'
html = req.get(url).content
soup = BeautifulSoup(html, 'html.parser')
text = soup.find(class_='entry-content').get_text()
print(text)
