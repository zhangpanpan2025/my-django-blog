from django.contrib import admin
from .models import Article

# 注册Article模型到后台
admin.site.register(Article)