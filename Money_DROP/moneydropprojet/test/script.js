function playSound(soundId) {
    var sound = document.getElementById(soundId);
    sound.play();
}
document.addEventListener('DOMContentLoaded', function() {
    var answerButtons = document.querySelectorAll('.answer');

    answerButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var soundId = button.getAttribute('data-sound');
            var sound = document.getElementById(soundId);
            sound.play();
        });
    });
});

function startTimer() {
    var timer = setInterval(function() {
        if (duration <= 0) {
            clearInterval(timer);
            // Rediriger l'utilisateur vers une page de fin de jeu ou effectuer une autre action
            // window.location.href = "{% url 'game:end_game' %}";
        } else {
            var minutes = Math.floor(duration / 60);
            var seconds = duration % 60;
            timerDisplay.textContent = "Temps restant : " + minutes.toString().padStart(2, '0') + ":" + seconds.toString().padStart(2, '0');
            duration--;
        }
    }, 1000); // Mettre à jour le timer chaque seconde
}

function submitAnswer() {
    var selectedAnswer = document.querySelector('input[name="answer"]:checked');
    if (!selectedAnswer) {
        alert("Veuillez sélectionner une réponse.");
        return false;
    }
    if (selectedAnswer.value === "{{ game_session.current_question.correct_answer }}") {
        // Si la réponse est correcte, faites quelque chose (par exemple, affichez un message)
        
        playWaitingAudio()
        alert("Félicitations! Vous avez choisi la bonne réponse.");



    } else {
        // Si la réponse est incorrecte, faites quelque chose d'autre (par exemple, affichez un message d'erreur)
        alert("Désolé, votre réponse est incorrecte. Essayez à nouveau.");
    }
}



	// Jouer le son "attente"
	function playWaitingAudio() {
	    waitingAudio.play();
	}

	// Jouer le son "bonne réponse"
	function playCorrectAudio() {
	    correctAudio.play();
	}

	// Jouer le son "mauvaise réponse"
	function playWrongAudio() {
	    wrongAudio.play();
	}
