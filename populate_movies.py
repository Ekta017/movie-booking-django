import os
import django

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()

from bookings.models import Movie

def add_movies():
    movie_list = [
        {"title": "Inception", "genre": "Sci-Fi", "language": "English", "trailer_id": "YoHD9XEInc0", "price": 450},
        {"title": "The Dark Knight", "genre": "Action", "language": "English", "trailer_id": "EXeTwQWaywY", "price": 500},
        {"title": "RRR", "genre": "Action", "language": "Hindi", "trailer_id": "NgBoMJy386M", "price": 400},
        {"title": "Interstellar", "genre": "Sci-Fi", "language": "English", "trailer_id": "zSWdZVtXT7E", "price": 550},
        {"title": "Parasite", "genre": "Thriller", "language": "Korean", "trailer_id": "5xH0HfJH963", "price": 350},
    ]

    for m in movie_list:
        # get_or_create prevents duplicate entries if you run the script twice
        obj, created = Movie.objects.get_or_create(**m)
        if created:
            print(f"Added: {m['title']}")
        else:
            print(f"Already exists: {m['title']}")

if __name__ == '__main__':
    add_movies()