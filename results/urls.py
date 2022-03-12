from django.urls import path
from .views import UserScore
app_name="results"
urlpatterns = [
    path('',UserScore.as_view(),name="results_data"),
]
