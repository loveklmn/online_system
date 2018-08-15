from django.conf.urls import url
from vron import views
from rest_framework.authtoken import views as token_views

urlpatterns = [
    url(r'^books/$', views.book_list),
    url(r'^books/(\d+)/guidance/$', views.book_guidance, name='guidance'),
    url(r'^books/(\d+)/ebook/$', views.book_ebook, name='ebook'),
    url(r'^community/(\d+)/$', views.community_group, name='community_group'),
    #auth
    url(r'^get-token/', token_views.obtain_auth_token),
]
