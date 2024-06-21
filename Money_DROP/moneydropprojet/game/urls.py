from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('start/', views.start_game, name='start'),
    path('question/<int:game_session_id>/', views.show_question, name='question'),
    path('submit/<int:game_session_id>/', views.submit_answer, name='submit'),
    path('end/', views.end_game, name='end_game'),
    path('', views.home, name='home'),
]
