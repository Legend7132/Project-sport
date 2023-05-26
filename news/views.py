from django.core.paginator import Paginator
from django.shortcuts import render
from newsapi import NewsApiClient


def news_list(request):

    newsapi = NewsApiClient(api_key ='bc16482d3ee144e2bb7933c67e386c48')
    topnews = newsapi.get_everything(q = 'UFC -li -Fishki.net', language = 'ru')

    latest = topnews['articles']
    title = []
    desc = []
    url = []
    im_url =[]

    for i in range(len(latest)):
        news = latest[i]

        title.append(news['title'])
        desc.append(news['description'])
        url.append(news['url'])
        im_url.append(news['urlToImage'])

    all_news = zip(title, desc, url, im_url)

    return render(request, "news/news_list.html", {'all_news': all_news})