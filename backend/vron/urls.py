from django.conf.urls import url
from vron import views

urlpatterns = [
    url(r'^books/$', views.book_list),
    url(r'^login/$', views.login, name='login'),
    url(r'^books/(\d+)/guidance/$', views.book_guidance, name='guidance')
]
