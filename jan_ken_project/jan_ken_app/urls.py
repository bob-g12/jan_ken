from django.urls import path
from jan_ken_app.views import frontpage
from jan_ken_app.views import drawpage , winpage , losepage
import random
judgment = [drawpage,winpage,losepage]
def random_def(low,high):
    print (judgment[random.randint(low,high)])
urlpatterns = [
    path("",frontpage), #パスを指定しなかった場合frontpageに誘導される
    path('draw.html',judgment[random.randint(0,2)]),
    path('win.html',judgment[random.randint(0,2)]),
    path('lose.html',judgment[random.randint(0,2)]),
    path('lady.html',frontpage),
]