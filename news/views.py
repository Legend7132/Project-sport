from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.shortcuts import render
from newsapi import NewsApiClient


def news_list(request):

    newsapi = NewsApiClient(api_key ='bc16482d3ee144e2bb7933c67e386c48')
    topnews = newsapi.get_everything(q = 'UFC -li -Fishki.net', language = 'ru')

    latest = topnews['articles']
    n_list = []

    for i in range(len(latest)):
        news = latest[i]
        n_list.append([news['title'], news['description'], news['url'], news['urlToImage']])

    page_num = request.GET.get('page', 1)
    paginator = Paginator(n_list, 10)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, "news/news_list.html", {'page_obj': page_obj})