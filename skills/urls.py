from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getskills/all/', views.getskills, name='getskills'),
    url(r'^getskills/red/', views.getredskills, name='getredskills'),
    url(r'^getskills/yellow/', views.getyellowskills, name='getyellowskills'),
    url(r'^getskills/blue/', views.getblueskills, name='getblueskills'),
    url(r'^getskills/green/', views.getgreenskills, name='getgreenskills')
]
