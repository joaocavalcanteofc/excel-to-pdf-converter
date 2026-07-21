# Projetos

## Excel Converter

| Campo | Informação |
| --- | --- |
| Caminho | Raiz deste diretório |
| Finalidade aparente | Converter planilhas `.xlsx` ou `.xls` em arquivos PDF por meio de uma interface gráfica |
| Linguagem | Python |
| Tecnologias detectadas | Tkinter, pandas, módulo `fpdf` e PyInstaller |
| Ambientes validados | Build legado com Python 3.11 e validação atual com Python 3.14 para Windows |
| Status aparente | Projeto legado com núcleo de conversão e empacotamento validados; interface ainda requer verificação manual completa |
| Instruções existentes | Instalação, execução, testes, auditoria e build documentados no `README.md` |

### Arquivos principais

- `Excel converter.py`: implementação da interface e da conversão.
- `Excel converter.spec`: configuração de empacotamento do PyInstaller.
- `icon.ico`: recurso utilizado pela configuração de empacotamento.

### Observações

- As dependências diretas e o ambiente completo de validação estão registrados em manifests separados.
- O módulo `fpdf` é fornecido pela distribuição `fpdf2` fixada no manifesto.
- O ícone é resolvido de forma portátil tanto no código-fonte quanto no bundle PyInstaller.
- `build/` contém arquivos intermediários e relatórios do PyInstaller.
- `dist/Excel converter.exe` é um executável gerado, sem assinatura digital ou metadados de versão detectáveis.
- Os testes automatizados cobrem a leitura de `.xlsx`, a geração de PDF e a resolução do ícone.
