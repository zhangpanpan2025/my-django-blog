from django.shortcuts import render
from .models import Article

def article_list(request):
    #获取所有文章，按创建时间倒序排列
    articles=Article.objects.all().order_by('-created_time')
    return render(request,'blog/article_list.html',{'articles':articles})

