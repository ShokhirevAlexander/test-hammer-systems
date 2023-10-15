from django.urls import path
from .views import index, register_view, verified_view, profile_view, invite_referral, logout


app_name = 'accounts'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register_view, name='register'),
    path('verified/', verified_view, name='verified'),
    path('profile/', profile_view, name='profile'),
    path('page/<int:page_number>/', profile_view, name='paginator'),
    path('logout/', logout, name='logout'),
    path('invite/', invite_referral, name='invite'),
]
