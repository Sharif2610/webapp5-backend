from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('register/',views.register_task),
    path('login/',obtain_auth_token),
    path('tasks/',views.task_list_create),
    path('update_task/<int:id>/',views.update_tasks),
]