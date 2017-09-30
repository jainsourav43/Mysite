from django.conf.urls import url
from django.contrib import admin
from .import views

app_name ='Mess'

urlpatterns = [
    url(r'^h/$',views.home,name='index'),
    url(r'^hi/$',views.oye,name='index'),
    url(r'^login_user/$',views.login_user,name='login_user'),
   	url(r'^adddata/$',views.adddata,name='adddata'),
   	url(r'^logout/',views.logout,name='logout')
   # url(r'^display/$',views.display,name='display'),
    # url(r'^index/$',views.index,name='index'),

]

