from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.movie_detail, name='detail'),
    path('book/<int:movie_id>/', views.process_booking, name='process_booking'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('success/<int:booking_id>/', views.payment_success, name='payment_success'),
]