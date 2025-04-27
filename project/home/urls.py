from django.urls import path
from project.home.views import index, idphoto_form

app_name = 'idphoto'


urlpatterns = [
    path('', index, name='home'),
    path('idphoto/', idphoto_form, name='idphoto'),
]