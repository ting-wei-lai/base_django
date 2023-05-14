from django.contrib import admin

# Register your models here.
# 后台要显示的内容
from user.models import Tags, User, Book, Comment, Rate


class UserAdmin(admin.ModelAdmin):  # 用户管理
    # 设置模型 字段，用于admin后台数据表头设置，下同
    list_display = ("username", "password", "name", "address", "email")
    # 设置可搜索的字段并在admin后台数据生成搜索框，有外键应该用双下画线连接两个模型的字段
    search_fields = ("username", "name", "address")

class BookAdmin(admin.ModelAdmin):  # 书籍管理
    list_display = ("title", "author","book_star","book_pl","book_date")
    search_fields = ("title", "author")
    #list_filter = ("title","author")

class RateAdmin(admin.ModelAdmin):  # 评分管理
    list_display = ("book","mark","user")
    # 设置过滤器，在后台数据的右侧生成导航栏，有外键应该用双下画线连接两个模型的字段
    list_filter = ("book","mark","user")

admin.site.register(Tags)   # 此处，模型Tags直接注册到admin后台
"""此处通过自定义模型User，Book，Rate继承ModelAdmin"""
admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Rate,RateAdmin)
admin.site.register(Comment)    # 此处，模型Tags直接注册到admin后台

'''方法一：用python装饰器把自定义类和模型类绑定并注册到后台 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):  # 用户管理
    # 设置模型 字段，用于admin后台数据表头设置，下同
    list_display = ("username", "password", "name", "address", "email")
    # 设置可搜索的字段并在admin后台数据生成搜索框，有外键应该用双下画线连接两个模型的字段
    search_fields = ("username", "name", "address")'''
