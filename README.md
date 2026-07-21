# Excel Converter

Este diretório contém um projeto pessoal legado para converter planilhas Excel em arquivos PDF por meio de uma interface gráfica.

O projeto foi preservado em sua estrutura original. O código, a configuração de empacotamento e os artefatos existentes não foram modificados durante a preparação para versionamento.

## Organização

- `Excel converter.py`: código-fonte principal da aplicação.
- `Excel converter.spec`: configuração existente do PyInstaller.
- `icon.ico`: ícone utilizado pelo empacotamento.
- `build/`: arquivos intermediários gerados pelo PyInstaller; mantidos localmente e ignorados pelo Git.
- `dist/`: executável gerado; mantido localmente e ignorado pelo Git.

Consulte `PROJECTS.md` para o inventário técnico e as limitações conhecidas.

## Tecnologias detectadas

- Python 3.11 no build legado e Python 3.14 no ambiente de validação atual;
- Tkinter para a interface gráfica;
- pandas para leitura das planilhas;
- módulo `fpdf` para geração dos arquivos PDF;
- PyInstaller para geração do executável Windows.

As dependências diretas estão registradas em `requirements.txt`. O ambiente completo usado nos testes, na auditoria e no empacotamento está fixado em `requirements-lock.txt`.

## Instalação e execução

Crie um ambiente virtual e instale as dependências de execução:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe "Excel converter.py"
```

Para reproduzir o ambiente completo de desenvolvimento e executar as validações:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe -m pytest
$env:PYTHONUTF8 = "1"
.\.venv\Scripts\python.exe -m pip_audit -r requirements-lock.txt
.\.venv\Scripts\python.exe -m PyInstaller "Excel converter.spec"
```

Os testes automatizados validam a localização portátil do ícone, a leitura de uma planilha `.xlsx` e a geração de um PDF. O build PyInstaller também foi concluído com sucesso. A seleção manual de arquivos e a aparência final da interface ainda devem ser verificadas interativamente em cada ambiente.

## Versionamento

Os diretórios `build/` e `dist/` são artefatos gerados e permanecem fora do versionamento. O arquivo `Excel converter.spec` e o ícone são preservados como entradas necessárias para uma futura reconstrução.

O workflow em `.github/workflows/ci.yml` executa testes, auditoria das dependências e validação do build. O Dependabot acompanha as dependências Python e as GitHub Actions.

Nenhuma licença foi escolhida para este projeto.
