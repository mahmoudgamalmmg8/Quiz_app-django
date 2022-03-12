from django.urls import path
from .views import QuestionListView,AnswersListView
app_name='questions'
urlpatterns = [
    path("<int:pk>/",QuestionListView.as_view(),name="question-list"),
    path("<int:pk>",AnswersListView.as_view(),name="answers-list"),

]
