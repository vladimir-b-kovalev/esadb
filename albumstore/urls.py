from django.urls import path

from albumstore import views

appname = 'albumstore'

urlpatterns = [
    path('', views.AlbumListView.as_view(), name = 'imgalbumlib'),
    path('detail/', views.albumdetail, name = 'detail'),
    path('detail/loadimage', views.albumloadimage, name = 'loadimage'),
    path('detail/deleteimage', views.albumdeleteimage, name = 'deleteimage'),
    path('create/', views.albumcreate, name = 'create'),
    path('update/', views.albumupdate, name = 'update'),
    path('delete/', views.albumdelete, name = 'delete')
]