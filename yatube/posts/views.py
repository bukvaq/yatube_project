from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
# одна строка вместо тысячи слов на SQL
    latest = Post.objects.order_by('-pub_date')[:10]
    # собираем тексты постов в один, разделяя новой строкой
    return render(request, "index.html", {"posts":latest}) 