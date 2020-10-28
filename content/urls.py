from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcements, name='announcements'),
    path('announcements', views.announcements),
    path('aboutacm', views.aboutacm, name='aboutacm'),
    path('aboutmse', views.aboutmse, name='aboutmse'),
    path('officers', views.officers, name='officers'),
    path('conference', views.conference, name='conference'),
    path('pastcon/<slug>', views.pastyear),
    path('pastcon', views.pastcon, name='pastcon'),
    path('documents', views.documents, name='documents'),
]