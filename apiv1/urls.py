from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

reading_endpoint = 'readings/'
file_endpoint = 'files/'
analytics_endpoint = 'analytics/'
ques_endpoint = 'ques/'
urlpatterns = [
    # sensor readings
	path(reading_endpoint + 'insert/', views.insert ,name='insert'),
	path(reading_endpoint + 'upload_readings/', views.SensorReadingFileView.as_view() ,name='upload_readings'),
	path(reading_endpoint + 'upload_zip/', views.SensorReadingUnzip.as_view() ,name='upload_zip'),
	path(reading_endpoint + 'query_readings_file/', views.ReadingQueryView.as_view() ,name='query_readings_file'),
	# files
	path(file_endpoint + 'upload/', views.FileView.as_view() ,name='upload'),
	path(file_endpoint + 'files/<int:pk>', views.FileMethods.as_view(), name='file_methods'),
	# analytics
	path(analytics_endpoint + 'insert_analytics/', views.insert_analytics ,name='insert_analytics'),
	# questionnaires/notifications
	path(ques_endpoint +'response', views.ResponsesView.as_view(), name='upload_response'),
	path(ques_endpoint +'response/<int:pk>', views.ResponsesMethods.as_view(), name='response_methods'),
	path(ques_endpoint +'notif', views.QuestionnaireView.as_view(), name='upload_questionnaire'),	 	
	path(ques_endpoint +'notif/<int:pk>', views.QuestionnaireMethods.as_view(), name='questionnaire_methods'),	 
]
urlpatterns = format_suffix_patterns(urlpatterns) # in order to accept URLS like "/entry-details/2.json" or "/entry-details/2.api" or "/entry-list.json"
