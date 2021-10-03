"""StackOverflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from . models import User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('',views.homepage, name = 'homepage'),
    path('SignUp/',views.SignUp, name = 'SignUp'),
    path('SignIn', views.SignIn, name='SignIn'),
    path('SignOut', views.SignOut, name='SingOut'),
    path('<int:id>/question_detail', views.question_detail, name = 'question_detail'),
    path('ask_question', views.ask_question , name = "ask_ques"),
    path('my_ques', views.my_ques, name = 'my_ques'),
    path('<int:id>/<int:q>/upvote_ans', views.upvote_ans, name = 'upvote_ans'),
    path('<int:id>/upvote_ques' , views.upvote_ques, name = 'upvote_ques'),
    path('<int:id>/unupvote_ques' , views.unupvote_ques, name = 'unupvote_ques'),
    path('<int:id>/<int:q>/unupvote_ans', views.unupvote_ans, name = 'unupvote_ans'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)


    