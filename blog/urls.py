from django.conf.urls import url

from .views import (post_model_list_view, post_model_create_view,)

urlpatterns = [
    url(r'^$', post_model_list_view, name='list'),
    url(r'^create/$', post_model_create_view, name='create'),
]
