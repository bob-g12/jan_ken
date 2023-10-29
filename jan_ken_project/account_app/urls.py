from django.urls import path
from . import views
from jan_ken_app.views import frontpage,judgpage
urlpatterns = [
    #アカウント管理のパス
    path('',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("home",views.home,name="home"),
    path('ready.html',frontpage,name="frontpage"),
    path('draw.html',judgpage),
    path('win.html',judgpage),
    path('lose.html',judgpage),
]