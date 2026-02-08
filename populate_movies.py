from bookings.models import Movie
from django.core.files import File

def assign_posters():
    posters = {
        "Inception": "media/posters/inception.jpg",
        "Interstellar": "media/posters/interstellar.jpg",
        "RRR": "media/posters/rrr.jpg",
        "The Dark Knight": "media/posters/dark_knight.jpg",
        "Parasite": "media/posters/parasite.jpg",
    }

    for movie in Movie.objects.all():
        if movie.title in posters:
            with open(posters[movie.title], "rb") as f:
                movie.poster.save(posters[movie.title], File(f), save=True)

assign_posters()
