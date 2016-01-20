from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/',views.login,name="login"),
    url(r'signup/',views.signUp,name="signup"),
    url(r'status/',views.status,name="status"),
    url(r'logout/',views.logout,name="logout"),
    url(r'check/',views.check,name="check")
]