from django.conf.urls import url

from .views import list_view, detail_view

urlpatterns = [
    url(r'^(?P<app_label>.*)/(?P<model_name>.*)/(?P<pk>.*)/',
        detail_view,
        name='detail-view'),
    url(r'^(?P<app_label>.*)/(?P<model_name>.*)/',
        list_view,
        name='list-view'),

]
