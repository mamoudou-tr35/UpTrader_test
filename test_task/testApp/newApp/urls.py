from django.conf.urls import url
from newApp.views import IndexView
from menuApp.views import menu_item

app_name = 'newApp'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(.*)/$', IndexView.as_view(), name='index'),
]