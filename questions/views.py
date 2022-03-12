from re import template
from django.shortcuts import render
from .models import Answer,Question
from django.views.generic import ListView
# Create your views here.
class QuestionListView(ListView):
    model = Question
    template_name = "quiz.html"
    context_object_name = "questions"

class AnswersListView(ListView):
    model = Answer
    template_name = "quiz.html"
    context_object_name = "answers"