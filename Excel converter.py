import pandas as pd
from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import sys


def caminho_recurso(nome_arquivo):
    diretorio_base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return diretorio_base / nome_arquivo

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Tabela Convertida do Excel para PDF", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    def add_table(self, df):
        self.set_font("Arial", "B", 10)
        col_width = self.epw / len(df.columns)  # largura ajustada ao número de colunas

        # Cabeçalho da tabela
        for col in df.columns:
            self.cell(col_width, 10, str(col), border=1)
        self.ln()

        self.set_font("Arial", "", 10)

        # Dados da tabela
        for _, row in df.iterrows():
            for item in row:
                texto = str(item)
                if len(texto) > 30:  # Trunca textos muito longos
                    texto = texto[:27] + "..."
                self.cell(col_width, 10, texto, border=1)
            self.ln()

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo Excel",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )
    if caminho_arquivo:
        try:
            df = pd.read_excel(caminho_arquivo)
            if df.empty:
                messagebox.showwarning("Aviso", "A planilha está vazia.")
                return
            salvar_pdf(df)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o Excel:\n{str(e)}")

def salvar_pdf(df):
    pdf = PDF(orientation='L')  # Modo paisagem para melhor aproveitamento horizontal
    pdf.add_page()
    pdf.add_table(df)

    caminho_pdf = filedialog.asksaveasfilename(
        title="Salvar PDF como...",
        defaultextension=".pdf",
        filetypes=[("Arquivo PDF", "*.pdf")]
    )
    if caminho_pdf:
        try:
            pdf.output(caminho_pdf)
            messagebox.showinfo("Sucesso", f"PDF salvo em:\n{caminho_pdf}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar PDF:\n{str(e)}")

# Interface Gráfica
def iniciar_interface():
    janela = tk.Tk()
    janela.title("Conversor Excel → PDF")
    janela.geometry("350x150")
    janela.resizable(False, False)
    janela.iconbitmap(str(caminho_recurso("icon.ico")))

    rotulo = tk.Label(janela, text="Clique abaixo para converter sua planilha Excel para PDF.", font=("Arial", 10), wraplength=300, justify="center")
    rotulo.pack(pady=20)

    botao = tk.Button(janela, text="Selecionar Arquivo Excel", command=selecionar_arquivo, font=("Arial", 10), width=30)
    botao.pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    iniciar_interface()
