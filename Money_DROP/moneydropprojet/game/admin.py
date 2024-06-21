from django.contrib import admin
from .models import Question, GameSession

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'answer_a', 'answer_b', 'answer_c', 'answer_d', 'correct_answer')

@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'current_question')

