from django.urls import path , include
from . import views
from jan_ken_app.views import frontpage
urlpatterns = [
    #アカウント管理のパス
    path('',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("home",views.home,name="home"),
    path('ready.html',include('jan_ken_app.urls')),
]