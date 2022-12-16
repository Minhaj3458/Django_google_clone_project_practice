from django.urls import path
app_name = 'GoogleApp'
from  .import views
urlpatterns = [
  path('', views.Index, name='Index'),
  path('Search', views.Search, name='Search')
]
