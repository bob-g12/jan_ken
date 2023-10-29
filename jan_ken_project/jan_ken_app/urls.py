from django.urls import path
from jan_ken_app.views import frontpage
from jan_ken_app.views import judgpage
from . import views

urlpatterns = [
    #path("",frontpage), #パスを指定しなかった場合frontpageに誘導される
    path('ready.html',frontpage,name="frontpage"),
    path('draw.html',judgpage),
    path('win.html',judgpage),
    path('lose.html',judgpage),
]
