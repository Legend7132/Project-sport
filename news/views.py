from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from dateutil.parser import isoparse
from newsapi import NewsApiClient
from googleapiclient.discovery import build


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


def video_list(request):
    youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')
    youtube_request = youtube.search().list(part='id,snippet', channelId='UCU8bQExxd38i-mnn-GLOtfA', type = 'video', maxResults=50, order = 'date', videoEmbeddable = 'true')
    response = youtube_request.execute()
    video_list = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_header = item['snippet']['title']
        video_list.append([video_id, video_header])

    paginator = Paginator(video_list, 10)
    page_num = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, "news/video_list.html", {'page_obj': page_obj})


def contacts(request):
    return render(request, 'news/Contact.html')