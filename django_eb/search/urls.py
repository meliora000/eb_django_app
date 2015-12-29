from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^search/',views.search,name="search"),
    url(r'^daum/',views.map,name="map"),
    url(r'url/',views.login,name="login")
]