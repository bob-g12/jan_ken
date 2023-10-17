from django.urls import path
from jan_ken_app.views import frontpage
from jan_ken_app.views import drawpage , winpage , losepage

urlpatterns = [
    path("",frontpage), #パスを指定しなかった場合frontpageに誘導される
    path('draw.html',drawpage),
    path('win.html',winpage),
    path('lose.html',losepage),
    path('lady.html',frontpage),
]