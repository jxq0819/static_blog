from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


def hello_world(request):
    return HttpResponse("Hello World")


def article_content(request):
    article = Article.objects.all()[0]
    article_id = article.article_id
    title = article.title
    brief_content = article.brief_content
    content = article.content
    publish_date = article.publish_date
    return_str = "title: %s, brief_content: %s, content: %s, article_id: %s, publish_date: %s" % (
        title, brief_content, content, article_id, publish_date)

    return HttpResponse(return_str)


def get_index_page(request):
    all_articles = Article.objects.all()
    return render(request, 'index.html', {'article_list': all_articles})
