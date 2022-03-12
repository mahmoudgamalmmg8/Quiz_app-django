from __future__ import division
from operator import truediv
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#
divisions =(
    ('Graphic Department','Graphic Department'),
    ('Network and IT Department','Network and IT Department'),
)
class CustomUserStudent(AbstractUser):
    division = models.CharField(max_length=30 , choices = divisions)
    custom_student_id = models.PositiveBigIntegerField(null=True)## this id not related to any thing in django local db
