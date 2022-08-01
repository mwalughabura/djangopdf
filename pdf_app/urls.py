from django.contrib import admin
from .views import generatePDF

urlpatterns = [
    path('generatePDF/', views.generatePDF, name='generatePDF'),
]
