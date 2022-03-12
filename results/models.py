from django.db import models
from quizz.models import Quiz
from django.contrib.auth.models import User
from accounts.models import CustomUserStudent
# Create your models here.
class Result(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUserStudent,on_delete=models.CASCADE)
    score = models.FloatField()
    def __str__(self):
        return f"{self.score}-{self.user}--{self.quiz}"
