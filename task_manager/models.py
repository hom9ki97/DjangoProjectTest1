from django.utils import timezone

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def mark_as_completed(self):
        self.is_completed = True
        self.completed_at = timezone.now()
        self.save()

    def mark_as_incomplete(self):
        self.is_completed = False
        self.completed_at = None
        self.save()
