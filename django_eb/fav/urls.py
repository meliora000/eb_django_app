from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="login"),
    url(r'^post/',views.fpost,name="addfavorite"),
]