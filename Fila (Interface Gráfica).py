import tkinter as tk
from tkinter import messagebox

class FilaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Fila")
        self.master.geometry("400x300")  # Tamanho fixo da janela
        self.master.config(bg="#f0f8ff")  # Cor de fundo da janela

        self.fila = []

        # Frame para os botões
        self.frame = tk.Frame(master, bg="#f0f8ff")
        self.frame.pack(pady=20)

        # Campo de entrada
        self.entry = tk.Entry(master, width=30, font=("Arial", 12), bd=2, relief="solid")
        self.entry.pack(pady=10)

        # Botões
        self.btn_inserir = tk.Button(self.frame, text="Inserir", command=self.inserir_elemento,
                                      bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
                                      relief="raised", bd=3, padx=10, pady=5)
        self.btn_inserir.pack(side=tk.LEFT, padx=10)

        self.btn_remover = tk.Button(self.frame, text="Remover", command=self.remover_elemento,
                                      bg="#f44336", fg="white", font=("Arial", 12, "bold"),
                                      relief="raised", bd=3, padx=10, pady=5)
        self.btn_remover.pack(side=tk.LEFT, padx=10)

        # Label para exibir a fila
        self.label_fila = tk.Label(master, text="Fila: []", font=("Arial", 14), bg="#f0f8ff", fg="#333333")
        self.label_fila.pack(pady=20)

    def inserir_elemento(self):
        elemento = self.entry.get()
        if elemento:
            self.fila.append(elemento)
            self.atualizar_fila()
            self.entry.delete(0, tk.END)  # Limpa o campo de entrada
            messagebox.showinfo("Sucesso", f"Elemento '{elemento}' inserido na fila!")
        else:
            messagebox.showwarning("Atenção", "Por favor, insira um elemento.")

    def remover_elemento(self):
        if self.fila:
            elemento_removido = self.fila.pop(0)
            self.atualizar_fila()
            messagebox.showinfo("Sucesso", f"Elemento '{elemento_removido}' removido da fila!")
        else:
            messagebox.showwarning("Atenção", "A fila está vazia.")

    def atualizar_fila(self):
        self.label_fila.config(text=f"Fila: {self.fila}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FilaApp(root)
    root.mainloop()
