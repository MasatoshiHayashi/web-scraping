from django.shortcuts import render
from .models import Dating
from django.views.generic import CreateView
from django.urls import reverse_lazy
from bs4 import BeautifulSoup
import requests
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Create your views here.
class Create(CreateView):
    template_name = 'home.html'
    model = Dating
    fields = ('month','spot') #フォームから受け取ったオブジェクトを生成している
    success_url = reverse_lazy('list')

def season(m):
    if m == '1':
        return '冬'
    elif m == '2':
        return '冬'
    elif m == '3':
        return '春'
    elif m == '4':
        return '春'
    elif m == '5':
        return 'GW'
    elif m == '6':
        return '梅雨'
    elif m == '7':
        return '夏'
    elif m == '8':
        return '夏'
    elif m == '9':
        return '秋'
    elif m == '10':
        return '秋'
    elif m == '11':
        return '秋'
    elif m == '12':
        return 'クリスマス'
    else:
        return ''

def listfunc(request):
    for post in Dating.objects.all():
        month = post.month
        spot = post.spot
    s = season(month)
    url = 'https://play-life.jp/search?utf8=%E2%9C%93&q=' + s + '%E3%80%80%E3%83%87%E3%83%BC%E3%83%88%E3%80%80' + spot
    list = []
    response = requests.get(url).content
    bs = BeautifulSoup(response, "html.parser")
    ul_tag = bs.select(".l-mt20.contents-list__item")
    for tag in ul_tag:
        title = tag.select_one(".l-mt10.text-ellipsis__body--2lines.contents-list__item-name").get_text()
        urls = 'https://play-life.jp' + tag.get('href')
        list.append([title, urls])
    context = {'list': list,}
    return render(request, 'list.html', context)
