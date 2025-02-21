from django.urls import path
from .views import *

urlpatterns = [
    path('service/', ServiceGetCreate.as_view()),
    path('service/<int:pk>', ServiceUpdateDelete.as_view()),
    path('category/', CategoryGetCreate.as_view()),
    path('category/<int:pk>', CategoryUpdateDelete.as_view()),
]
