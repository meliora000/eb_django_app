from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^favorite/',views.index,name="login"),
]