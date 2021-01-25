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

#季節と場所から各サイトに置ける検索URLを生成する関数
def url_maker(a,b):
    url_dic = {}
    playlife_url = 'https://play-life.jp/search?utf8=%E2%9C%93&q=' + a + '%E3%80%80%E3%83%87%E3%83%BC%E3%83%88%E3%80%80' + b
    aumo_url = 'https://aumo.jp/search?utf8=%E2%9C%93&q=' + a + '%E3%80%80%E3%83%87%E3%83%BC%E3%83%88%E3%80%80' + b
    #retrip_url = 'https://retrip.jp/search/?q='+ a + '+%E3%83%87%E3%83%BC%E3%83%88+' + b
    #icotto_url = 'https://icotto.jp/presses?query=' + a + '%E3%80%80%E3%83%87%E3%83%BC%E3%83%88%E3%80%80' + b
    url_dic['playlife'] = playlife_url
    url_dic['aumo'] = aumo_url
    return url_dic

#playlifeでのスクレイピング/パースを定義する関数
def bs_playlife(c):
    list_pl = []
    res_pl = requests.get(c).content
    bs_pl = BeautifulSoup(res_pl, "html.parser")
    ul_tag_pl = bs_pl.select(".l-mt20.contents-list__item")
    for tag_pl in ul_tag_pl:
        title_pl = tag_pl.select_one(".l-mt10.text-ellipsis__body--2lines.contents-list__item-name").get_text()
        url_pl = 'https://play-life.jp' + tag_pl.get('href')
        list_pl.append([title_pl, url_pl])
    return list_pl

#aumoでのスクレイピング/パースを定義する関数
def bs_aumo(d):
    list_aumo = []
    res_aumo = requests.get(d).content
    bs_aumo = BeautifulSoup(res_aumo, "html.parser")
    ul_tag_aumo = bs_aumo.select(".entries-item")
    for tag_aumo in ul_tag_aumo:
        title_aumo = tag_aumo.select_one(".entries-item-title").get_text()
        url_aumo = 'https://aumo.jp' + tag_aumo.select_one('a').get('href')
        list_aumo.append([title_aumo, url_aumo])
    return list_aumo

#生成したURLから取得した要素のリストを生成する関数
def list_maker(u):
    show_list = []
    list_1 = bs_playlife(u.get('playlife')) #playlifeのリスト
    show_list.extend(list_1)
    list_2 = bs_aumo(u.get('aumo')) #aumoのリスト
    show_list.extend(list_2)
    return show_list

def listfunc(request):
    for post in Dating.objects.all():
        month = post.month
        spot = post.spot
    s = season(month)
    urls = url_maker(s,spot)
    list = []
    list_final = list_maker(urls)
    list.extend(list_final)
    context = {'list': list,}
    return render(request, 'list.html', context)
