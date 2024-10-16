# ORIENTADO A OBJETO - Implemente um jogo da forca para dois ou mais jogadores com uma temática personalizada. O programa deve permitir que um dos jogadores insira uma palavra e dicas e o(s) outro(s) jogador(es) tente(m) adivinhá-la dentro de um limite máximo de tentativas pré-estabelecido (i.e. a formação do boneco na forca). Adicione um sistema de pontuação que se baseie no número de tentativas e na dificuldade da palavra. No final de cada rodada (i.e. o boneco foi formado por completo ou alguém descobriu a palavra), o sistema deverá exibir o ranking dos jogadores, ordenados em ordem decrescente com base na quantidade de pontos.
import os

class Hangman:
    def __init__(self):
        self.word = ''
        self.hint = ''
        self.players = []
        self.scores = {}
        self.max_attempts = 6
        self.attempts = 0
        self.current_player = ''
        self.guessed_word = []
    
    def add_player(self, player):
        self.players.append(player)
        self.scores[player] = 0
    
    def play(self):
        print("Bem-vindo ao jogo da forca!")
        
        # Solicitar a palavra e a dica
        self.word = input("Digite a palavra: ")
        self.hint = input("Digite a dica: ")
        
        self.clear_terminal()
        
        if (len(self.players) > 0):
            print(f"Jogadores cadastrados: {', '.join(self.players)}")
            
        while True:
            player = input("Digite o nome do jogador (ou '0' para começar o jogo): ")
            if player == '0':
                if len(self.players) >= 2:
                    break
                else:
                    print("Você precisa adicionar pelo menos dois jogadores.")
            else:
                self.add_player(player)
        
        self.start_game()
    
    def start_game(self):
        self.current_player = self.players[0]
        self.attempts = 0
        self.guessed_word = ['_' if letter.isalpha() else letter for letter in self.word]
        self.play_round()
        
    def get_play_infors(self):
        print(f"\nJogador: {self.current_player}")
        print(f"Dica: {self.hint}")
        print(f"Palavra: {' '.join(self.guessed_word)}")
        
    def get_scores(self):
        print(f"Pontuação:")
        for player, score in self.scores.items():
            print(f"{player}: {score}")
    
    def play_round(self):
        self.get_play_infors()
        guess = input("Digite uma letra ou a palavra completa: ")
        
        if len(guess) == 1:
            if guess in self.word:
                print("\nLetra correta!")
                self.scores[self.current_player] += 1
                for i, letter in enumerate(self.word):
                    if letter == guess:
                        self.guessed_word[i] = guess
                if '_' not in self.guessed_word:
                    self.scores[self.current_player] += 1
                    self.get_scores()
                    self.try_again()
                else:
                    self.play_round()
            else:
                print("\nLetra incorreta!")
                self.attempts += 1
                if self.attempts == self.max_attempts:
                    print(f"Tentativas expiradas, a palavra era {self.word}")
                    self.try_again()
                else:
                    print(f"Tentativas restantes: {self.max_attempts - self.attempts}/6")
                    self.next_player()
                    self.play_round()
        else:
            if guess == self.word:
                print("\nPalavra correta, parabéns!")
                self.scores[self.current_player] += 2
                self.get_scores()
                self.try_again()
            else:
                print("\nPalavra incorreta!")
                self.attempts += 1
                if self.attempts == self.max_attempts:
                    print(f"Tentativas expiradas, a palavra era {self.word}")
                    self.try_again()
                else:
                    self.next_player()
                    self.play_round()
                    
    def next_player(self):
        self.players.append(self.players.pop(0))
        self.current_player = self.players[0]
    
    def try_again(self):
        answer = input("\n\nDeseja jogar novamente? (s/n): ")
        if answer.lower() == 's':
            print("\nJogo reiniciado!")
            self.play()
        else:
            self.end_game()
                
    def end_game(self):
        print("\nJogo finalizado!")
        print("Ranking:")
        for player, score in sorted(self.scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{player}: {score}")
            
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Palavra escondida! Esse é o nosso segredo :D\n\n")
            
game = Hangman()
game.play()