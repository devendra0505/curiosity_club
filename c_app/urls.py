from django.conf.urls import url
from c_app import views

app_name = 'c_app'

urlpatterns = [
    url(r'^$', views.about_page, name = 'about_page'),
    url(r'^join', views.join_page, name = 'join_page'),
    url(r'^front/', views.front_page, name = 'front_page'),
    url(r'^event', views.event_page, name = 'event_page'),
    url(r'^mem', views.member_page, name = 'member_page'),

]
