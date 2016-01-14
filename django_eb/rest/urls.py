from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'search/(\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)/$',views.index,name="restsearch"),
]