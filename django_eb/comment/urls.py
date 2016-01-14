from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="test"),
    url(r'^post/$',views.post,name="postcomment")
]
