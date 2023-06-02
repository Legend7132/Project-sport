from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from dateutil.parser import isoparse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from newsapi import NewsApiClient


def news_list(request):

    newsapi = NewsApiClient(api_key ='bc16482d3ee144e2bb7933c67e386c48')
    topnews = newsapi.get_everything(q = 'UFC -<li>', language = 'ru')

    latest = topnews['articles']
    news_list = []

    for i in range(len(latest)):
        news = latest[i]

        news_desc = news['description']
        if ('Fishki.net' in news_desc):
            news_desc = news_desc.replace(news_desc[news_desc.find(' – Самые лучшие и интересные'):], '.')
        
        news_list.append([news['title'], news_desc, news['url'], isoparse(news['publishedAt']), news['urlToImage']])

    news_list.sort(key = lambda x: x[3], reverse = True)
    paginator = Paginator(news_list, 10)
    page_num = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, "news/news_list.html", {'page_obj': page_obj})


def video_list(request, pn):
    main_url = "https://ufc.ru/watch/library?search=&page=" + str(pn - 1)
    html_code = str(urlopen(main_url).read(),'utf-8')
    soup = BeautifulSoup(html_code, "html.parser")
    
    pre_video_total = soup.find('div', {"class": 'althelete-total'}).text
    video_total = pre_video_total[pre_video_total.find(' ') + 1:]

    pre_headers = soup.find_all('h3', {"class": 'e-t4'})
    headers = []
    for el in pre_headers:
        headers.append(el.text.strip())

    pre_video_page_urls = soup.find_all('a', {"class": 'c-card'})
    video_page_urls = []
    for el in pre_video_page_urls:
        video_page_urls.append('https://ufc.ru' + el['href'])

    video_urls = []
    for el in video_page_urls:
        html_code = str(urlopen(el).read(),'utf-8')
        soup = BeautifulSoup(html_code, "html.parser")
        inner_soup = soup.find('div', {"class": 'video-embed-field-provider-youtube'})
        pre_video_url = inner_soup.find('iframe')['src']
        video_urls.append(pre_video_url[:pre_video_url.find('?')])

    video_list = zip(headers, video_urls)
    
    my_list = [i+1 for i in range(int(video_total))]
    paginator = Paginator(my_list, len(video_urls))
    page_num = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, "news/video_list.html", {'video_list': video_list, 'page_obj': page_obj})


def contacts(request):
    return render(request, 'news/Contact.html')