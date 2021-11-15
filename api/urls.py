from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    # path('', views.apiOverview, name="api-overview"),
	path('insert/', views.insert ,name='insert'),
	path('insert_analytics/', views.insert_analytics ,name='insert_analytics'),
	path('upload/', views.FileView.as_view() ,name='upload'),
	path('upload_readings/', views.SensorReadingFileView.as_view() ,name='upload_readings'),	
]
urlpatterns = format_suffix_patterns(urlpatterns) # in order to accept URLS like "/entry-details/2.json" or "/entry-details/2.api" or "/entry-list.json"
