from django.conf.urls import url
from . import views

app_name="LogReg"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^1$', views.index1, name="index1"),
    # url(r'^2$', views.index2, name="index2"),
    # url(r'^3$', views.index3, name="index3"),
    url(r'^login', views.log_reg, name="login"),
    url(r'^register', views.log_reg, name="register"),
    url(r'^logout', views.logout, name="logout"),
]
