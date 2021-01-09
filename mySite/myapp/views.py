from django.shortcuts import render
from .models import News
from django.views.generic import CreateView
from django.urls import reverse_lazy
from bs4 import BeautifulSoup
import requests
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Create your views here.
class Create(CreateView):
    template_name = 'home.html'
    model = News
    fields = ('url',) #フォームから受け取ったURLオブジェクトを生成している
    success_url = reverse_lazy('list')

def listfunc(request):
    for post in News.objects.all():
        url = post.url
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
