# Projetos

## Excel Converter

| Campo | Informação |
| --- | --- |
| Caminho | Raiz deste diretório |
| Finalidade aparente | Converter planilhas `.xlsx` ou `.xls` em arquivos PDF por meio de uma interface gráfica |
| Linguagem | Python |
| Tecnologias detectadas | Tkinter, pandas, módulo `fpdf` e PyInstaller |
| Ambiente do build existente | Python 3.11 para Windows |
| Status aparente | Projeto legado com artefato de build; funcionamento atual não validado |
| Instruções existentes | Nenhuma documentação de instalação, execução ou teste foi encontrada |

### Arquivos principais

- `Excel converter.py`: implementação da interface e da conversão.
- `Excel converter.spec`: configuração de empacotamento do PyInstaller.
- `icon.ico`: recurso utilizado pela configuração de empacotamento.

### Observações

- Não existe manifesto de dependências com versões reproduzíveis.
- A distribuição responsável pelo módulo importado como `fpdf` não foi determinada com segurança.
- `Excel converter.py` contém um caminho absoluto do computador original para carregar o ícone da janela.
- `build/` contém arquivos intermediários e relatórios do PyInstaller.
- `dist/Excel converter.exe` é um executável gerado, sem assinatura digital ou metadados de versão detectáveis.
- Nenhum teste ou aplicação desconhecida foi executado durante a preparação para Git.
