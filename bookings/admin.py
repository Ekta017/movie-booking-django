# from django.contrib import admin
# from .models import Movie, Booking
#
# admin.site.register(Movie)
# admin.site.register(Booking)

from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'duration')
