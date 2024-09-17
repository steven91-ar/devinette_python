# Importer la bibliothèque random
import random


# Définir une fonction pour obtenir un nombre aléatoire
def get_random_number():
    return random.randint(1, 30)


# Définir une fonction pour jouer au jeu de devinette
def play_guessing_game():
    # Obtenir le nombre aléatoire
    number_to_guess = get_random_number()

    # Initialiser le nombre de tentatives
    attempts = 0

    # Boucle pour jouer au jeu
    while True:
        # Demander à l'utilisateur de deviner le nombre
        user_guess = int(input("Devinez le nombre : "))

        # Incrémenter le nombre de tentatives
        attempts += 1

        # Vérifier si l'utilisateur a deviné le nombre
        if user_guess == number_to_guess:
            print(f"Félicitations ! Vous avez deviné le nombre en {attempts} tentatives.")
            break
        elif user_guess < number_to_guess:
            print("Votre nombre est trop bas. Essayez à nouveau.")
        else:
            print("Votre nombre est trop haut. Essayez à nouveau.")


# Jouer au jeu de devinette
play_guessing_game()