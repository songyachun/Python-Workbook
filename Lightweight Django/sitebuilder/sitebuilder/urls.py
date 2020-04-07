from django.urls import path,re_path
from .views import page

urlpatterns = [
    path('',page,name='homepage'),
    re_path(r'(?P<slug>[\w./-]+)/',page,name='page'),
]
