from django.urls import path
from api.views import user_all


app_name = 'api'

urlpatterns = [
    path('user_all/', user_all),
]
