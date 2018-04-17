from django.conf.urls import url
from . import views

app_name="Wall"

urlpatterns = [
    url(r'^wall', views.wall, name="wall"),
    url(r'^message', views.message, name="message"),
    url(r'^comment/(?P<message_id>\d+)*$', views.comment, name='comment'),
    url(r'^deleteMessage/(?P<message_id>\d+)/$', views.deleteMessage, name="deleteMessage"),
    url(r'^deleteComment/(?P<comment_id>\d+)/$', views.deleteComment, name="deleteComment"),
    # url(r'^users/show/(?P<user_id>\d+)/$', views.show_user, name='show_user'),
]
