from django.conf.urls import url 
from django.urls import path
from apis import views 


urlpatterns = [
    path('', views.index, name='index'),
]

