from asyncio import mixins
from multiprocessing import context
from unittest import result
from urllib import request
from django.views.generic.list import ListView
from .models import Result
from django.contrib.auth.models import User
from accounts.models import CustomUserStudent
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
class UserScore(LoginRequiredMixin,ListView):
    model = Result 
    template_name = 'score.html'
    context_object_name = 'score'
    def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context["score"] = context["score"].filter(user = self.request.user).order_by('-score')
                return context