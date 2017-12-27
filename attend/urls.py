from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


app_name = 'attend'
urlpatterns = [
    # login/
    url(r'^$', login, {'template_name': 'attend/index.html'}),
    #login/profile
    url(r'^profile/$', views.feed, name='profile'),

    url(r'^signup/$', views.signup, name='signUp-form'),


]


