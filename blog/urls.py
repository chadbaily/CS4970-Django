from django.urls import path

from .views import post_model_lsit_view

app_name = 'blog'


urlpatterns = [
    url(r'^$', post_model_list_view, name='list'),
]
