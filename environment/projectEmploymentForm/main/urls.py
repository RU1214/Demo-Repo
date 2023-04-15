from django.urls import path
from .views import employmentFormPageView
 
urlpatterns = [
	path("", employmentFormPageView, name="form")
] 
