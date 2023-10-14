from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls), #パスをadminに指定するとadmin.site.urlsに誘導される
    path("",frontpage), #パスを指定しなかった場合frontpageに誘導される
]
