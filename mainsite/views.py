from django.shortcuts import render
from datetime import datetime
from .models import Article
from newsapi import NewsApiClient

def index(request):
    context={
        'current_date':datetime.now(),
        'title':'Home'
    }
    return render(request,'index.html',context)

def about(request):
    context={
        'current_date':datetime.now(),
        'title':'About'
    }
    return render(request,'about.html',context)

def news(request):


    articles = populate_db()
    #get_articles()
    context={
        'articles':articles,
        'current_date':datetime.now(),
        'title':'News'
    }
    return render(request,'news.html',context)

def get_articles():
    result=Article.objects.all()
    return result

def populate_db():

    #if(Article.objects.count()>=100):
    #    Article.objects.all().delete()
        
    n = NewsApiClient(api_key='f52949219e43497581e433887d68f404')
    news = n.get_top_headlines(sources='techcrunch')
    l=news['articles']
    article_no = []
    title = []
    content = []
    image_url = []
    for i in range(len(l)):
        article_no.append(i+1)
        title.append(l[i]['title'])
        content.append(l[i]['description'])
        image_url.append(l[i]['urlToImage'])
    
    return zip(article_no,title,content,image_url)
    '''if(Article.objects.count()==0):
    Article(title='first item',content='this first item in db').save()
    Article(title='second item',content='this second item in db').save()
    Article(title='third item',content='this third item in db').save()
    '''