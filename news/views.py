from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from dateutil.parser import isoparse
from urllib.request import Request, urlopen
from PIL import Image
from newsapi import NewsApiClient


def news_list(request):

    newsapi = NewsApiClient(api_key ='bc16482d3ee144e2bb7933c67e386c48')
    topnews = newsapi.get_everything(q = 'UFC -<li>', language = 'ru')

    latest = topnews['articles']
    n_list = []

    for i in range(len(latest)):
        news = latest[i]

        n_desc = news['description']
        if ('Fishki.net' in n_desc):
            n_desc = n_desc.replace(n_desc[n_desc.find(' – Самые лучшие и интересные'):], '.')
        
        img_url = news['urlToImage']
        img_height = 300
        if img_url is not None:
            req = Request(img_url, headers={'User-Agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)'})
            img = Image.open(urlopen(req))
            img_height = img.height
            if img.height > 300:
                img_height = 300
        
        n_list.append([news['title'], n_desc, news['url'], isoparse(news['publishedAt']), img_url, img_height])

    n_list.sort(key = lambda x: x[3], reverse = True)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(n_list, 10)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, "news/news_list.html", {'page_obj': page_obj})