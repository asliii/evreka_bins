from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('get_collection_frequencies', views.get_collection_frequencies, name='get_collection_frequencies')
]
