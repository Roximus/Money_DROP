from django.db import models

# Create your models here.




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_a = models.CharField(max_length=200)
    answer_b = models.CharField(max_length=200)
    answer_c = models.CharField(max_length=200)
    answer_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)
    order = models.IntegerField()
    
    
    def __str__(self):
        return self.question_text


class GameSession(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    current_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    # other fields like players, scores, etc.
    duration = models.PositiveIntegerField(default=300)