"""Session_Cookies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    ## cookies
    # path('sc/',views.setcookie, name = 'sc'),           # set url for coockie
    path('home/',views.homepage,name = 'home'),
    path('gc/',views.get_cookies,name = 'gc'),
    path('dc/',views.delete_cookies,name='dc' ),
    path('sc1/',views.set_cookie1,name = 'sc1'),

    ## Session
    path('testcookie/',views.cookie_session,name='testcookie'),
    path('deletecookie/',views.cookie_delete,name = 'deletecookie'),
    path('demoview/',views.demo_view),
    path('create/',views.create_session),
    path('show-session/',views.show_session_data, name = 'show_session'),
    path('delee-session/', views.delete_session, name = 'deletesession'),
]
