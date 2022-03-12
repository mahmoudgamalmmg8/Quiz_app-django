from django.db import models
import random

subjects = (
    ('php', 'php'),
    ('asp.net', 'asp.net'),
    ('java', 'java'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    subject = models.CharField(max_length=50, choices=subjects)
    total = models.PositiveIntegerField()
    def __str__(self):
        return f"quiz name :  {self.name} / topic: {self.topic} / Total grade: {self.total} / Subject:  {self.subject}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'