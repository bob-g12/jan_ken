from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls), #パスをadminに指定するとadmin.site.urlsに誘導される
    path("",include('jan_ken_app.urls')), #パスを指定しなかった場合frontpageに誘導される
]
