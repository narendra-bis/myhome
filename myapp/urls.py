from django.conf.urls import url, include
from . import views
from django.views.generic import RedirectView

app_name = "myapp"

urlpatterns = [
    url(r'^$',views.myapphome, name='home'),
    url(r'myapp',RedirectView.as_view(pattern_name='myapp:home', permanent=True)),
    url(r'login',views.signin, name='login'),
    url(r'register',views.signup, name='signup'),
    url(r'logout',views.signout, name='logout')
   
]