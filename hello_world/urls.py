from django.urls import path
from hello_world import views

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    #path('', views.about_company, name='about_company'), was fixed by VL
    path('about_company/', views.about_company, name='about_company'),
    path('news/', views.news, name='news'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('our_team/', views.our_team, name='our_team'),
]
