from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='events'
    )
    title = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date", "start_time"]
        # ordering = ["-date", "start_time"]) --if newest date


    def __str__(self):
        # Team Meeting (2026-01-15 09:00:00-10:00:00)
        return f"{self.title} ({self.date} {self.start_time}-{self.end_time})"


    