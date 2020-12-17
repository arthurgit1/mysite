import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text

class Question(models.Model):
    # ...
    def was_published_recently(self):
         now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

