from django.contrib import admin
from django.urls import path
from menus import views

urlpatterns = [
    path('', views.index_view, name='index'), # 이해가 안돼... 물어보기
]