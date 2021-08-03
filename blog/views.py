from django.core.paginator import Paginator
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
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print('page param:', page)
    all_articles = Article.objects.all()
    latest10_article_list = Article.objects.order_by('-publish_date')[:10]

    paginator = Paginator(all_articles, 6)
    page_num = paginator.num_pages
    print('page num:', paginator.num_pages)
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    return render(request, 'index.html',
                  {'article_list': page_article_list, 'page_num': range(1, page_num + 1), 'curr_page': page,
                   'next_page': next_page, 'previous_page': previous_page,
                   'latest10_article_list': latest10_article_list})


def get_detail_page(request, article_id):
    all_articles = Article.objects.all()
    curr_article = None
    previous_article = None
    next_article = None
    previous_index = 0
    next_index = 0
    for index, article in enumerate(all_articles):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_articles) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_articles[previous_index]
            next_article = all_articles[next_index]
            break
    section_list = curr_article.content.split('\n')

    return render(request, 'detail.html',
                  {'curr_article': curr_article, 'section_list': section_list, 'previous_article': previous_article,
                   'next_article': next_article})
