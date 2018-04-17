from django.conf.urls import url
from . import views

app_name="User"

urlpatterns = [
    url(r'^profile', views.profile, name="profile"),
    url(r'^edit', views.edit, name="edit"),
    url(r'^delete', views.delete, name="delete"),
    url(r'^note/(?P<user_id>\d+)/$', views.note, name="note"),
    url(r'^userComment/(?P<user_id>\d+)/(?P<message_id>\d+)*$', views.comment, name='userComment'),
    url(r'^userDeleteMessage/(?P<user_id>\d+)/(?P<message_id>\d+)/$', views.deleteMessage, name="userDeleteMessage"),
    url(r'^userDeleteComment/(?P<user_id>\d+)/(?P<comment_id>\d+)/$', views.deleteComment, name="userDeleteComment"),
    url(r'^users/show/(?P<user_id>\d+)/$', views.show_user, name='show_user'),
]
