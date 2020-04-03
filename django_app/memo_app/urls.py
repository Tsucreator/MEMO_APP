from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:now_page>', views.index, name='index'),
    path('set_record_number', views.set_record_number, name='set_record_number'),
    path('post', views.post, name='post'),
]
