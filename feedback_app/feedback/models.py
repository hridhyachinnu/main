from django.db import models
from django.db import models
from django.db import models

class InternFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    supervisor_name = models.CharField(max_length=100, blank=True)
    experience_rating = models.CharField(max_length=20)
    skills_learned = models.TextField()
    overall_satisfaction = models.IntegerField()
    suggestions = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"
