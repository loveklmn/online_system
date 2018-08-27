from django.conf.urls import url
from vron import views
from rest_framework.authtoken import views as token_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^books/$',
        views.BookList.as_view()),
    url(r'^books/(\d+)/guidance/$',
        views.BookGuidance.as_view(), name='guidance'),
    url(r'^books/(\d+)/ebook/$',
        views.BookEbook.as_view(), name='ebook'),
    url(r'^books/(\d+)/progress/$',
        views.BookProgress.as_view(), name='progress'),
    url(r'^books/(\d+)/homework/$',
        views.BookHomework.as_view(), name='homework'),
    url(r'^community/$',
        views.CommunityGroup.as_view(), name='community_group'),
    url(r'^upload/$',
        views.UploadFile.as_view(), name='upload'),
    url(r'^userinfo/$',
        views.UserInfo.as_view(), name='userinfo'),
    url(r'^userinfo/change-password/$',
        views.ChangePassword.as_view(), name='change_password'),
    url(r'^userinfo/level/$',
        views.UserLevel.as_view()),
    url(r'^userinfo/level/update/$',
        views.UserLevelUpdate.as_view()),
    url(r'^ranklist/$',
        views.RankList.as_view(), name='ranklist'),
    url(r'^notices/$',
        views.NoticeInfo.as_view(), name='notice_info'),
    url(r'^notices/readed/$',
        views.MarkNotice.as_view(), name='notice_readed'),
    url(r'^students/$',
        views.StudentList.as_view(), name='student_list'),
    url(r'^generatekey/$',
        views.KeyGenerator.as_view(), name='key_generator'),
    #auth
    url(r'^register/$',
        views.register_view, name='register'),
    url(r'^get-token/$',
        token_views.obtain_auth_token),
    url(r'^manager-token/$',
        views.manager_token),
] + static(settings.MEDIA_URL,
             document_root=settings.MEDIA_ROOT)
