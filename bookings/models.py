from django.db import models
from django.utils import timezone
from datetime import timedelta

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    trailer_id = models.CharField(max_length=100) # YouTube Video ID
    price = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)

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