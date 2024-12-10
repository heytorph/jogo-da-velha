import tkinter as tk

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        self.tabuleiro = [" " for _ in range(9)]  
        self.jogador_atual = "X"
        self.botoes = []

        # Fundo preto
        self.master.configure(bg="black")

        # Frame para os nomes dos jogadores
        frame_jogadores = tk.Frame(master, bg="black")
        frame_jogadores.grid(row=0, column=0, columnspan=3)

        # Nomes dos jogadores
        self.label_jogador1 = tk.Label(frame_jogadores, text="Jogador 1 (X)", fg="purple", bg="black", font=("Arial", 12))
        self.label_jogador1.pack(side="left", padx=50)

        self.label_jogador2 = tk.Label(frame_jogadores, text="Jogador 2 (O)", fg="red", bg="black", font=("Arial", 12))
        self.label_jogador2.pack(side="right", padx=50)

        # Botões com fundo preto 
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(master, text=" ", width=10, height=3, bg="black", fg="white", font=("Arial", 20),
                                  highlightbackground="purple", highlightthickness=4, 
                                  command=lambda i=i, j=j: self.jogar(i, j))
                botao.grid(row=i+1, column=j, padx=5, pady=5)  
                linha.append(botao)
            self.botoes.append(linha)

        # Botão reiniciar o jogo
        botao_reiniciar = tk.Button(master, text="Reiniciar", command=self.resetar_jogo, bg="blue", fg="white", font=("Arial", 12))
        botao_reiniciar.grid(row=4, column=0, columnspan=3, pady=10)

    def jogar(self, i, j):
        index = i * 3 + j
        if self.tabuleiro[index] == " ":
            self.tabuleiro[index] = self.jogador_atual
            self.botoes[i][j].config(text=self.jogador_atual, fg="purple" if self.jogador_atual == "X" else "red")
            
            if self.verifica_vitoria():
                print(f"Jogador {self.jogador_atual} venceu!")  
                self.resetar_jogo()
            elif " " not in self.tabuleiro:
                print("Empate!")  
                self.resetar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verifica_vitoria(self):
        
        for i in range(3):
            if self.tabuleiro[i*3] == self.tabuleiro[i*3+1] == self.tabuleiro[i*3+2] != " ":
                return True
            if self.tabuleiro[i] == self.tabuleiro[i+3] == self.tabuleiro[i+6] != " ":
                return True
        if self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] != " ":
            return True
        if self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] != " ":
            return True
        return False

    def resetar_jogo(self):
        self.tabuleiro = [" " for _ in range(9)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text=" ", fg="white")  
        self.jogador_atual = "X"

root = tk.Tk()
jogo = JogoDaVelha(root)

root.mainloop()
