# game/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, GameSession


def home(request):
    return render(request, 'game/index.html')


def start_game(request):
    game_session = GameSession.objects.create()
    first_question = Question.objects.order_by('order').first()
    game_session.current_question = first_question
    game_session.save()
    return redirect('game:question', game_session_id=game_session.id)

def show_question(request, game_session_id):
    game_session = get_object_or_404(GameSession, pk=game_session_id)
    # Récupérer la question associée à la session de jeu
    # Assurez-vous que votre modèle GameSession a un champ pour stocker la question actuelle
    question = game_session.current_question
    return render(request, 'game/question.html', {'question': question, 'game_session': game_session})

def submit_answer(request, game_session_id):
    game_session = get_object_or_404(GameSession, pk=game_session_id)
    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        if selected_answer == game_session.current_question.correct_answer:
            # Si la réponse est correcte, recherchez la prochaine question
            next_question = Question.objects.filter(order__gt=game_session.current_question.order).order_by('order').first()
            if next_question:
                logging.debug(next_question)
                # Mettez à jour la session de jeu avec la nouvelle question
                game_session.current_question = next_question
                game_session.save()
                # Redirigez l'utilisateur vers la page de la nouvelle question
                return redirect('game:question', game_session_id=game_session.id)
            else:
                # Si c'était la dernière question, redirigez vers une page de fin de jeu
                return render(request, 'game/game_over.html', {'message': 'Félicitations! Vous avez terminé le jeu.'})
        else:
            # Si la réponse est incorrecte, affichez un message d'erreur
            error_message = 'Désolé, votre réponse est incorrecte. Essayez à nouveau.'
            return render(request, 'game/question.html', {'game_session': game_session, 'error': error_message})
    # Si la méthode n'est pas POST, redirigez l'utilisateur vers la page de la question actuelle
    return redirect('game:question', game_session_id=game_session.id)

from django.shortcuts import render

def spectator_view():
    pass
def player_signup():
    pass

def player_login():
    pass
def end_game(request):
    # Logique de fin de jeu
    return render(request, 'game/end_game.html')
