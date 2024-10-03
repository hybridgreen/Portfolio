from django.urls import path, include
from . import views
app_name = 'pages'

urlpatterns = [
    path('', views.home , name = "home"),
    path('projects', views.projects, name = 'projects'),
    path('contact', views.contact, name = 'contact'),
    path('contact/submit' , views.contact_form),
]