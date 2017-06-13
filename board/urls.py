from django.conf.urls import url

from . import views


app_name = 'board'
urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^(?P<board_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        ]
