from django.urls import path, re_path
from . import views, admin
from .views import PicDetail,PicUpload,PicList


app_name = 'MytestApp'
urlpatterns = [
    path('', PicList.as_view(), name='pic_list'),
    re_path(r'^pic/(?P<pk>\d+)/$', PicDetail.as_view(), name='pic_detail'),
    # path('pic_upload/', views.PicUpload.as_view(), name='pic_upload'),
    re_path(r'^pic/upload/$', PicUpload.as_view(), name='pic_upload'),
]
