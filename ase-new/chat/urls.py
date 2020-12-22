from django.urls import path, include
from . import views
from django.conf.urls import url
from . import views
urlpatterns=[
    path('chat',views.messager,name='chat'),
    path('chatview/<str:userid>',views.MsgView,name='msgview'),
    path('list',views.listmsg,name='listmsg')
]