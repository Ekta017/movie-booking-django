from django.db import models
from django.utils import timezone
from datetime import timedelta

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    # FIXED: Replaced 'on_submit' with 'on_delete=models.CASCADE'
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) 
    user_email = models.EmailField()
    status = models.CharField(max_length=20, default='PENDING') # PENDING, PAID, EXPIRED
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        # Task 5: Check if 5 minutes have passed since reservation
        return timezone.now() > self.created_at + timedelta(minutes=5)

    def __str__(self):
        return f"{self.user_email} - {self.movie.title}"