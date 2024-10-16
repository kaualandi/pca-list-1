import random

class WordGuessGame:
    def __init__(self, word_list, attempts=6):
        self.word_list = word_list
        self.target_word = random.choice(self.word_list).lower()
        self.max_attempts = attempts
        self.attempts_left = attempts
        self.history = []
    
    def make_guess(self, guess):
        guess = guess.lower()
        if len(guess) != len(self.target_word):
            return f"Seu chute deve ter {len(self.target_word)} letras, mas tem {len(guess)}."
        
        self.attempts_left -= 1
        result = self.generate_hint(guess)
        self.history.append((guess, result))
        return result

    def generate_hint(self, guess):
        feedback = ['_'] * len(self.target_word)
        target_word_copy = list(self.target_word)
        
        # Verificar por letras corretas nas posições corretas
        for i, letter in enumerate(guess):
            if letter == self.target_word[i]:
                feedback[i] = letter
                target_word_copy[i] = None  # Marcar metra como 'usada'
        
        # Verificar por letras corretas nas posições erradas
        for i, letter in enumerate(guess):
            if feedback[i] == '_' and letter in target_word_copy:
                feedback[i] = '*'
                target_word_copy[target_word_copy.index(letter)] = None
        
        return ''.join(feedback)

    def is_game_over(self):
        return self.attempts_left <= 0 or self.has_won()

    def has_won(self):
        return any(guess == self.target_word for guess, _ in self.history)

    def play(self):
        print(f"Bem vindo ao jogo de adivinhação! Você tem {self.max_attempts} tentativas para acertar a palavra.")
        print(f"TEMA: Go Horse - O amigo dos devs!")
        print(f"\nQuando você acertar uma letra na posição correta, ela será exibida.")
        print(f"Quando você acertar uma letra na palavra, mas na posição errada, ela será exibida com um asterisco.")
        print(f"Todas as palavras estão em português e sem acentos.")
        print(f"\nA palavra tem {len(self.target_word)} letras.")
        print(f"\nBoa sorte!\n")
        
        while not self.is_game_over():
            guess = input(f"\nTentativas restantes: {self.attempts_left}. Digite seu chute: ")
            hint = self.make_guess(guess)
            print(f"Dica: {hint}")
        
        if self.has_won():
            print(f"\nParabéns! Você adivinhou a palavra '{self.target_word}'!")
        else:
            print(f"\nFim de Jogo! A palavra correta era '{self.target_word}'.")


if __name__ == "__main__":
    word_list = ['gambiarra', 'chutometro', 'provisorio', 'bugado', 'desespero', 'quebragalho', 'testar']
    game = WordGuessGame(word_list)
    game.play()
