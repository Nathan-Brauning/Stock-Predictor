from django.urls import path
from .views import receive_data_from_js

urlpatterns = [
    path('/Users/james/Documents/GitHub/dataproj/backend.py', receive_data_from_js, name='receive_data_from_js'),
    # Add other URL patterns as needed
]