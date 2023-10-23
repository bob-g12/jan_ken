from django.urls import path, include
from jan_ken_app.views import frontpage
from jan_ken_app.views import judgpage
from . import views

urlpatterns = [
    path("",frontpage), #パスを指定しなかった場合frontpageに誘導される
    path('draw.html',judgpage),
    path('win.html',judgpage),
    path('lose.html',judgpage),
    path('lady.html',frontpage),
    path('accounts/',include("accounts.urls")),
    #path('', views.AccountRegistration.as_view(), name='register'),
]