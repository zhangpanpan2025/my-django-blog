from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    # 文章标题 - CharField用于存储较短文本
    title = models.CharField(max_length=200, verbose_name='标题')

    # 文章内容 - TextField用于存储长文本
    content = models.TextField(verbose_name='内容')
    
    #作者 - ForeignKey表示"多对一"关系，一篇文章属于一个用户
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    
    # 创建时间 - auto_now_add=True表示创建时自动设置时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    # 更新时间 - auto_now=True表示每次保存时自动更新时间为当前时间
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    def __str__(self):
        """定义对象的字符串表示形式，在后台管理界面显示"""
        return self.title
    
    class Meta:
        """模型的元数据配置"""
        verbose_name = '文章'          # 单数名称        
        verbose_name_plural = '文章'   # 复数名称