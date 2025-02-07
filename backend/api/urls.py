from api import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', ServiceGetCreate.as_view()),
    path('<int:pk>', ServiceUpdateDelete.as_view()),
]
