from django.urls import path

from . import views as edt_views

urlpatterns = [
    path('', edt_views.index, name='index'),
]
