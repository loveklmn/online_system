from django.conf.urls import url
from vron import views
from rest_framework.authtoken import views as token_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^books/$', views.BookList.as_view()),
    url(r'^books/(\d+)/guidance/$', views.BookGuidance.as_view(), name='guidance'),
    url(r'^books/(\d+)/ebook/$', views.BookEbook.as_view(), name='ebook'),
    url(r'^books/(\d+)/progress/$', views.BookProgress.as_view(), name='progress'),
    url(r'^books/(\d+)/homework/$', views.BookHomework.as_view(), name='homework'),
    url(r'^community/$', views.CommunityGroup.as_view(), name='community_group'),
    url(r'^upload/$', views.UploadFile.as_view(), name='upload'),
    url(r'^userinfo/$', views.UserInfo.as_view(), name='userinfo'),
    #auth
    url(r'^get-token/$', token_views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
