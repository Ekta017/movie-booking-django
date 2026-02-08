from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Booking
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum, Count
from django.core.mail import send_mail
from django.conf import settings


# --- Task 1: Movie Listing with Filters & Search ---
def index(request):
    # Retrieve query parameters from the URL
    genre = request.GET.get('genre')
    lang = request.GET.get('language')
    search = request.GET.get('search')

    # Start with all movies
    movies = Movie.objects.all()

    # Apply filters based on user input
    if genre:
        movies = movies.filter(genre=genre)
    if lang:
        movies = movies.filter(language=lang)
    if search:
        movies = movies.filter(title__icontains=search)

    return render(request, 'bookings/index.html', {'movies': movies})


# --- Task 2: Movie Detail & Trailer ---
def movie_detail(request, movie_id):
    # Fetch the movie or return a 404 error if not found
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'bookings/detail.html', {'movie': movie})


# --- Task 3, 4 & 5: Booking Logic & Timeout ---
def process_booking(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_id)
        email = request.POST.get('email')

        # Task 5: Seat Reservation Timeout Logic
        # First, clean up any expired pending bookings (older than 5 mins)
        expiration_limit = timezone.now() - timedelta(minutes=5)
        Booking.objects.filter(status='PENDING', created_at__lt=expiration_limit).delete()

        # Create the new booking
        booking = Booking.objects.create(
            movie=movie,
            user_email=email,
            status='PAID'  # Marking as PAID for this simplified flow
        )

        # Task 2: Send Confirmation Email
        try:
            subject = f"🎬 Ticket Confirmed: {movie.title}"
            message = f"Hi,\n\nYour booking for {movie.title} is confirmed!\nBooking ID: #CINE-{booking.id}\nPrice: ₹{movie.price}\n\nEnjoy your movie!"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email failed to send: {e}")

        return redirect('payment_success', booking_id=booking.id)


# --- Success Page ---
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/success.html', {'booking': booking})


# --- Task 6: Admin Analytics Dashboard ---
def admin_dashboard(request):
    # Task 6: Calculate total revenue from paid bookings
    total_revenue = Booking.objects.filter(status='PAID').aggregate(Sum('movie__price'))['movie__price__sum'] or 0

    # Task 6: Get statistics per movie
    movie_stats = Movie.objects.annotate(ticket_count=Count('booking')).all()

    context = {
        'revenue': total_revenue,
        'stats': movie_stats
    }
    return render(request, 'bookings/admin.html', context)

from .models import Movie
from django.shortcuts import render

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})
