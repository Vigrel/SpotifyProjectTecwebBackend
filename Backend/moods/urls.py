from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/moods/<int:mood_id>/', views.api_mood),
    path('api/moods/', views.api_mood),
    # Você possivelmente tem outras rotas aqui.
]