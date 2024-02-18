from django.urls import path
from .views import receive_data_from_js, renderView

urlpatterns = [
    path('frontend/', renderView, name='render'),
    path('backend/', receive_data_from_js, name='receive_data_from_js')
]