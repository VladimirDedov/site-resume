from django.urls import path, include
from .views import *
urlpatterns = [
    path('', ViewIndex.as_view(), name='index'),
    path('redirect/', send_form, name='name_send_form'),
]