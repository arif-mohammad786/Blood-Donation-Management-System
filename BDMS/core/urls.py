
from django.urls import path
from . import views
urlpatterns = [
    path('about/',views.about,name="about"),
    path('whydonar/',views.whydonar,name="whydonar"),
    path('becomedonar/',views.become_donar,name="becomedonar"),
    path('searchdonar/',views.searchdonar,name="searchdonar"),
    path('contact/',views.contact,name="contact"),

]