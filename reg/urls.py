from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^student/$',views.student, name='student'),
	url(r'^viewdata/$',views.viewdata, name='viewdata'),
	url(r'^viewresult/$',views.viewresult, name='viewresult'),
	url(r'^candidate/$',views.candidate, name='candidate'),
    url(r'^party/$',views.party, name='party'),
    url(r'^college/$',views.college, name='college'),
    url(r'^post/$',views.post, name='post'),
    url(r'^election/$', views.election, name='election'),

]