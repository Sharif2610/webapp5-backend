from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('register_book/',views.register_book),
    path('login_book/',obtain_auth_token),
    path('show/',views.show_api)
]