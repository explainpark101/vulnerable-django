from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from .models import Article

def dictfetchall(cursor):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]

def articleList(request):
    context = {}
    context['articles'] = Article.objects.all().order_by("-id")

    return render(request, "list.html", context)

def detail(request, article_id):
    context = {}
    # context["article"] = get_object_or_404(Article, pk=article_id)
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT *
    FROM "board_article"
    WHERE "board_article"."id"={article_id}
    """)
    context["article"] = dictfetchall(cursor)[0]


    return render(request, "detail.html", context)


def create(request):
    context = {}
    if request.method == "POST":
        article = Article(title=request.POST.get("title"), content=request.POST.get("content"))
        article.save()
        return redirect('article list')

    return render(request, "create.html", context)